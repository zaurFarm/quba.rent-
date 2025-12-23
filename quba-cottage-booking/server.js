/**
 * Quba Cottage Booking System
 * Main Server File
 * 
 * Features:
 * - REST API for booking management
 * - Telegram Bot with AI assistant
 * - Database integration (MongoDB)
 * - Payment verification
 * - Notifications to admin
 */

require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');
const path = require('path');

// Import modules
const TelegramBot = require('./bot/telegramBot');
const BookingManager = require('./services/bookingManager');
const AIManager = require('./services/aiManager');
const Database = require('./services/database');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, '../quba-cottage/public')));

// Store for in-memory data (can be replaced with MongoDB)
const bookings = new Map();
const availableDates = new Set();
const settings = {
    pricePerNight: 150, // AZN
    minNights: 2,
    maxGuests: 6,
    adminChatId: null,
    botToken: process.env.TELEGRAM_BOT_TOKEN || 'YOUR_BOT_TOKEN',
    openaiKey: process.env.OPENAI_API_KEY || 'YOUR_OPENAI_KEY'
};

// Initialize services
let telegramBot = null;
let aiManager = null;
let bookingManager = null;

// ==================== API ROUTES ====================

// Get availability
app.get('/api/availability', (req, res) => {
    res.json({
        success: true,
        availableDates: Array.from(availableDates),
        settings: {
            pricePerNight: settings.pricePerNight,
            minNights: settings.minNights,
            maxGuests: settings.maxGuests
        }
    });
});

// Create booking
app.post('/api/booking', async (req, res) => {
    try {
        const { name, phone, email, checkIn, checkOut, guests, notes } = req.body;
        
        // Validate required fields
        if (!name || !phone || !checkIn || !checkOut) {
            return res.status(400).json({
                success: false,
                message: 'Zəhmət olmasa bütün məlumatları doldurun / Please fill all required fields'
            });
        }
        
        // Create booking ID
        const bookingId = uuidv4().substring(0, 8).toUpperCase();
        
        // Calculate total price
        const nights = Math.ceil((new Date(checkOut) - new Date(checkIn)) / (1000 * 60 * 60 * 24));
        const totalPrice = nights * settings.pricePerNight;
        
        // Create booking object
        const booking = {
            id: bookingId,
            name,
            phone,
            email: email || '',
            checkIn,
            checkOut,
            guests: guests || 2,
            nights,
            totalPrice,
            notes: notes || '',
            status: 'pending',
            createdAt: new Date().toISOString(),
            paymentStatus: 'unpaid'
        };
        
        // Store booking
        bookings.set(bookingId, booking);
        
        // Notify admin via Telegram
        if (telegramBot) {
            await telegramBot.sendBookingNotification(booking);
        }
        
        // Mark dates as unavailable
        let currentDate = new Date(checkIn);
        while (currentDate < new Date(checkOut)) {
            availableDates.add(currentDate.toISOString().split('T')[0]);
            currentDate.setDate(currentDate.getDate() + 1);
        }
        
        res.json({
            success: true,
            message: 'Rezervasiya qəbul edildi! / Booking accepted!',
            bookingId,
            totalPrice,
            nights
        });
        
    } catch (error) {
        console.error('Booking error:', error);
        res.status(500).json({
            success: false,
            message: 'Xəta baş verdi / Error occurred'
        });
    }
});

// Get booking status
app.get('/api/booking/:id', (req, res) => {
    const booking = bookings.get(req.params.id);
    
    if (booking) {
        res.json({
            success: true,
            booking
        });
    } else {
        res.status(404).json({
            success: false,
            message: 'Rezervasiya tapılmadı / Booking not found'
        });
    }
});

// Payment confirmation (webhook from payment system)
app.post('/api/payment/confirm', async (req, res) => {
    try {
        const { bookingId, paymentId, status } = req.body;
        const booking = bookings.get(bookingId);
        
        if (booking) {
            booking.paymentStatus = status === 'success' ? 'paid' : 'failed';
            booking.paymentId = paymentId;
            booking.status = status === 'success' ? 'confirmed' : 'pending';
            
            bookings.set(bookingId, booking);
            
            // Notify admin
            if (telegramBot) {
                await telegramBot.sendPaymentNotification(booking);
            }
            
            res.json({ success: true });
        } else {
            res.status(404).json({ success: false, message: 'Booking not found' });
        }
    } catch (error) {
        console.error('Payment confirmation error:', error);
        res.status(500).json({ success: false, message: 'Error confirming payment' });
    }
});

// Admin: Get all bookings
app.get('/api/admin/bookings', (req, res) => {
    const allBookings = Array.from(bookings.values()).sort(
        (a, b) => new Date(b.createdAt) - new Date(a.createdAt)
    );
    
    res.json({
        success: true,
        bookings: allBookings,
        total: allBookings.length,
        pending: allBookings.filter(b => b.status === 'pending').length,
        confirmed: allBookings.filter(b => b.status === 'confirmed').length
    });
});

// Admin: Confirm/reject booking
app.post('/api/admin/booking/:id', async (req, res) => {
    const { action, adminNote } = req.body;
    const booking = bookings.get(req.params.id);
    
    if (booking) {
        if (action === 'confirm') {
            booking.status = 'confirmed';
            booking.adminNote = adminNote || '';
            
            // Notify user via Telegram (if they have username)
            if (telegramBot) {
                await telegramBot.sendUserConfirmation(booking);
            }
        } else if (action === 'reject') {
            booking.status = 'rejected';
            booking.adminNote = adminNote || '';
            
            // Free up dates
            let currentDate = new Date(booking.checkIn);
            while (currentDate < new Date(booking.checkOut)) {
                availableDates.delete(currentDate.toISOString().split('T')[0]);
                currentDate.setDate(currentDate.getDate() + 1);
            }
        } else if (action === 'cancel') {
            booking.status = 'cancelled';
            
            // Free up dates
            let currentDate = new Date(booking.checkIn);
            while (currentDate < new Date(booking.checkOut)) {
                availableDates.delete(currentDate.toISOString().split('T')[0]);
                currentDate.setDate(currentDate.getDate() + 1);
            }
        }
        
        bookings.set(req.params.id, booking);
        
        res.json({
            success: true,
            message: `Booking ${action}ed successfully`
        });
    } else {
        res.status(404).json({
            success: false,
            message: 'Booking not found'
        });
    }
});

// AI Chat endpoint
app.post('/api/ai/chat', async (req, res) => {
    const { message, context } = req.body;
    
    if (aiManager) {
        try {
            const response = await aiManager.chat(message, context);
            res.json({
                success: true,
                response
            });
        } catch (error) {
            res.status(500).json({
                success: false,
                message: 'AI暂时不可用 / AI temporarily unavailable'
            });
        }
    } else {
        res.json({
            success: true,
            response: "Salam! Ailəvi istirahət üçün əla seçim. Rezervasiya etmək üçün əlaqə saxlayın: +994 70 255 59 09\n\nHello! Great choice for family vacation. Contact to book: +994 70 255 59 09"
        });
    }
});

// Serve main page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../quba-cottage/public/index.html'));
});

// ==================== INITIALIZATION ====================

async function initializeServices() {
    try {
        // Initialize Database
        console.log('📦 Initializing database...');
        await Database.connect();
        
        // Initialize Telegram Bot
        console.log('🤖 Initializing Telegram bot...');
        try {
            telegramBot = new TelegramBot(settings.botToken);
            telegramBot.setBookingManager({
                getAllBookings: () => Array.from(bookings.values()),
                confirmBooking: (id, note) => {
                    const booking = bookings.get(id);
                    if (booking) {
                        booking.status = 'confirmed';
                        booking.adminNote = note;
                        bookings.set(id, booking);
                        return true;
                    }
                    return false;
                },
                rejectBooking: (id, note) => {
                    const booking = bookings.get(id);
                    if (booking) {
                        booking.status = 'rejected';
                        booking.adminNote = note;
                        bookings.set(id, booking);
                        return true;
                    }
                    return false;
                },
                getSettings: () => settings
            });
            
            // Start bot polling
            telegramBot.start();
            console.log('✅ Telegram bot started!');
        } catch (error) {
            console.log('⚠️ Telegram bot initialization failed (check TOKEN)');
        }
        
        // Initialize AI Manager
        console.log('🧠 Initializing AI manager...');
        try {
            aiManager = new AIManager(settings.openaiKey, {
                pricePerNight: settings.pricePerNight,
                location: 'Kusnet Qazma, Quba, Azerbaijan',
                features: ['Wi-Fi', 'Parking', 'Kitchen', 'Heating', 'BBQ', 'River access', 'Fireplace']
            });
            console.log('✅ AI manager ready!');
        } catch (error) {
            console.log('⚠️ AI initialization failed (check OPENAI_API_KEY)');
        }
        
        // Start server
        app.listen(PORT, () => {
            console.log(`
╔════════════════════════════════════════════════╗
║         🏠 Quba Cottage Booking System          ║
╠════════════════════════════════════════════════╣
║  Server running on: http://localhost:${PORT}       ║
║  API Base URL: http://localhost:${PORT}/api         ║
╠════════════════════════════════════════════════╣
║  📅 Booking API: POST /api/booking              ║
║  📋 Get Bookings: GET /api/admin/bookings       ║
║  💬 AI Chat: POST /api/ai/chat                  ║
╚════════════════════════════════════════════════╝
            `);
        });
        
    } catch (error) {
        console.error('Initialization failed:', error);
        process.exit(1);
    }
}

// Handle graceful shutdown
process.on('SIGINT', () => {
    console.log('\n👋 Shutting down gracefully...');
    if (telegramBot) {
        telegramBot.stop();
    }
    process.exit(0);
});

// Start the application
initializeServices();

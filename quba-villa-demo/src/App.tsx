import { useState } from 'react'
import { MapPin, Phone, Mail, Clock, Calendar, Star } from 'lucide-react'

function App() {
  const [selectedLang, setSelectedLang] = useState('az')

  const translations = {
    az: {
      title: "Kübə Villa Premium",
      subtitle: "Dağlıq İstirahət & Turizm",
      description: "Premium villa accommodation in Quba mountains. Tours, activities, WhatsApp booking. Neriman - local guide with 25 years experience.",
      heroTitle: "Dağlıq Kübədə Premium İstirahət",
      heroDesc: "Turlar və fəaliyyətlər. WhatsApp ilə bir klik rezervasiya. Neriman - yerli rehber.",
      aboutTitle: "Haqqımızda",
      aboutDesc: "25 illik təcrübə ilə dağlıq Kübədə premium istirahət təklif edirik. Bütün fəaliyyətlər və turlar yerli rehber Neriman tərəfindən təşkil olunur.",
      locationTitle: "Məkan",
      locationDesc: "Kübə, Azərbaycan",
      bookingTitle: "İndi Rezervasiya Edin",
      bookingDesc: "Calendly ilə onlayn rezervasiya - asanlıqla vaxt seçin və sürətlə təsdiq edin",
      contactTitle: "Əlaqə",
      phone: "+994 70 255 59 09 (Neriman)",
      email: "neriman@quba-villa.com",
      hours: "7/24 - 08:00-20:00",
      features: [
        "🏔️ Turlar və Ekskursiyalar",
        "🏇 At sürüşü", 
        "🏍️ ATV Adventures",
        "🥾 Dağ Gəzintiləri",
        "📸 Fotoqrafiya Turları",
        "🎭 Mədəni Təcrübə"
      ]
    },
    en: {
      title: "Quba Villa Premium",
      subtitle: "Mountain Tourism & Events",
      description: "Premium villa accommodation in Quba mountains. Tours, activities, WhatsApp booking. Neriman - local guide with 25 years experience.",
      heroTitle: "Premium Mountain Stay in Quba",
      heroDesc: "Tours & activities. One-click WhatsApp booking. Neriman - local guide.",
      aboutTitle: "About",
      aboutDesc: "With 25 years of experience, we offer premium mountain relaxation in Quba. All activities and tours organized by local guide Neriman.",
      locationTitle: "Location", 
      locationDesc: "Quba, Azerbaijan",
      bookingTitle: "Book Your Stay Now",
      bookingDesc: "Online booking with Calendly - select your preferred time and get instant confirmation",
      contactTitle: "Contact",
      phone: "+994 70 255 59 09 (Neriman)",
      email: "neriman@quba-villa.com", 
      hours: "7/24 - 08:00-20:00",
      features: [
        "🏔️ Tours & Excursions",
        "🏇 Horse Riding",
        "🏍️ ATV Adventures", 
        "🥾 Mountain Hiking",
        "📸 Photography Tours",
        "🎭 Cultural Experience"
      ]
    },
    ru: {
      title: "Куба Вилла Премиум",
      subtitle: "Горный Туризм & Мероприятия",
      description: "Премиум вилла в горах Куба. Туры, активности, бронирование WhatsApp. Нэриман - местный гид с 25-летним опытом.",
      heroTitle: "Премиум Горный Отдых в Губе",
      heroDesc: "Туры и активности. Однокликовое бронирование WhatsApp. Нэриман - местный гид.",
      aboutTitle: "О нас",
      aboutDesc: "С 25-летним опытом предлагаем премиум горный отдых в Губе. Все активности и туры организует местный гид Нэриман.",
      locationTitle: "Местоположение",
      locationDesc: "Куба, Азербайджан",
      bookingTitle: "Забронируйте Сейчас", 
      bookingDesc: "Онлайн бронирование с Calendly - выберите удобное время и получите мгновенное подтверждение",
      contactTitle: "Контакты",
      phone: "+994 70 255 59 09 (Нэриман)",
      email: "neriman@quba-villa.com",
      hours: "7/24 - 08:00-20:00",
      features: [
        "🏔️ Туры и Экскурсии",
        "🏇 Конные Прогулки",
        "🏍️ Приключения на ATV", 
        "🥾 Горные Походы",
        "📸 Фототур",
        "🎭 Культурный Опыт"
      ]
    },
    ar: {
      title: "كوتج كوبة فريميوم",
      subtitle: "السياحة الجبلية & الفعاليات",
      description: "إقامة فيلا فريميوم в جبال كوبة. جولات، أنشطة، حجز واتساب. نيريمان - مرشد محلي بخبرة 25 عاماً.",
      heroTitle: "إقامة جبلية فريميوم في كوبة",
      heroDesc: "جولات وأنشطة. حجز واتساب بنقرة واحدة. نيريمان - مرشد محلي.",
      aboutTitle: "من نحن",
      aboutDesc: "مع خبرة 25 عاماً، نقدم إقامة جبلية فريميوم в كوبة. جميع الأنشطة والجولات ينظمها المرشد المحلي نيريمان.",
      locationTitle: "الموقع",
      locationDesc: "كوبة، أذربيجان", 
      bookingTitle: "احجز رحلتك الآن",
      bookingDesc: "حجز عبر الإنترنت مع Calendly - اختر الوقت المناسب واحصل على تأكيد فوري",
      contactTitle: "التواصل",
      phone: "+994 70 255 59 09 (نيريمان)",
      email: "neriman@quba-villa.com",
      hours: "7/24 - 08:00-20:00",
      features: [
        "🏔️ جولات و excursions",
        "🏇 ركوب الخيل",
        "🏍️ مغامرات ATV",
        "🥾 رحلات جبلية", 
        "📸 جولات التصوير",
        "🎭 التجربة الثقافية"
      ]
    }
  }

  const t = translations[selectedLang as keyof typeof translations]

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-800 via-green-700 to-green-900">
      {/* Language Selector */}
      <div className="fixed top-4 right-4 z-50">
        <select 
          value={selectedLang}
          onChange={(e) => setSelectedLang(e.target.value)}
          className="bg-white/20 backdrop-blur-sm text-white border border-white/30 rounded-lg px-3 py-2"
        >
          <option value="az" className="text-black">AZ</option>
          <option value="en" className="text-black">EN</option>
          <option value="ru" className="text-black">RU</option>
          <option value="ar" className="text-black">AR</option>
        </select>
      </div>

      {/* Hero Section */}
      <div className="relative h-screen flex items-center justify-center text-center text-white px-4">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-6xl md:text-8xl font-bold mb-6 bg-gradient-to-r from-yellow-300 to-yellow-500 bg-clip-text text-transparent">
            🏔️ {t.title}
          </h1>
          <h2 className="text-2xl md:text-4xl font-light mb-8 text-yellow-200">
            {t.subtitle}
          </h2>
          <p className="text-lg md:text-xl mb-12 text-white/90 max-w-2xl mx-auto leading-relaxed">
            {t.heroDesc}
          </p>
          
          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <button 
              onClick={() => window.open('https://calendly.com/quba-villa/30min', '_blank')}
              className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-xl font-semibold text-lg transition-all duration-300 transform hover:scale-105 shadow-xl"
            >
              <Calendar className="inline mr-2" size={20} />
              {t.bookingTitle}
            </button>
            
            <button 
              onClick={() => window.open('https://wa.me/994702555909?text=🏔️ Hello! I want to book a stay at Quba Villa', '_blank')}
              className="bg-green-600 hover:bg-green-700 text-white px-8 py-4 rounded-xl font-semibold text-lg transition-all duration-300 transform hover:scale-105 shadow-xl"
            >
              📱 WhatsApp Booking
            </button>
          </div>
        </div>
      </div>

      {/* Content Sections */}
      <div className="bg-white text-gray-900">
        <div className="max-w-6xl mx-auto px-4 py-20">
          
          {/* About Section */}
          <div className="mb-20 text-center">
            <h2 className="text-4xl font-bold mb-6 text-green-800">{t.aboutTitle}</h2>
            <p className="text-xl text-gray-700 max-w-4xl mx-auto leading-relaxed">
              {t.aboutDesc}
            </p>
            <div className="mt-8 flex items-center justify-center gap-4 text-yellow-600">
              <Star className="text-yellow-500" size={24} />
              <span className="text-lg font-semibold">25 Years Experience</span>
              <Star className="text-yellow-500" size={24} />
            </div>
          </div>

          {/* Features Grid */}
          <div className="mb-20">
            <h2 className="text-4xl font-bold text-center mb-12 text-green-800">
              🏔️ Tours & Activities
            </h2>
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
              {t.features.map((feature, index) => (
                <div key={index} className="bg-gradient-to-br from-green-50 to-green-100 p-6 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
                  <p className="text-lg font-semibold text-green-800">{feature}</p>
                </div>
              ))}
            </div>
          </div>

          {/* Contact Section */}
          <div className="bg-gradient-to-r from-green-800 to-green-900 rounded-2xl p-8 text-white text-center">
            <h2 className="text-4xl font-bold mb-8">{t.contactTitle}</h2>
            <div className="grid md:grid-cols-3 gap-8">
              
              <div className="flex flex-col items-center">
                <Phone className="text-yellow-400 mb-3" size={32} />
                <h3 className="text-xl font-semibold mb-2">📞 Phone</h3>
                <p className="text-green-200">{t.phone}</p>
              </div>
              
              <div className="flex flex-col items-center">
                <Mail className="text-yellow-400 mb-3" size={32} />
                <h3 className="text-xl font-semibold mb-2">📧 Email</h3>
                <p className="text-green-200">{t.email}</p>
              </div>
              
              <div className="flex flex-col items-center">
                <Clock className="text-yellow-400 mb-3" size={32} />
                <h3 className="text-xl font-semibold mb-2">🕐 Hours</h3>
                <p className="text-green-200">{t.hours}</p>
              </div>
            </div>
            
            <div className="mt-8">
              <MapPin className="text-yellow-400 mb-3 mx-auto" size={32} />
              <h3 className="text-xl font-semibold mb-2">📍 Location</h3>
              <p className="text-green-200 text-lg">{t.locationDesc}</p>
              <p className="text-green-300 text-sm mt-2">Coordinates: 41.275389, 48.337667</p>
            </div>
          </div>

          {/* SEO Section */}
          <div className="mt-20 bg-gray-50 rounded-xl p-8">
            <h2 className="text-3xl font-bold mb-8 text-center text-green-800">🚀 SEO Optimizations</h2>
            <div className="grid md:grid-cols-2 gap-8">
              <div>
                <h3 className="text-xl font-semibold mb-4 text-green-700">✅ Completed Features</h3>
                <ul className="space-y-2 text-gray-700">
                  <li>• SEO meta tags optimization</li>
                  <li>• Open Graph & Twitter Cards</li>
                  <li>• Schema.org Structured Data</li>
                  <li>• Calendly booking integration</li>
                  <li>• Multi-language support (4 languages)</li>
                  <li>• WhatsApp booking buttons</li>
                  <li>• Interactive map with directions</li>
                  <li>• Mobile responsive design</li>
                </ul>
              </div>
              <div>
                <h3 className="text-xl font-semibold mb-4 text-green-700">📊 Ready for Google</h3>
                <ul className="space-y-2 text-gray-700">
                  <li>• Fast loading times</li>
                  <li>• Clean URL structure</li>
                  <li>• Proper heading hierarchy</li>
                  <li>• Alt tags for images</li>
                  <li>• Internal linking strategy</li>
                  <li>• Geographic targeting</li>
                  <li>• Local business markup</li>
                  <li>• Social media integration</li>
                </ul>
              </div>
            </div>
          </div>

        </div>
      </div>

      {/* Footer */}
      <div className="bg-gray-900 text-white py-8 text-center">
        <p className="text-lg">
          🏔️ <strong>Kübə Villa</strong> - Premium Mountain Tourism
        </p>
        <p className="text-gray-400 mt-2">
          © 2025 Neriman - 25 Years Experience in Quba Tourism
        </p>
        <p className="text-gray-500 text-sm mt-2">
          SEO Optimized • Calendly Integrated • WhatsApp Ready
        </p>
      </div>
    </div>
  )
}

export default App
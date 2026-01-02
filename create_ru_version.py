#!/usr/bin/env python3
"""
Create Russian version from Azerbaijani HTML
Translates content while keeping HTML structure intact
"""

import re
import ftplib

# Translation dictionary - Azerbaijani to Russian
TRANSLATIONS = {
    # Meta tags and SEO
    "Quba Dağ Evi": "Горный дом Куба",
    "Ekoloji Təmiz Dağ Evi": "Экологически чистый горный дом",
    "Bron Edin": "Забронировать",
    "Quba Dağ Evi Küsnet Qazma kəndində": "Горный дом Куба в селе Кюснет Казма",
    "Ailələr üçün ekoloji təmiz istirahət yeri": "Экологически чистое место отдыха для семей",
    "WiFi, pulsuz parkinq, tam avadanlıqlı mətbəx, bulaq suyu, möhtəşəm dağ mənzərələri": "WiFi, бесплатная парковка, полностью оборудованная кухня, родниковая вода, потрясающие горные пейзажи",
    "WhatsApp ilə bron!": "Бронирование через WhatsApp!",
    
    # Keywords
    "Quba dağ evi": "горный дом Куба",
    "Küsnet Qazma kəndi": "село Кюснет Казма",
    "ekoloji təmiz": "экологически чистый",
    "dağ evi kirayə": "аренда горного дома",
    "Azerbaycan dağ turizmi": "горный туризм в Азербайджане",
    "ailələr üçün istirahət": "отдых для семей",
    "bulaq suyu": "родниковая вода",
    "dağ mənzərələri": "горные пейзажи",
    "bron": "бронирование",
    "meşə": "лес",
    "təbiət": "природа",
    
    # OG Tags
    "Təbiətin Qoynunda Unudulmaz İstirahət": "Незабываемый отдых в объятиях природы",
    "Küsnet Qazma kəndində ekoloji təmiz dağ evi": "Экологически чистый горный дом в селе Кюснет Казма",
    "Çoxlu ağaclar, bulaq suyu, möhtəşəm mənzərələr": "Много деревьев, родниковая вода, потрясающие пейзажи",
    "Ailələr üçün ideal istirahət yeri": "Идеальное место отдыха для семей",
    
    # Twitter
    "Təbiətin Qoynunda İstirahət": "Отдых в объятиях природы",
    
    # Schema
    "Ekoloji Təmiz Dağ Evi Küsnet Qazma Kəndində": "Экологически чистый горный дом в селе Кюснет Казма",
    "Ailələr üçün ekoloji təmiz istirahət yeri - meşə, bulaq suyu, dağ mənzərələri": "Экологически чистое место отдыха для семей - лес, родниковая вода, горные пейзажи",
    "Qonaqlar üçün ekoloji təmiz dağ evi": "Экологически чистый горный дом для гостей",
    "Küsnet Qazma": "Кюснет Казма",
    "Quba rayonu": " район Куба",
    "Azərbaycan": "Азербайджан",
    "Pulsuz Wi-Fi": "Бесплатный Wi-Fi",
    "Pulsuz parkinq": "Бесплатная парковка",
    "Tam avadanlıqlı mətbəx": "Полностью оборудованная кухня",
    "Mərkəzi istilik": "Центральное отопление",
    "Çaya birbaşa çıxış": "Прямой выход к реке",
    "Qəlyanaltı sahəsi": "Зона для шашлыка",
    "Gəzinti yollar": "Пешеходные дорожки",
    "Qonaqlar": "Гости",
    
    # Navigation
    "Haqqımızda": "О нас",
    "Qalereya": "Галерея",
    "İmkanlar": "Удобства",
    "Turlar": "Туры",
    "Blog": "Блог",
    "Əlaqə": "Контакты",
    
    # Hero section
    "🏔️ Quba rayonu, Küsnet Qazma kəndi": "🏔️ Район Куба, село Кюснет Казма",
    "Quba Dağ Evi": "Горный дом Куба",
    "Təbiətin qoynunda unudulmaz istirahət": "Незабываемый отдых в объятиях природы",
    "Ailələr üçün": "Для семей",
    "🌿 Sakit və rahat, təhlükəsiz mühit": "🌿 Спокойная и комфортная, безопасная среда",
    "Bron et": "Забронировать",
    "Qalereya": "Галерея",
    
    # About section
    "🏡 Ailəvi istirahət üçün ideal yer": "🏡 Идеальное место для семейного отдыха",
    "Ekoloji təmiz ərazidə Küsnet Qazma kəndində yerləşir": "Расположен в экологически чистом районе села Кюснет Казма",
    "Bu ərazi təbiət gözəlliyi, ağacların sıxlığı və bulaq suları ilə seçilir": "Эта местность отличается красотой природы, густотой деревьев и родниковой водой",
    "Hava burada həqiqətən təmizdir, səs-küy yoxdur": "Здесь воздух действительно чист, нет шума",
    "Yalnız quşların cəh-cəhi və axar suların şırıltısı": "Только щебет птиц и журчание проточной воды",
    "✅ Ailələr üçün nəzərdə tutulub": "✅ Предназначено для семей",
    "Yalnız ailəli qonaqlar qəbul edilir": "Принимаются только семейные гости",
    "Səs-küylü əyləncə və spirtli içkilər qadağandır": "Шумные развлечения и алкоголь запрещены",
    "Bu, sakit, təhlükəsiz və rahat istirahət yeridir": "Это спокойное, безопасное и комфортное место для отдыха",
    "Ekoloji təmiz ərazi": "Экологически чистая территория",
    "Meşə ilə əhatə olunub": "Окружен лесом",
    "Bulaq suları": "Родниковые воды",
    "Dağ mənzərələri": "Горные пейзажи",
    
    # Gallery
    "Qalereya": "Галерея",
    "Quba evimizin gözəlliyini kəşf edin": "Откройте для себя красоту нашего дома в Кубе",
    
    # Amenities section
    "✨ Evimizin imkanları": "✨ Удобства нашего дома",
    "Rahat istirahət üçün hər şey": "Всё для комфортного отдыха",
    "Wi-Fi": "Wi-Fi",
    "Pulsuz parkinq": "Бесплатная парковка",
    "Tam avadanlıqlı mətbəx": "Полностью оборудованная кухня",
    "Mərkəzi istilik": "Центральное отопление",
    "Qəlyanaltı sahəsi": "Зона для шашлыка",
    "Çaya birbaşa çıxış": "Прямой выход к реке",
    "Gəzinti yolları": "Пешеходные дорожки",
    "Kamin": "Камин",
    
    # Location section
    "📍 Məkan": "📍 Местоположение",
    "Quba rayonu, Küsnet Qazma kəndi, Azərbaycan": "Село Кюснет Казма, район Куба, Азербайджан",
    "Bakıdan məsafə": "Расстояние от Баку",
    "Quba mərkəzindən məsafə": "Расстояние от центра Куба",
    "Dəniz səviyyəsindən hündürlük": "Высота над уровнем моря",
    "Xəritədə bax": "Посмотреть на карте",
    
    # Contact section
    "📞 Bizimlə əlaqə": "📞 Свяжитесь с нами",
    "Hər hansı bir sualınız varsa və ya rezervasiya etmək istəyirsinizsə, bizimlə əlaqə saxlayın": "Если у вас есть вопросы или вы хотите забронировать, свяжитесь с нами",
    "Nömrə": "Номер",
    "Ünvan": "Адрес",
    "E-poçt": "Email",
    "Mesaj göndərin": "Отправить сообщение",
    "Ad və soyad": "Имя и фамилия",
    "E-poçt ünvanı": "Email адрес",
    "Mesaj": "Сообщение",
    "Göndər": "Отправить",
    
    # Footer
    "Quba": "Куба",
    "Ailəvi istirahət üçün sakit, rahat yer": "Спокойное, комфортное место для семейного отдыха",
    "Səhifələr": "Страницы",
    "Haqqımızda": "О нас",
    "Qalereya": "Галерея",
    "İmkanlar": "Удобства",
    "Əlaqə": "Контакты",
    "© 2024 Quba Cottage": "© 2024 Горный дом Куба",
    "Bütün hüquqlar qorunur": "Все права защищены",
    "Quba Cottage": "Горный дом Куба",
    
    # Booking widget
    "Quba Dağ Evi Bron": "Бронирование горного дома Куба",
    "Ailələr üçün ideal!": "Идеально для семей!",
    "Giriş": "Заезд",
    "Çıxış": "Выезд",
    "Qonaq sayı": "Количество гостей",
    "Ad": "Имя",
    "Seçin": "Выберите",
    "1 qonaq": "1 гость",
    "2 qonaq": "2 гостя",
    "3 qonaq": "3 гостя",
    "4 qonaq": "4 гостя",
    "5 qonaq": "5 гостей",
    "6+ qonaq": "6+ гостей",
    "WhatsApp ilə sürətli bron": "Быстрое бронирование через WhatsApp",
    
    # WhatsApp popup
    "Bizimlə əlaqə saxlayın! 📱": "Свяжитесь с нами! 📱",
    "WhatsApp ilə bron 💬": "Бронирование через WhatsApp 💬",
    
    # Alerts
    "Zəhmət olmasa bütün sahələri doldurun!": "Пожалуйста, заполните все поля!",
    "Qeyd edilməyib": "Не указано",
    
    # Booking message
    "Quba Dağ Evi Bron": "Бронирование горного дома Куба",
    "Giriş": "Заезд",
    "Çıxış": "Выезд",
    "Qonaq sayı": "Количество гостей",
    "nəfər": "гостей",
    "Ad": "Имя",
    "Telefon": "Телефон",
    "Qeydlər": "Примечания",
    "Bu mesaj veb-saytdan göndərilib": "Это сообщение отправлено с сайта",
    
    # Owner caption
    "Nəriman - Ev Sahibi": "Нераман - Владелец",
}

def translate_content(html_content):
    """Translate Azerbaijani content to Russian while keeping HTML structure"""
    
    # Sort translations by length (longest first) to avoid partial replacements
    sorted_translations = sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)
    
    translated_html = html_content
    
    # Replace all translations
    for az_text, ru_text in sorted_translations:
        # Use word boundaries to avoid partial matches
        # But be careful with HTML attributes
        if az_text in translated_html:
            translated_html = translated_html.replace(az_text, ru_text)
    
    # Fix specific patterns that might be broken
    
    # Fix language switcher - keep language codes
    translated_html = re.sub(r'href="/az/"', 'href="/"', translated_html)
    translated_html = re.sub(r'data-lang=az', 'data-lang=ru', translated_html)
    translated_html = re.sub(r'>AZ<', '>RU<', translated_html)
    translated_html = re.sub(r'>RU<', '>RU<', translated_html)  # Already correct
    translated_html = re.sub(r'>EN<', '>EN<', translated_html)
    translated_html = re.sub(r'>العربي<', '>عربي<', translated_html)
    translated_html = re.sub(r'class=lang-btn data-lang=ru>RU<', 'class="lang-btn active" data-lang=ru>RU<', translated_html)
    
    # Fix hreflang
    translated_html = re.sub(r'hreflang=az', 'hreflang=ru', translated_html)
    translated_html = re.sub(r'og:locale content=az_AZ', 'og:locale content=ru_RU', translated_html)
    translated_html = re.sub(r'yandex-language content=az', 'yandex-language content=ru', translated_html)
    
    # Fix language content tag
    translated_html = re.sub(r'<meta name=language content=az>', '<meta name=language content=ru>', translated_html)
    
    # Fix canonical URL
    translated_html = re.sub(r'link rel=canonical href=https://quba.rent/', 'link rel=canonical href=https://quba.rent/ru/', translated_html)
    translated_html = re.sub(r'og:url content=https://quba.rent/az/', 'og:url content=https://quba.rent/ru/', translated_html)
    
    # Fix alternate links
    translated_html = re.sub(r'href=/az/ class=lang-btn', 'href=/ class=lang-btn', translated_html)
    translated_html = re.sub(r'href=/ru/ class=lang-btn', 'href=/ru/ class="lang-btn active"', translated_html)
    
    # Fix title
    translated_html = re.sub(r'<title>Quba Dağ Evi', '<title>Горный дом Куба', translated_html)
    
    return translated_html

def create_russian_version():
    """Create Russian HTML file from Azerbaijani version"""
    
    # Read Azerbaijani version
    with open('/workspace/quba.rent/az_live.html', 'r', encoding='utf-8') as f:
        az_content = f.read()
    
    # Translate to Russian
    ru_content = translate_content(az_content)
    
    # Save Russian version
    with open('/workspace/quba.rent/index-ru.html', 'w', encoding='utf-8') as f:
        f.write(ru_content)
    
    print("✅ Russian version created: /workspace/quba.rent/index-ru.html")
    return ru_content

def upload_to_server():
    """Upload Russian version to server"""
    FTP_HOST = '95.216.232.219'
    FTP_PORT = 19121
    FTP_USER = 'www-data'
    FTP_PASSWORD = '0R6dXU1YnwSEl1OnURos'
    
    try:
        with ftplib.FTP() as ftp:
            ftp.connect(FTP_HOST, FTP_PORT)
            ftp.login(FTP_USER, FTP_PASSWORD)
            print(f"Connected to {FTP_HOST}:{FTP_PORT}")
            
            # Upload file
            with open('/workspace/quba.rent/index-ru.html', 'rb') as f:
                ftp.storbinary('STOR index-ru.html', f)
            
            print("✅ Successfully uploaded index-ru.html to server!")
            
    except Exception as e:
        print(f"❌ Error uploading: {e}")

if __name__ == '__main__':
    create_russian_version()
    upload_to_server()

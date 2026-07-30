from textwrap import dedent

# Navigation labels for each supported language.
NAV = {
    'en': {
        'home': 'Home',
        'problems': 'Possible issues',
        'artix': 'Artix Linux',
        'brand': 'Artix Installer',
    },
    'uk': {
        'home': 'Головна',
        'problems': 'Можливі проблеми',
        'artix': 'Artix Linux',
        'brand': 'Artix Installer',
    },
    'ru': {
        'home': 'Главная',
        'problems': 'Возможные проблемы',
        'artix': 'Artix Linux',
        'brand': 'Artix Installer',
    },
    'pl': {
        'home': 'Strona główna',
        'problems': 'Możliwe problemy',
        'artix': 'Artix Linux',
        'brand': 'Artix Installer',
    },
    'fr': {
        'home': 'Accueil',
        'problems': 'Problèmes possibles',
        'artix': 'Artix Linux',
        'brand': 'Artix Installer',
    },
    'it': {
        'home': 'Home',
        'problems': 'Possibili problemi',
        'artix': 'Artix Linux',
        'brand': 'Artix Installer',
    },
    'de': {
        'home': 'Startseite',
        'problems': 'Mögliche Probleme',
        'artix': 'Artix Linux',
        'brand': 'Artix Installer',
    },
}

LANGUAGES = {
    'en': 'English',
    'uk': 'Українська',
    'ru': 'Русский',
    'pl': 'Polski',
    'fr': 'Français',
    'it': 'Italiano',
    'de': 'Deutsch',
}

LANGUAGE_FLAGS = {
    'en': '🇬🇧',
    'uk': '🇺🇦',
    'ru': '🇷🇺',
    'pl': '🇵🇱',
    'fr': '🇫🇷',
    'it': '🇮🇹',
    'de': '🇩🇪',
}

# Page content for each supported language.
CONTENT = {
    "index": {
        "en": {
            "title": 'Artix Installer — Home',
            "body": dedent("""\
<h1>Artix Linux Installer</h1>

<p>
    This is a bash script that automatically installs
    <a href="/artix">Artix Linux</a>
    with the KDE Plasma desktop (Wayland), the PipeWire sound server,
    the NetworkManager network manager, and the GRUB bootloader.
</p>

<div class="warning">
    <strong>Important:</strong> the script completely erases the selected disk.
    Use it only on a test computer or in a virtual machine while experimenting.
</div>

<h2>What this script is for</h2>

<ul>
    <li>Automatically detects the CPU and GPU.</li>
    <li>Automatically chooses disk partitioning for UEFI or BIOS.</li>
    <li>Installs the correct drivers (Intel, AMD, NVIDIA, hybrid configurations).</li>
    <li>Configures locale, timezone, user account, and bootloader.</li>
    <li>Prepares KDE Plasma for Wayland.</li>
</ul>

<h2>What will be installed</h2>

<table>
    <tr><td><strong>Init system</strong></td><td>OpenRC + elogind</td></tr>
    <tr><td><strong>Kernel</strong></td><td>linux, linux-firmware, linux-headers</td></tr>
    <tr><td><strong>Desktop</strong></td><td>KDE Plasma (minimal set, Wayland)</td></tr>
    <tr><td><strong>Sound</strong></td><td>PipeWire + WirePlumber</td></tr>
    <tr><td><strong>Network</strong></td><td>NetworkManager</td></tr>
    <tr><td><strong>Bootloader</strong></td><td>GRUB (UEFI/BIOS)</td></tr>
    <tr><td><strong>Extras</strong></td><td>BlueZ, chrony, basic utilities and fonts</td></tr>
</table>

<h2>Requirements</h2>

<ul>
    <li>Boot from the official Artix Linux live ISO.</li>
    <li>Internet access.</li>
    <li>Root privileges (run with <code>sudo</code>).</li>
    <li>The target disk will be completely wiped.</li>
</ul>

<h2>How to use</h2>

<ol>
    <li>Boot from the Artix Linux live ISO.</li>
    <li>Connect to the internet.</li>
    <li>Copy or clone the script.</li>
    <li>Enter the <code>script/</code> directory.</li>
    <li>Make the script executable and run it:</li>
</ol>

<pre><code>chmod +x artix-installer.sh
sudo ./artix-installer.sh</code></pre>

<p>The script will ask a few questions:</p>

<ul>
    <li>Which disk to use.</li>
    <li>Hostname, username, timezone.</li>
    <li>Root and user passwords.</li>
    <li>During installation it may ask you to choose a package provider — follow the recommended hints.</li>
</ul>

<h2>Dry-run mode</h2>

<p>
    If you want to see what the script is going to do without changing the disk,
    use the <code>--dry-run</code> flag:
</p>

<pre><code>./artix-installer.sh --dry-run</code></pre>

<p>
    In this mode no real partitioning, formatting, or installation commands are
    executed — they are only printed to the screen.
</p>

<h2>After installation</h2>

<ol>
    <li>Remove the installation medium.</li>
    <li>Reboot.</li>
    <li>At the SDDM login screen choose the <strong>Plasma (Wayland)</strong> session.</li>
    <li>Log in with the created user.</li>
</ol>

<p>
    If you want to know what issues may occur in advance, visit the
    <a href="/problems">Possible issues</a> page.
</p>
""").strip(),
        },
        "uk": {
            "title": 'Artix Installer — головна',
            "body": dedent("""\
<h1>Встановлювач Artix Linux</h1>

<p>
    Це bash-скрипт, який автоматично встановлює
    <a href="/artix">Artix Linux</a>
    із робочим столом KDE Plasma (Wayland), звуковим сервером PipeWire,
    мережевим менеджером NetworkManager і завантажувачем GRUB.
</p>

<div class="warning">
    <strong>Важливо:</strong> скрипт повністю стирає вибраний диск.
    Використовуйте його лише на тестовому комп’ютері або у віртуальній машині,
    якщо експериментуєте.
</div>

<h2>Для чого потрібен цей скрипт</h2>

<ul>
    <li>Автоматично визначає процесор і відеокарту.</li>
    <li>Автоматично обирає розмітку диска під UEFI або BIOS.</li>
    <li>Сам встановлює потрібні драйвери (Intel, AMD, NVIDIA, гібридні конфігурації).</li>
    <li>Налаштовує локаль, часовий пояс, користувача і завантажувач.</li>
    <li>Готує KDE Plasma до роботи в Wayland.</li>
</ul>

<h2>Що буде встановлено</h2>

<table>
    <tr><td><strong>Система ініціалізації</strong></td><td>OpenRC + elogind</td></tr>
    <tr><td><strong>Ядро</strong></td><td>linux, linux-firmware, linux-headers</td></tr>
    <tr><td><strong>Робочий стіл</strong></td><td>KDE Plasma (мінімальний набір, Wayland)</td></tr>
    <tr><td><strong>Звук</strong></td><td>PipeWire + WirePlumber</td></tr>
    <tr><td><strong>Мережа</strong></td><td>NetworkManager</td></tr>
    <tr><td><strong>Завантажувач</strong></td><td>GRUB (UEFI/BIOS)</td></tr>
    <tr><td><strong>Додатково</strong></td><td>BlueZ, chrony, базові утиліти і шрифти</td></tr>
</table>

<h2>Вимоги</h2>

<ul>
    <li>Завантаження з офіційного live-образу Artix Linux.</li>
    <li>Доступ до інтернету.</li>
    <li>Права root (скрипт запускається через <code>sudo</code>).</li>
    <li>Цільовий диск буде повністю очищено.</li>
</ul>

<h2>Як використовувати</h2>

<ol>
    <li>Завантажтеся з Artix Linux live ISO.</li>
    <li>Підключіться до інтернету.</li>
    <li>Скопіюйте або клонуйте скрипт.</li>
    <li>Перейдіть у папку <code>script/</code>.</li>
    <li>Зробіть скрипт виконуваним і запустіть його:</li>
</ol>

<pre><code>chmod +x artix-installer.sh
sudo ./artix-installer.sh</code></pre>

<p>Скрипт поставить кілька запитань:</p>

<ul>
    <li>Який диск використовувати.</li>
    <li>Hostname, ім’я користувача, часовий пояс.</li>
    <li>Паролі root і користувача.</li>
    <li>Під час встановлення може запитати вибір провайдера пакета — обирайте рекомендовані підказки.</li>
</ul>

<h2>Режим пробного запуску</h2>

<p>
    Якщо хочете подивитися, що скрипт збирається робити, не змінюючи диск,
    використовуйте прапор <code>--dry-run</code>:
</p>

<pre><code>./artix-installer.sh --dry-run</code></pre>

<p>
    У цьому режимі не виконуються реальні команди розмітки, форматування
    і встановлення — лише виводяться на екран.
</p>

<h2>Після встановлення</h2>

<ol>
    <li>Вийміть установчий носій.</li>
    <li>Перезавантажтеся.</li>
    <li>На екрані входу SDDM оберіть сесію <strong>Plasma (Wayland)</strong>.</li>
    <li>Увійдіть під створеним користувачем.</li>
</ol>

<p>
    Якщо хочете заздалегідь дізнатися, які складнощі можуть виникнути,
    перейдіть на сторінку
    <a href="/problems">«Можливі проблеми»</a>.
</p>
""").strip(),
        },
        "ru": {
            "title": 'Artix Installer — главная',
            "body": dedent("""\
<h1>Установщик Artix Linux</h1>

<p>
    Это bash-скрипт, который автоматически устанавливает
    <a href="/artix">Artix Linux</a>
    с рабочим столом KDE Plasma (Wayland), звуковым сервером PipeWire,
    менеджером сети NetworkManager и загрузчиком GRUB.
</p>

<div class="warning">
    <strong>Важно:</strong> скрипт стирает выбранный диск полностью.
    Используйте его только на тестовом компьютере или в виртуальной машине,
    если экспериментируете.
</div>

<h2>Для чего нужен этот скрипт</h2>

<ul>
    <li>Автоматически определяет процессор и видеокарту.</li>
    <li>Автоматически выбирает разметку диска под UEFI или BIOS.</li>
    <li>Сам устанавливает нужные драйверы (Intel, AMD, NVIDIA, гибридные конфигурации).</li>
    <li>Настраивает локаль, часовой пояс, пользователя и загрузчик.</li>
    <li>Подготавливает KDE Plasma к работе в Wayland.</li>
</ul>

<h2>Что будет установлено</h2>

<table>
    <tr><td><strong>Система инициализации</strong></td><td>OpenRC + elogind</td></tr>
    <tr><td><strong>Ядро</strong></td><td>linux, linux-firmware, linux-headers</td></tr>
    <tr><td><strong>Рабочий стол</strong></td><td>KDE Plasma (минимальный набор, Wayland)</td></tr>
    <tr><td><strong>Звук</strong></td><td>PipeWire + WirePlumber</td></tr>
    <tr><td><strong>Сеть</strong></td><td>NetworkManager</td></tr>
    <tr><td><strong>Загрузчик</strong></td><td>GRUB (UEFI/BIOS)</td></tr>
    <tr><td><strong>Дополнительно</strong></td><td>BlueZ, chrony, базовые утилиты и шрифты</td></tr>
</table>

<h2>Требования</h2>

<ul>
    <li>Загрузка с официального live-образа Artix Linux.</li>
    <li>Доступ в интернет.</li>
    <li>Права root (скрипт запускается через <code>sudo</code>).</li>
    <li>Целевой диск будет полностью очищен.</li>
</ul>

<h2>Как использовать</h2>

<ol>
    <li>Загрузитесь с Artix Linux live ISO.</li>
    <li>Подключитесь к интернету.</li>
    <li>Скопируйте или клонируйте скрипт.</li>
    <li>Перейдите в папку <code>script/</code>.</li>
    <li>Сделайте скрипт исполняемым и запустите его:</li>
</ol>

<pre><code>chmod +x artix-installer.sh
sudo ./artix-installer.sh</code></pre>

<p>Скрипт задаст несколько вопросов:</p>

<ul>
    <li>Какой диск использовать.</li>
    <li>Hostname, имя пользователя, часовой пояс.</li>
    <li>Пароли root и пользователя.</li>
    <li>Во время установки может спросить выбор провайдера пакета — выбирайте рекомендуемые подсказки.</li>
</ul>

<h2>Режим пробного запуска</h2>

<p>
    Если хотите посмотреть, что скрипт собирается делать, не изменяя диск,
    используйте флаг <code>--dry-run</code>:
</p>

<pre><code>./artix-installer.sh --dry-run</code></pre>

<p>
    В этом режиме не выполняются реальные команды разметки, форматирования
    и установки — только печатаются на экран.
</p>

<h2>После установки</h2>

<ol>
    <li>Извлеките установочный носитель.</li>
    <li>Перезагрузитесь.</li>
    <li>В экране входа SDDM выберите сессию <strong>Plasma (Wayland)</strong>.</li>
    <li>Войдите под созданным пользователем.</li>
</ol>

<p>
    Если хотите заранее узнать, какие сложности могут возникнуть,
    перейдите на страницу
    <a href="/problems">«Возможные проблемы»</a>.
</p>
""").strip(),
        },
        "pl": {
            "title": 'Artix Installer — strona główna',
            "body": dedent("""\
<h1>Instalator Artix Linux</h1>

<p>
    To skrypt bash, który automatycznie instaluje
    <a href="/artix">Artix Linux</a>
    z pulpitem KDE Plasma (Wayland), serwerem dźwięku PipeWire,
    menedżerem sieci NetworkManager oraz bootloaderem GRUB.
</p>

<div class="warning">
    <strong>Ważne:</strong> skrypt całkowicie usuwa wybrany dysk.
    Używaj go tylko na komputerze testowym lub w maszynie wirtualnej,
    jeśli eksperymentujesz.
</div>

<h2>Do czego służy ten skrypt</h2>

<ul>
    <li>Automatycznie wykrywa procesor i kartę graficzną.</li>
    <li>Automatycznie wybiera partycjonowanie dysku pod UEFI lub BIOS.</li>
    <li>Sam instaluje odpowiednie sterowniki (Intel, AMD, NVIDIA, konfiguracje hybrydowe).</li>
    <li>Konfiguruje ustawienia regionalne, strefę czasową, użytkownika i bootloader.</li>
    <li>Przygotowuje KDE Plasma do pracy w Wayland.</li>
</ul>

<h2>Co zostanie zainstalowane</h2>

<table>
    <tr><td><strong>System init</strong></td><td>OpenRC + elogind</td></tr>
    <tr><td><strong>Jądro</strong></td><td>linux, linux-firmware, linux-headers</td></tr>
    <tr><td><strong>Pulpit</strong></td><td>KDE Plasma (minimalny zestaw, Wayland)</td></tr>
    <tr><td><strong>Dźwięk</strong></td><td>PipeWire + WirePlumber</td></tr>
    <tr><td><strong>Sieć</strong></td><td>NetworkManager</td></tr>
    <tr><td><strong>Bootloader</strong></td><td>GRUB (UEFI/BIOS)</td></tr>
    <tr><td><strong>Dodatkowo</strong></td><td>BlueZ, chrony, podstawowe narzędzia i czcionki</td></tr>
</table>

<h2>Wymagania</h2>

<ul>
    <li>Uruchomienie z oficjalnego obrazu live Artix Linux.</li>
    <li>Dostęp do internetu.</li>
    <li>Uprawnienia root (skrypt uruchamiany przez <code>sudo</code>).</li>
    <li>Dysk docelowy zostanie całkowicie wyczyszczony.</li>
</ul>

<h2>Jak używać</h2>

<ol>
    <li>Uruchom komputer z obrazu live Artix Linux ISO.</li>
    <li>Połącz się z internetem.</li>
    <li>Skopiuj lub sklonuj skrypt.</li>
    <li>Wejdź do katalogu <code>script/</code>.</li>
    <li>Ustaw skrypt jako wykonywalny i uruchom go:</li>
</ol>

<pre><code>chmod +x artix-installer.sh
sudo ./artix-installer.sh</code></pre>

<p>Skrypt zada kilka pytań:</p>

<ul>
    <li>Którego dysku użyć.</li>
    <li>Hostname, nazwa użytkownika, strefa czasowa.</li>
    <li>Hasła root i użytkownika.</li>
    <li>Podczas instalacji może zapytać o wyboru dostawcy pakietu — wybieraj zalecane podpowiedzi.</li>
</ul>

<h2>Tryb próbny</h2>

<p>
    Jeśli chcesz zobaczyć, co skrypt zamierza zrobić, nie zmieniając dysku,
    użyj flagi <code>--dry-run</code>:
</p>

<pre><code>./artix-installer.sh --dry-run</code></pre>

<p>
    W tym trybie nie są wykonywane rzeczywiste polecenia partycjonowania,
    formatowania i instalacji — są tylko wyświetlane na ekranie.
</p>

<h2>Po instalacji</h2>

<ol>
    <li>Wyjmij nośnik instalacyjny.</li>
    <li>Zrestartuj komputer.</li>
    <li>W ekranie logowania SDDM wybierz sesję <strong>Plasma (Wayland)</strong>.</li>
    <li>Zaloguj się utworzonym użytkownikiem.</li>
</ol>

<p>
    Jeśli chcesz wcześniej wiedzieć, jakie problemy mogą wystąpić,
    przejdź na stronę
    <a href="/problems">„Możliwe problemy”</a>.
</p>
""").strip(),
        },
        "fr": {
            "title": 'Artix Installer — Accueil',
            "body": dedent("""\
<h1>Installateur Artix Linux</h1>

<p>
    C'est un script bash qui installe automatiquement
    <a href="/artix">Artix Linux</a>
    avec le bureau KDE Plasma (Wayland), le serveur audio PipeWire,
    le gestionnaire de réseau NetworkManager et le chargeur de démarrage GRUB.
</p>

<div class="warning">
    <strong>Important :</strong> le script efface complètement le disque sélectionné.
    Utilisez-le uniquement sur un ordinateur de test ou dans une machine virtuelle
    si vous faites des expérimentations.
</div>

<h2>À quoi sert ce script</h2>

<ul>
    <li>Détecte automatiquement le processeur et la carte graphique.</li>
    <li>Choisit automatiquement le partitionnement du disque pour UEFI ou BIOS.</li>
    <li>Installe les bons pilotes (Intel, AMD, NVIDIA, configurations hybrides).</li>
    <li>Configure la locale, le fuseau horaire, l'utilisateur et le chargeur de démarrage.</li>
    <li>Prépare KDE Plasma pour Wayland.</li>
</ul>

<h2>Ce qui sera installé</h2>

<table>
    <tr><td><strong>Système d'initialisation</strong></td><td>OpenRC + elogind</td></tr>
    <tr><td><strong>Noyau</strong></td><td>linux, linux-firmware, linux-headers</td></tr>
    <tr><td><strong>Bureau</strong></td><td>KDE Plasma (ensemble minimal, Wayland)</td></tr>
    <tr><td><strong>Audio</strong></td><td>PipeWire + WirePlumber</td></tr>
    <tr><td><strong>Réseau</strong></td><td>NetworkManager</td></tr>
    <tr><td><strong>Chargeur de démarrage</strong></td><td>GRUB (UEFI/BIOS)</td></tr>
    <tr><td><strong>Suppléments</strong></td><td>BlueZ, chrony, utilitaires de base et polices</td></tr>
</table>

<h2>Prérequis</h2>

<ul>
    <li>Démarrage depuis l'image live officielle d'Artix Linux.</li>
    <li>Accès à Internet.</li>
    <li>Droits root (le script s'exécute avec <code>sudo</code>).</li>
    <li>Le disque cible sera complètement effacé.</li>
</ul>

<h2>Comment utiliser</h2>

<ol>
    <li>Démarrez depuis l'ISO live d'Artix Linux.</li>
    <li>Connectez-vous à Internet.</li>
    <li>Copiez ou clonez le script.</li>
    <li>Entrez dans le répertoire <code>script/</code>.</li>
    <li>Rendez le script exécutable et lancez-le :</li>
</ol>

<pre><code>chmod +x artix-installer.sh
sudo ./artix-installer.sh</code></pre>

<p>Le script posera quelques questions :</p>

<ul>
    <li>Quel disque utiliser.</li>
    <li>Nom d'hôte, nom d'utilisateur, fuseau horaire.</li>
    <li>Mots de passe root et utilisateur.</li>
    <li>Pendant l'installation, il peut demander de choisir un fournisseur de paquet — suivez les suggestions recommandées.</li>
</ul>

<h2>Mode simulation</h2>

<p>
    Si vous voulez voir ce que le script va faire sans modifier le disque,
    utilisez le flag <code>--dry-run</code> :
</p>

<pre><code>./artix-installer.sh --dry-run</code></pre>

<p>
    Dans ce mode, aucune commande réelle de partitionnement, de formatage
    ou d'installation n'est exécutée — elles sont seulement affichées à l'écran.
</p>

<h2>Après l'installation</h2>

<ol>
    <li>Retirez le support d'installation.</li>
    <li>Redémarrez.</li>
    <li>À l'écran de connexion SDDM, choisissez la session <strong>Plasma (Wayland)</strong>.</li>
    <li>Connectez-vous avec l'utilisateur créé.</li>
</ol>

<p>
    Si vous voulez savoir à l'avance quelles difficultés peuvent survenir,
    consultez la page
    <a href="/problems">« Problèmes possibles »</a>.
</p>
""").strip(),
        },
        "it": {
            "title": 'Artix Installer — Home',
            "body": dedent("""\
<h1>Installatore Artix Linux</h1>

<p>
    Questo è uno script bash che installa automaticamente
    <a href="/artix">Artix Linux</a>
    con il desktop KDE Plasma (Wayland), il server audio PipeWire,
    il gestore di rete NetworkManager e il bootloader GRUB.
</p>

<div class="warning">
    <strong>Importante:</strong> lo script cancella completamente il disco selezionato.
    Usalo solo su un computer di test o in una macchina virtuale
    se stai sperimentando.
</div>

<h2>A cosa serve questo script</h2>

<ul>
    <li>Rileva automaticamente CPU e GPU.</li>
    <li>Sceglie automaticamente il partizionamento del disco per UEFI o BIOS.</li>
    <li>Installa automaticamente i driver corretti (Intel, AMD, NVIDIA, configurazioni ibride).</li>
    <li>Configura la locale, il fuso orario, l'utente e il bootloader.</li>
    <li>Prepara KDE Plasma per Wayland.</li>
</ul>

<h2>Cosa verrà installato</h2>

<table>
    <tr><td><strong>Sistema init</strong></td><td>OpenRC + elogind</td></tr>
    <tr><td><strong>Kernel</strong></td><td>linux, linux-firmware, linux-headers</td></tr>
    <tr><td><strong>Desktop</strong></td><td>KDE Plasma (insieme minimo, Wayland)</td></tr>
    <tr><td><strong>Audio</strong></td><td>PipeWire + WirePlumber</td></tr>
    <tr><td><strong>Rete</strong></td><td>NetworkManager</td></tr>
    <tr><td><strong>Bootloader</strong></td><td>GRUB (UEFI/BIOS)</td></tr>
    <tr><td><strong>Extra</strong></td><td>BlueZ, chrony, utilità di base e font</td></tr>
</table>

<h2>Requisiti</h2>

<ul>
    <li>Avvio dall'immagine live ufficiale di Artix Linux.</li>
    <li>Accesso a Internet.</li>
    <li>Privilegi root (lo script si avvia con <code>sudo</code>).</li>
    <li>Il disco di destinazione verrà completamente cancellato.</li>
</ul>

<h2>Come usare</h2>

<ol>
    <li>Avvia dal live ISO di Artix Linux.</li>
    <li>Connettiti a Internet.</li>
    <li>Copia o clona lo script.</li>
    <li>Entra nella cartella <code>script/</code>.</li>
    <li>Rendi lo script eseguibile e avvialo:</li>
</ol>

<pre><code>chmod +x artix-installer.sh
sudo ./artix-installer.sh</code></pre>

<p>Lo script farà alcune domande:</p>

<ul>
    <li>Quale disco utilizzare.</li>
    <li>Hostname, nome utente, fuso orario.</li>
    <li>Password di root e dell'utente.</li>
    <li>Durante l'installazione potrebbe chiedere di scegliere un provider di pacchetti — segui i suggerimenti consigliati.</li>
</ul>

<h2>Modalità di simulazione</h2>

<p>
    Se vuoi vedere cosa farà lo script senza modificare il disco,
    usa il flag <code>--dry-run</code>:
</p>

<pre><code>./artix-installer.sh --dry-run</code></pre>

<p>
    In questa modalità non vengono eseguiti comandi reali di partizionamento,
    formattazione o installazione — vengono solo stampati a schermo.
</p>

<h2>Dopo l'installazione</h2>

<ol>
    <li>Rimuovi il supporto di installazione.</li>
    <li>Riavvia.</li>
    <li>Nella schermata di accesso SDDM scegli la sessione <strong>Plasma (Wayland)</strong>.</li>
    <li>Accedi con l'utente creato.</li>
</ol>

<p>
    Se vuoi sapere in anticipo quali difficoltà potrebbero sorgere,
    visita la pagina
    <a href="/problems">«Possibili problemi»</a>.
</p>
""").strip(),
        },
        "de": {
            "title": 'Artix Installer — Startseite',
            "body": dedent("""\
<h1>Artix Linux Installationsassistent</h1>

<p>
    Dies ist ein Bash-Skript, das
    <a href="/artix">Artix Linux</a>
    automatisch mit dem KDE Plasma Desktop (Wayland), dem PipeWire-Soundserver,
    dem Netzwerkmanager NetworkManager und dem Bootloader GRUB installiert.
</p>

<div class="warning">
    <strong>Wichtig:</strong> das Skript löscht die ausgewählte Festplatte vollständig.
    Verwenden Sie es nur auf einem Testcomputer oder in einer virtuellen Maschine,
    wenn Sie experimentieren.
</div>

<h2>Wozu dient dieses Skript</h2>

<ul>
    <li>Erkennt CPU und GPU automatisch.</li>
    <li>Wählt automatisch die Partitionierung für UEFI oder BIOS.</li>
    <li>Installiert die richtigen Treiber (Intel, AMD, NVIDIA, hybride Konfigurationen).</li>
    <li>Konfiguriert Locale, Zeitzone, Benutzer und Bootloader.</li>
    <li>Bereitet KDE Plasma für Wayland vor.</li>
</ul>

<h2>Was installiert wird</h2>

<table>
    <tr>
        <td><strong>Init-System</strong></td>
        <td>OpenRC + elogind</td>
    </tr>
    <tr>
        <td><strong>Kernel</strong></td>
        <td>linux, linux-firmware, linux-headers</td>
    </tr>
    <tr>
        <td><strong>Desktop</strong></td>
        <td>KDE Plasma (minimales Set, Wayland)</td>
    </tr>
    <tr>
        <td><strong>Audio</strong></td>
        <td>PipeWire + WirePlumber</td>
    </tr>
    <tr>
        <td><strong>Netzwerk</strong></td>
        <td>NetworkManager</td>
    </tr>
    <tr>
        <td><strong>Bootloader</strong></td>
        <td>GRUB (UEFI/BIOS)</td>
    </tr>
    <tr>
        <td><strong>Extras</strong></td>
        <td>BlueZ, chrony, grundlegende Dienstprogramme und Schriftarten</td>
    </tr>
</table>

<h2>Voraussetzungen</h2>

<ul>
    <li>Starten vom offiziellen Artix Linux Live-Image.</li>
    <li>Internetzugang.</li>
    <li>Root-Rechte (das Skript wird mit <code>sudo</code> ausgeführt).</li>
    <li>Die Zielfestplatte wird vollständig gelöscht.</li>
</ul>

<h2>Verwendung</h2>

<ol>
    <li>Starten Sie von der Artix Linux Live-ISO.</li>
    <li>Stellen Sie eine Internetverbindung her.</li>
    <li>Kopieren oder klonen Sie das Skript.</li>
    <li>Wechseln Sie in das Verzeichnis <code>script/</code>.</li>
    <li>Machen Sie das Skript ausführbar und starten Sie es:</li>
</ol>

<pre><code>chmod +x artix-installer.sh
sudo ./artix-installer.sh</code></pre>

<p>Das Skript wird einige Fragen stellen:</p>

<ul>
    <li>Welche Festplatte verwendet werden soll.</li>
    <li>Hostname, Benutzername, Zeitzone.</li>
    <li>Root- und Benutzerpasswörter.</li>
    <li>Während der Installation kann es nach einem Paketprovider fragen — folgen Sie den empfohlenen Hinweisen.</li>
</ul>

<h2>Trockenlauf-Modus</h2>

<p>
    Wenn Sie sehen möchten, was das Skript tun wird, ohne die Festplatte zu ändern,
    verwenden Sie das Flag <code>--dry-run</code>:
</p>

<pre><code>./artix-installer.sh --dry-run</code></pre>

<p>
    In diesem Modus werden keine echten Partitionierungs-, Formatierungs-
    oder Installationsbefehle ausgeführt — sie werden nur auf dem Bildschirm angezeigt.
</p>

<h2>Nach der Installation</h2>

<ol>
    <li>Entfernen Sie das Installationsmedium.</li>
    <li>Starten Sie neu.</li>
    <li>Wählen Sie im SDDM-Anmeldebildschirm die Sitzung <strong>Plasma (Wayland)</strong>.</li>
    <li>Melden Sie sich mit dem erstellten Benutzer an.</li>
</ol>

<p>
    Wenn Sie im Voraus wissen möchten, welche Probleme auftreten können,
    besuchen Sie die Seite
    <a href="/problems">„Mögliche Probleme“</a>.
</p>
""").strip(),
        },
    },
    "problems": {
        "en": {
            "title": 'Possible issues — Artix Installer',
            "body": dedent("""\
<h1>Possible issues and solutions</h1>

<p>
    Below are typical situations you may encounter when using the installer,
    along with ways to solve them.
</p>

<div class="problem">
    <h3>1. “Run this script as root”</h3>
    <p><strong>Cause:</strong> the installer must be run with superuser privileges.</p>
    <p><strong>Solution:</strong></p>
    <pre><code>sudo ./artix-installer.sh</code></pre>
</div>

<div class="problem">
    <h3>2. “No internet connection”</h3>
    <p><strong>Cause:</strong> <code>basestrap</code> needs the internet to install packages.</p>
    <p><strong>Solution:</strong> check connectivity:</p>
    <pre><code>ping -c 3 archlinux.org</code></pre>
    <p>If you are using Wi-Fi, connect via <code>iwctl</code> or <code>nmtui</code> before running the script.</p>
</div>

<div class="problem">
    <h3>3. The script erased the wrong disk</h3>
    <p><strong>Cause:</strong> the wrong disk was selected. The script does not check whether the disk is the live USB.
    </p>
    <p><strong>Solution:</strong></p>
    <ul>
        <li>Carefully check the disk model and size.</li>
        <li>Run <code>--dry-run</code> first to see which disk will be selected.</li>
        <li>In a virtual machine, detach extra disks.</li>
    </ul>
</div>

<div class="problem">
    <h3>4. “Disk is too small”</h3>
    <p><strong>Cause:</strong> the disk is smaller than required for EFI (512 MiB), swap, and a minimal root (5 GiB).
    </p>
    <p><strong>Solution:</strong> use a disk of at least 16–20 GiB. For comfortable KDE use, 40 GiB or more is
        recommended.</p>
</div>

<div class="problem">
    <h3>5. “Some partitions are currently mounted”</h3>
    <p><strong>Cause:</strong> some partitions on the selected disk are already mounted.</p>
    <p><strong>Solution:</strong> either choose another disk, or unmount the partitions manually:</p>
    <pre><code>sudo umount /dev/sdX1
sudo swapoff /dev/sdX2</code></pre>
</div>

<div class="problem">
    <h3>6. Errors from <code>parted</code>, <code>wipefs</code>, or <code>sgdisk</code></h3>
    <p><strong>Cause:</strong> the disk is in use or inaccessible.</p>
    <p><strong>Solution:</strong></p>
    <ul>
        <li>Make sure the disk is not mounted.</li>
        <li>If it is “busy”, try unmounting all its partitions.</li>
        <li>Use <code>lsblk</code> to find the process blocking the disk.</li>
    </ul>
</div>

<div class="problem">
    <h3>7. <code>basestrap</code> asks for a package provider</h3>
    <p><strong>Cause:</strong> several packages provide the same functionality.</p>
    <p><strong>Solution:</strong> choose the recommended options:</p>
    <ul>
        <li><code>iptables-nft</code> instead of legacy iptables.</li>
        <li><code>mkinitcpio</code> for creating initramfs.</li>
        <li><code>xorg-server</code> for Xorg.</li>
    </ul>
</div>

<div class="problem">
    <h3>8. <code>basestrap failed</code></h3>
    <p><strong>Cause:</strong> usually a network, mirror, or incorrect package name issue.</p>
    <p><strong>Solution:</strong></p>
    <ul>
        <li>Check your internet connection.</li>
        <li>Update the mirror list in live mode:</li>
    </ul>
    <pre><code>sudo reflector --country Ukraine --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist</code></pre>
</div>

<div class="problem">
    <h3>9. GPU was not detected</h3>
    <p><strong>Cause:</strong> <code>lspci</code> does not see the GPU or its output is not recognized.</p>
    <p><strong>Solution:</strong> install drivers manually after installation. For NVIDIA:</p>
    <pre><code>sudo pacman -S nvidia-dkms nvidia-utils nvidia-settings</code></pre>
    <p>For AMD:</p>
    <pre><code>sudo pacman -S mesa vulkan-radeon xf86-video-amdgpu</code></pre>
</div>

<div class="problem">
    <h3>10. NVIDIA issues in Wayland</h3>
    <p><strong>Cause:</strong> the proprietary NVIDIA driver requires extra parameters.</p>
    <p><strong>Solution:</strong> the script should add them automatically:</p>
    <ul>
        <li>Kernel parameter <code>nvidia-drm.modeset=1</code>.</li>
        <li>Modules <code>nvidia nvidia_modeset nvidia_uvm nvidia_drm</code> in <code>/etc/mkinitcpio.conf</code>.</li>
    </ul>
    <p>If this did not happen, add them manually and regenerate initramfs:</p>
    <pre><code>sudo mkinitcpio -P
sudo grub-mkconfig -o /boot/grub/grub.cfg</code></pre>
</div>

<div class="problem">
    <h3>11. PipeWire does not start / no sound</h3>
    <p><strong>Cause:</strong> OpenRC has no systemd user sessions, so PipeWire may not start automatically.</p>
    <p><strong>Solution:</strong> the script creates autostart entries for the user. If there is no sound, check:</p>
    <pre><code>pactl info
ps aux | grep pipewire</code></pre>
    <p>Start manually:</p>
    <pre><code>pipewire &amp;
wireplumber &amp;</code></pre>
</div>

<div class="problem">
    <h3>12. Bluetooth does not work</h3>
    <p><strong>Cause:</strong> the service may be named <code>bluetooth</code> instead of <code>bluetoothd</code> on
        some init variants.</p>
    <p><strong>Solution:</strong></p>
    <pre><code>sudo rc-update add bluetooth default
sudo rc-service bluetooth start</code></pre>
</div>

<div class="problem">
    <h3>13. Error while creating initramfs / GRUB</h3>
    <p><strong>Cause:</strong> inside the chroot some modules may not load, or <code>grub-install</code> may fail.</p>
    <p><strong>Solution:</strong> enter the chroot of the installed system from the live USB:</p>
    <pre><code>sudo artix-chroot /mnt
mkinitcpio -P
grub-mkconfig -o /boot/grub/grub.cfg
exit</code></pre>
</div>

<div class="problem">
    <h3>14. I want to test the script safely</h3>
    <p><strong>Solution:</strong> use the dry-run mode:</p>
    <pre><code>./artix-installer.sh --dry-run</code></pre>
    <p>It will not change any disks, but will show the entire action plan.</p>
</div>

<p>
    Return to the <a href="/">home page</a>
    or visit the <a href="/artix">Artix Linux</a> website.
</p>
""").strip(),
        },
        "uk": {
            "title": 'Можливі проблеми — Artix Installer',
            "body": dedent("""\
<h1>Можливі проблеми та їх вирішення</h1>

<p>
    Нижче зібрані типові ситуації, з якими можна зіткнутися під час роботи
    з встановлювачем, і способи їх вирішення.
</p>

<div class="problem">
    <h3>1. «Run this script as root»</h3>
    <p><strong>Причина:</strong> встановлювач має запускатися з правами суперкористувача.</p>
    <p><strong>Вирішення:</strong></p>
    <pre><code>sudo ./artix-installer.sh</code></pre>
</div>

<div class="problem">
    <h3>2. «No internet connection»</h3>
    <p><strong>Причина:</strong> для встановлення пакетів через <code>basestrap</code> потрібен інтернет.</p>
    <p><strong>Вирішення:</strong> перевірте підключення:</p>
    <pre><code>ping -c 3 archlinux.org</code></pre>
    <p>Якщо використовуєте Wi-Fi, підключіться через <code>iwctl</code> або <code>nmtui</code> до запуску скрипта.</p>
</div>

<div class="problem">
    <h3>3. Скрипт стер не той диск</h3>
    <p><strong>Причина:</strong> вибрано неправильний диск. Скрипт не перевіряє, чи є диск завантажувальним USB.</p>
    <p><strong>Вирішення:</strong></p>
    <ul>
        <li>Уважно дивіться на модель і розмір диска.</li>
        <li>Спочатку запустіть <code>--dry-run</code>, щоб побачити, який диск буде вибрано.</li>
        <li>У віртуальній машині відключіть зайві диски.</li>
    </ul>
</div>

<div class="problem">
    <h3>4. «Disk is too small»</h3>
    <p><strong>Причина:</strong> диск менший, ніж потрібно для EFI (512 МіБ), swap і мінімального root (5 ГіБ).</p>
    <p><strong>Вирішення:</strong> використовуйте диск об’ємом щонайменше 16–20 ГіБ. Для комфортної роботи з KDE рекомендується 40 ГіБ і більше.</p>
</div>

<div class="problem">
    <h3>5. «Some partitions are currently mounted»</h3>
    <p><strong>Причина:</strong> на вибраному диску вже змонтовано розділи.</p>
    <p><strong>Вирішення:</strong> або оберіть інший диск, або відмонтуйте розділи вручну:</p>
    <pre><code>sudo umount /dev/sdX1
sudo swapoff /dev/sdX2</code></pre>
</div>

<div class="problem">
    <h3>6. Помилки <code>parted</code>, <code>wipefs</code> або <code>sgdisk</code></h3>
    <p><strong>Причина:</strong> диск використовується або до нього немає доступу.</p>
    <p><strong>Вирішення:</strong></p>
    <ul>
        <li>Переконайтеся, що диск не змонтовано.</li>
        <li>Якщо диск «зайнятий», спробуйте відмонтувати всі його розділи.</li>
        <li>В крайньому випадку використовуйте <code>lsblk</code>, щоб знайти процес, який блокує диск.</li>
    </ul>
</div>

<div class="problem">
    <h3>7. <code>basestrap</code> запитує провайдера пакета</h3>
    <p><strong>Причина:</strong> кілька пакетів надають той самий функціонал.</p>
    <p><strong>Вирішення:</strong> обирайте рекомендовані варіанти:</p>
    <ul>
        <li><code>iptables-nft</code> замість застарілого iptables.</li>
        <li><code>mkinitcpio</code> для створення initramfs.</li>
        <li><code>xorg-server</code> для Xorg.</li>
    </ul>
</div>

<div class="problem">
    <h3>8. <code>basestrap failed</code></h3>
    <p><strong>Причина:</strong> зазвичай проблема з мережею, дзеркалами або неправильною назвою пакета.</p>
    <p><strong>Вирішення:</strong></p>
    <ul>
        <li>Перевірте інтернет.</li>
        <li>Оновіть список дзеркал у live-режимі:</li>
    </ul>
    <pre><code>sudo reflector --country Ukraine --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist</code></pre>
</div>

<div class="problem">
    <h3>9. Не визначилася відеокарта</h3>
    <p><strong>Причина:</strong> <code>lspci</code> не бачить GPU або його вивід не розпізнано.</p>
    <p><strong>Вирішення:</strong> після встановлення встановіть драйвери вручну. Наприклад, для NVIDIA:</p>
    <pre><code>sudo pacman -S nvidia-dkms nvidia-utils nvidia-settings</code></pre>
    <p>Для AMD:</p>
    <pre><code>sudo pacman -S mesa vulkan-radeon xf86-video-amdgpu</code></pre>
</div>

<div class="problem">
    <h3>10. Проблеми з NVIDIA в Wayland</h3>
    <p><strong>Причина:</strong> пропрієтарний драйвер NVIDIA потребує додаткових параметрів.</p>
    <p><strong>Вирішення:</strong> скрипт мав додати їх автоматично:</p>
    <ul>
        <li>Параметр ядра <code>nvidia-drm.modeset=1</code>.</li>
        <li>Модулі <code>nvidia nvidia_modeset nvidia_uvm nvidia_drm</code> у <code>/etc/mkinitcpio.conf</code>.</li>
    </ul>
    <p>Якщо цього не сталося, зробіть вручну і перестворіть initramfs:</p>
    <pre><code>sudo mkinitcpio -P
sudo grub-mkconfig -o /boot/grub/grub.cfg</code></pre>
</div>

<div class="problem">
    <h3>11. Не запускається PipeWire / немає звуку</h3>
    <p><strong>Причина:</strong> у OpenRC немає systemd user-сесій, тому PipeWire не завжди стартує автоматично.</p>
    <p><strong>Вирішення:</strong> скрипт створює autostart-записи для користувача. Якщо звуку немає, перевірте:</p>
    <pre><code>pactl info
ps aux | grep pipewire</code></pre>
    <p>Запустіть вручну:</p>
    <pre><code>pipewire &amp;
wireplumber &amp;</code></pre>
</div>

<div class="problem">
    <h3>12. Bluetooth не працює</h3>
    <p><strong>Причина:</strong> сервіс може називатися <code>bluetooth</code> замість <code>bluetoothd</code> на деяких варіантах init.</p>
    <p><strong>Вирішення:</strong></p>
    <pre><code>sudo rc-update add bluetooth default
sudo rc-service bluetooth start</code></pre>
</div>

<div class="problem">
    <h3>13. Помилка під час створення initramfs / GRUB</h3>
    <p><strong>Причина:</strong> всередині chroot могли не підтягнутися всі модулі або не спрацював <code>grub-install</code>.</p>
    <p><strong>Вирішення:</strong> зайдіть у chroot встановленої системи з live USB:</p>
    <pre><code>sudo artix-chroot /mnt
mkinitcpio -P
grub-mkconfig -o /boot/grub/grub.cfg
exit</code></pre>
</div>

<div class="problem">
    <h3>14. Хочу безпечно протестувати скрипт</h3>
    <p><strong>Вирішення:</strong> використовуйте режим пробного запуску:</p>
    <pre><code>./artix-installer.sh --dry-run</code></pre>
    <p>Він не змінить диски, але покаже весь план дій.</p>
</div>

<p>
    Повернутися на <a href="/">головну сторінку</a>
    або відвідати сайт <a href="/artix">Artix Linux</a>.
</p>
""").strip(),
        },
        "ru": {
            "title": 'Возможные проблемы — Artix Installer',
            "body": dedent("""\
<h1>Возможные проблемы и решения</h1>

<p>
    Ниже собраны типичные ситуации, с которыми можно столкнуться при работе
    с установщиком, и способы их решения.
</p>

<div class="problem">
    <h3>1. «Run this script as root»</h3>
    <p><strong>Причина:</strong> установщик должен запускаться с правами суперпользователя.</p>
    <p><strong>Решение:</strong></p>
    <pre><code>sudo ./artix-installer.sh</code></pre>
</div>

<div class="problem">
    <h3>2. «No internet connection»</h3>
    <p><strong>Причина:</strong> для установки пакетов через <code>basestrap</code> нужен интернет.</p>
    <p><strong>Решение:</strong> проверьте подключение:</p>
    <pre><code>ping -c 3 archlinux.org</code></pre>
    <p>Если используете Wi-Fi, подключитесь через <code>iwctl</code> или <code>nmtui</code> до запуска скрипта.</p>
</div>

<div class="problem">
    <h3>3. Скрипт стер не тот диск</h3>
    <p><strong>Причина:</strong> выбран неправильный диск. Скрипт не проверяет, является ли диск загрузочным USB.</p>
    <p><strong>Решение:</strong></p>
    <ul>
        <li>Внимательно смотрите на модель и размер диска.</li>
        <li>Сначала запустите <code>--dry-run</code>, чтобы увидеть, какой диск будет выбран.</li>
        <li>В виртуальной машине отключите лишние диски.</li>
    </ul>
</div>

<div class="problem">
    <h3>4. «Disk is too small»</h3>
    <p><strong>Причина:</strong> диск меньше, чем требуется для EFI (512 МиБ), swap и минимального root (5 ГиБ).</p>
    <p><strong>Решение:</strong> используйте диск объёмом не менее 16–20 ГиБ. Для комфортной работы с KDE рекомендуется 40 ГиБ и больше.</p>
</div>

<div class="problem">
    <h3>5. «Some partitions are currently mounted»</h3>
    <p><strong>Причина:</strong> на выбранном диске уже смонтированы разделы.</p>
    <p><strong>Решение:</strong> либо выберите другой диск, либо отмонтируйте разделы вручную:</p>
    <pre><code>sudo umount /dev/sdX1
sudo swapoff /dev/sdX2</code></pre>
</div>

<div class="problem">
    <h3>6. Ошибки <code>parted</code>, <code>wipefs</code> или <code>sgdisk</code></h3>
    <p><strong>Причина:</strong> диск используется или к нему нет доступа.</p>
    <p><strong>Решение:</strong></p>
    <ul>
        <li>Убедитесь, что диск не смонтирован.</li>
        <li>Если диск «занят», попробуйте отмонтировать все его разделы.</li>
        <li>В крайнем случае используйте <code>lsblk</code>, чтобы найти мешающий процесс.</li>
    </ul>
</div>

<div class="problem">
    <h3>7. <code>basestrap</code> спрашивает провайдера пакета</h3>
    <p><strong>Причина:</strong> несколько пакетов предоставляют один и тот же функционал.</p>
    <p><strong>Решение:</strong> выбирайте рекомендуемые варианты:</p>
    <ul>
        <li><code>iptables-nft</code> вместо устаревшего iptables.</li>
        <li><code>mkinitcpio</code> для создания initramfs.</li>
        <li><code>xorg-server</code> для Xorg.</li>
    </ul>
</div>

<div class="problem">
    <h3>8. <code>basestrap failed</code></h3>
    <p><strong>Причина:</strong> обычно проблема с сетью, зеркалами или неверным именем пакета.</p>
    <p><strong>Решение:</strong></p>
    <ul>
        <li>Проверьте интернет.</li>
        <li>Обновите список зеркал в live-режиме:</li>
    </ul>
    <pre><code>sudo reflector --country Ukraine --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist</code></pre>
</div>

<div class="problem">
    <h3>9. Не определилась видеокарта</h3>
    <p><strong>Причина:</strong> <code>lspci</code> не видит GPU или его вывод не распознан.</p>
    <p><strong>Решение:</strong> после установки установите драйверы вручную. Например, для NVIDIA:</p>
    <pre><code>sudo pacman -S nvidia-dkms nvidia-utils nvidia-settings</code></pre>
    <p>Для AMD:</p>
    <pre><code>sudo pacman -S mesa vulkan-radeon xf86-video-amdgpu</code></pre>
</div>

<div class="problem">
    <h3>10. Проблемы с NVIDIA в Wayland</h3>
    <p><strong>Причина:</strong> проприетарный драйвер NVIDIA требует дополнительных параметров.</p>
    <p><strong>Решение:</strong> скрипт должен был добавить их автоматически:</p>
    <ul>
        <li>Параметр ядра <code>nvidia-drm.modeset=1</code>.</li>
        <li>Модули <code>nvidia nvidia_modeset nvidia_uvm nvidia_drm</code> в <code>/etc/mkinitcpio.conf</code>.</li>
    </ul>
    <p>Если этого не произошло, сделайте вручную и пересоздайте initramfs:</p>
    <pre><code>sudo mkinitcpio -P
sudo grub-mkconfig -o /boot/grub/grub.cfg</code></pre>
</div>

<div class="problem">
    <h3>11. Не запускается PipeWire / нет звука</h3>
    <p><strong>Причина:</strong> в OpenRC нет systemd user-сессий, поэтому PipeWire не всегда стартует автоматически.</p>
    <p><strong>Решение:</strong> скрипт создаёт autostart-записи для пользователя. Если звука нет, проверьте:</p>
    <pre><code>pactl info
ps aux | grep pipewire</code></pre>
    <p>Запустите вручную:</p>
    <pre><code>pipewire &amp;
wireplumber &amp;</code></pre>
</div>

<div class="problem">
    <h3>12. Bluetooth не работает</h3>
    <p><strong>Причина:</strong> сервис может называться <code>bluetooth</code> вместо <code>bluetoothd</code> на некоторых вариантах init.</p>
    <p><strong>Решение:</strong></p>
    <pre><code>sudo rc-update add bluetooth default
sudo rc-service bluetooth start</code></pre>
</div>

<div class="problem">
    <h3>13. Ошибка при создании initramfs / GRUB</h3>
    <p><strong>Причина:</strong> внутри chroot могли не подтянуться все модули или не сработал <code>grub-install</code>.</p>
    <p><strong>Решение:</strong> зайдите в chroot установленной системы с live USB:</p>
    <pre><code>sudo artix-chroot /mnt
mkinitcpio -P
grub-mkconfig -o /boot/grub/grub.cfg
exit</code></pre>
</div>

<div class="problem">
    <h3>14. Хочу протестировать скрипт безопасно</h3>
    <p><strong>Решение:</strong> используйте режим пробного запуска:</p>
    <pre><code>./artix-installer.sh --dry-run</code></pre>
    <p>Он не изменит диски, но покажет весь план действий.</p>
</div>

<p>
    Вернуться на <a href="/">главную страницу</a>
    или посетить сайт <a href="/artix">Artix Linux</a>.
</p>
""").strip(),
        },
        "pl": {
            "title": 'Możliwe problemy — Artix Installer',
            "body": dedent("""\
<h1>Możliwe problemy i rozwiązania</h1>

<p>
    Poniżej zebrano typowe sytuacje, które mogą wystąpić podczas korzystania
    z instalatora, oraz sposoby ich rozwiązania.
</p>

<div class="problem">
    <h3>1. „Run this script as root”</h3>
    <p><strong>Przyczyna:</strong> instalator musi być uruchamiany z uprawnieniami root.</p>
    <p><strong>Rozwiązanie:</strong></p>
    <pre><code>sudo ./artix-installer.sh</code></pre>
</div>

<div class="problem">
    <h3>2. „No internet connection”</h3>
    <p><strong>Przyczyna:</strong> do instalacji pakietów przez <code>basestrap</code> potrzebny jest internet.</p>
    <p><strong>Rozwiązanie:</strong> sprawdź połączenie:</p>
    <pre><code>ping -c 3 archlinux.org</code></pre>
    <p>Jeśli używasz Wi-Fi, połącz się przez <code>iwctl</code> lub <code>nmtui</code> przed uruchomieniem skryptu.</p>
</div>

<div class="problem">
    <h3>3. Skrypt wymazał niewłaściwy dysk</h3>
    <p><strong>Przyczyna:</strong> wybrano niewłaściwy dysk. Skrypt nie sprawdza, czy dysk jest bootowalnym USB.</p>
    <p><strong>Rozwiązanie:</strong></p>
    <ul>
        <li>Uważnie sprawdź model i rozmiar dysku.</li>
        <li>Najpierw uruchom <code>--dry-run</code>, aby zobaczyć, który dysk zostanie wybrany.</li>
        <li>W maszynie wirtualnej odłącz zbędne dyski.</li>
    </ul>
</div>

<div class="problem">
    <h3>4. „Disk is too small”</h3>
    <p><strong>Przyczyna:</strong> dysk jest mniejszy niż wymagane dla EFI (512 MiB), swap i minimalnego root (5 GiB).</p>
    <p><strong>Rozwiązanie:</strong> użyj dysku o pojemności co najmniej 16–20 GiB. Dla komfortowej pracy z KDE zalecane jest 40 GiB lub więcej.</p>
</div>

<div class="problem">
    <h3>5. „Some partitions are currently mounted”</h3>
    <p><strong>Przyczyna:</strong> na wybranym dysku są już zamontowane partycje.</p>
    <p><strong>Rozwiązanie:</strong> wybierz inny dysk lub odmontuj partycje ręcznie:</p>
    <pre><code>sudo umount /dev/sdX1
sudo swapoff /dev/sdX2</code></pre>
</div>

<div class="problem">
    <h3>6. Błędy <code>parted</code>, <code>wipefs</code> lub <code>sgdisk</code></h3>
    <p><strong>Przyczyna:</strong> dysk jest w użyciu lub jest niedostępny.</p>
    <p><strong>Rozwiązanie:</strong></p>
    <ul>
        <li>Upewnij się, że dysk nie jest zamontowany.</li>
        <li>Jeśli dysk jest „zajęty”, spróbuj odmontować wszystkie jego partycje.</li>
        <li>W ostateczności użyj <code>lsblk</code>, aby znaleźć proces blokujący dysk.</li>
    </ul>
</div>

<div class="problem">
    <h3>7. <code>basestrap</code> pyta o dostawcę pakietu</h3>
    <p><strong>Przyczyna:</strong> kilka pakietów dostarcza tę samą funkcjonalność.</p>
    <p><strong>Rozwiązanie:</strong> wybieraj zalecane opcje:</p>
    <ul>
        <li><code>iptables-nft</code> zamiast starszego iptables.</li>
        <li><code>mkinitcpio</code> do tworzenia initramfs.</li>
        <li><code>xorg-server</code> dla Xorg.</li>
    </ul>
</div>

<div class="problem">
    <h3>8. <code>basestrap failed</code></h3>
    <p><strong>Przyczyna:</strong> zazwyczaj problem z siecią, mirrorami lub nieprawidłową nazwą pakietu.</p>
    <p><strong>Rozwiązanie:</strong></p>
    <ul>
        <li>Sprawdź połączenie internetowe.</li>
        <li>Zaktualizuj listę mirrorów w trybie live:</li>
    </ul>
    <pre><code>sudo reflector --country Poland --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist</code></pre>
</div>

<div class="problem">
    <h3>9. Karta graficzna nie została wykryta</h3>
    <p><strong>Przyczyna:</strong> <code>lspci</code> nie widzi GPU lub jego wyjście nie zostało rozpoznane.</p>
    <p><strong>Rozwiązanie:</strong> po instalacji zainstaluj sterowniki ręcznie. Na przykład dla NVIDIA:</p>
    <pre><code>sudo pacman -S nvidia-dkms nvidia-utils nvidia-settings</code></pre>
    <p>Dla AMD:</p>
    <pre><code>sudo pacman -S mesa vulkan-radeon xf86-video-amdgpu</code></pre>
</div>

<div class="problem">
    <h3>10. Problemy z NVIDIA w Wayland</h3>
    <p><strong>Przyczyna:</strong> własnościowy sterownik NVIDIA wymaga dodatkowych parametrów.</p>
    <p><strong>Rozwiązanie:</strong> skrypt powinien dodać je automatycznie:</p>
    <ul>
        <li>Parametr jądra <code>nvidia-drm.modeset=1</code>.</li>
        <li>Moduły <code>nvidia nvidia_modeset nvidia_uvm nvidia_drm</code> w <code>/etc/mkinitcpio.conf</code>.</li>
    </ul>
    <p>Jeśli to nie nastąpiło, dodaj je ręcznie i przebuduj initramfs:</p>
    <pre><code>sudo mkinitcpio -P
sudo grub-mkconfig -o /boot/grub/grub.cfg</code></pre>
</div>

<div class="problem">
    <h3>11. PipeWire nie startuje / brak dźwięku</h3>
    <p><strong>Przyczyna:</strong> w OpenRC nie ma sesji użytkownika systemd, więc PipeWire może nie startować automatycznie.</p>
    <p><strong>Rozwiązanie:</strong> skrypt tworzy wpisy autostart dla użytkownika. Jeśli nie ma dźwięku, sprawdź:</p>
    <pre><code>pactl info
ps aux | grep pipewire</code></pre>
    <p>Uruchom ręcznie:</p>
    <pre><code>pipewire &amp;
wireplumber &amp;</code></pre>
</div>

<div class="problem">
    <h3>12. Bluetooth nie działa</h3>
    <p><strong>Przyczyna:</strong> usługa może nazywać się <code>bluetooth</code> zamiast <code>bluetoothd</code> w niektórych wariantach init.</p>
    <p><strong>Rozwiązanie:</strong></p>
    <pre><code>sudo rc-update add bluetooth default
sudo rc-service bluetooth start</code></pre>
</div>

<div class="problem">
    <h3>13. Błąd podczas tworzenia initramfs / GRUB</h3>
    <p><strong>Przyczyna:</strong> wewnątrz chroot mogły nie załadować się wszystkie moduły lub <code>grub-install</code> nie zadziałał.</p>
    <p><strong>Rozwiązanie:</strong> wejdź do chroot zainstalowanego systemu z live USB:</p>
    <pre><code>sudo artix-chroot /mnt
mkinitcpio -P
grub-mkconfig -o /boot/grub/grub.cfg
exit</code></pre>
</div>

<div class="problem">
    <h3>14. Chcę bezpiecznie przetestować skrypt</h3>
    <p><strong>Rozwiązanie:</strong> użyj trybu próbnego:</p>
    <pre><code>./artix-installer.sh --dry-run</code></pre>
    <p>Nie zmieni on dysków, ale pokaże cały plan działania.</p>
</div>

<p>
    Wróć na <a href="/">stronę główną</a>
    lub odwiedź stronę <a href="/artix">Artix Linux</a>.
</p>
""").strip(),
        },
        "fr": {
            "title": 'Problèmes possibles — Artix Installer',
            "body": dedent("""\
<h1>Problèmes possibles et solutions</h1>

<p>
    Voici les situations typiques que vous pouvez rencontrer en utilisant
    l'installateur, ainsi que les façons de les résoudre.
</p>

<div class="problem">
    <h3>1. « Run this script as root »</h3>
    <p><strong>Cause :</strong> l'installateur doit être exécuté avec les privilèges root.</p>
    <p><strong>Solution :</strong></p>
    <pre><code>sudo ./artix-installer.sh</code></pre>
</div>

<div class="problem">
    <h3>2. « No internet connection »</h3>
    <p><strong>Cause :</strong> l'installation des paquets via <code>basestrap</code> nécessite Internet.</p>
    <p><strong>Solution :</strong> vérifiez la connectivité :</p>
    <pre><code>ping -c 3 archlinux.org</code></pre>
    <p>Si vous utilisez le Wi-Fi, connectez-vous via <code>iwctl</code> ou <code>nmtui</code> avant de lancer le script.</p>
</div>

<div class="problem">
    <h3>3. Le script a effacé le mauvais disque</h3>
    <p><strong>Cause :</strong> le mauvais disque a été sélectionné. Le script ne vérifie pas si le disque est la clé USB de démarrage.</p>
    <p><strong>Solution :</strong></p>
    <ul>
        <li>Vérifiez attentivement le modèle et la taille du disque.</li>
        <li>Lancez d'abord <code>--dry-run</code> pour voir quel disque sera sélectionné.</li>
        <li>Dans une machine virtuelle, détachez les disques superflus.</li>
    </ul>
</div>

<div class="problem">
    <h3>4. « Disk is too small »</h3>
    <p><strong>Cause :</strong> le disque est plus petit que nécessaire pour l'EFI (512 Mio), le swap et le root minimal (5 Gio).</p>
    <p><strong>Solution :</strong> utilisez un disque d'au moins 16 à 20 Gio. Pour une utilisation confortable de KDE, 40 Gio ou plus sont recommandés.</p>
</div>

<div class="problem">
    <h3>5. « Some partitions are currently mounted »</h3>
    <p><strong>Cause :</strong> certaines partitions du disque sélectionné sont déjà montées.</p>
    <p><strong>Solution :</strong> choisissez un autre disque ou démontez les partitions manuellement :</p>
    <pre><code>sudo umount /dev/sdX1
sudo swapoff /dev/sdX2</code></pre>
</div>

<div class="problem">
    <h3>6. Erreurs de <code>parted</code>, <code>wipefs</code> ou <code>sgdisk</code></h3>
    <p><strong>Cause :</strong> le disque est en cours d'utilisation ou inaccessible.</p>
    <p><strong>Solution :</strong></p>
    <ul>
        <li>Assurez-vous que le disque n'est pas monté.</li>
        <li>Si le disque est « occupé », essayez de démonter toutes ses partitions.</li>
        <li>En dernier recours, utilisez <code>lsblk</code> pour trouver le processus bloquant.</li>
    </ul>
</div>

<div class="problem">
    <h3>7. <code>basestrap</code> demande un fournisseur de paquet</h3>
    <p><strong>Cause :</strong> plusieurs paquets fournissent la même fonctionnalité.</p>
    <p><strong>Solution :</strong> choisissez les options recommandées :</p>
    <ul>
        <li><code>iptables-nft</code> au lieu de l'ancien iptables.</li>
        <li><code>mkinitcpio</code> pour créer l'initramfs.</li>
        <li><code>xorg-server</code> pour Xorg.</li>
    </ul>
</div>

<div class="problem">
    <h3>8. <code>basestrap failed</code></h3>
    <p><strong>Cause :</strong> problème réseau, miroirs ou nom de paquet incorrect.</p>
    <p><strong>Solution :</strong></p>
    <ul>
        <li>Vérifiez votre connexion Internet.</li>
        <li>Mettez à jour la liste des miroirs en mode live :</li>
    </ul>
    <pre><code>sudo reflector --country France --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist</code></pre>
</div>

<div class="problem">
    <h3>9. Le GPU n'a pas été détecté</h3>
    <p><strong>Cause :</strong> <code>lspci</code> ne voit pas le GPU ou sa sortie n'est pas reconnue.</p>
    <p><strong>Solution :</strong> installez les pilotes manuellement après l'installation. Pour NVIDIA :</p>
    <pre><code>sudo pacman -S nvidia-dkms nvidia-utils nvidia-settings</code></pre>
    <p>Pour AMD :</p>
    <pre><code>sudo pacman -S mesa vulkan-radeon xf86-video-amdgpu</code></pre>
</div>

<div class="problem">
    <h3>10. Problèmes NVIDIA sous Wayland</h3>
    <p><strong>Cause :</strong> le pilote propriétaire NVIDIA nécessite des paramètres supplémentaires.</p>
    <p><strong>Solution :</strong> le script devait les ajouter automatiquement :</p>
    <ul>
        <li>Paramètre noyau <code>nvidia-drm.modeset=1</code>.</li>
        <li>Modules <code>nvidia nvidia_modeset nvidia_uvm nvidia_drm</code> dans <code>/etc/mkinitcpio.conf</code>.</li>
    </ul>
    <p>Si ce n'est pas le cas, ajoutez-les manuellement et régénérez l'initramfs :</p>
    <pre><code>sudo mkinitcpio -P
sudo grub-mkconfig -o /boot/grub/grub.cfg</code></pre>
</div>

<div class="problem">
    <h3>11. PipeWire ne démarre pas / pas de son</h3>
    <p><strong>Cause :</strong> OpenRC n'a pas de sessions utilisateur systemd, donc PipeWire ne démarre pas toujours automatiquement.</p>
    <p><strong>Solution :</strong> le script crée des entrées autostart pour l'utilisateur. S'il n'y a pas de son, vérifiez :</p>
    <pre><code>pactl info
ps aux | grep pipewire</code></pre>
    <p>Démarrez manuellement :</p>
    <pre><code>pipewire &amp;
wireplumber &amp;</code></pre>
</div>

<div class="problem">
    <h3>12. Le Bluetooth ne fonctionne pas</h3>
    <p><strong>Cause :</strong> le service peut s'appeler <code>bluetooth</code> au lieu de <code>bluetoothd</code> sur certaines variantes d'init.</p>
    <p><strong>Solution :</strong></p>
    <pre><code>sudo rc-update add bluetooth default
sudo rc-service bluetooth start</code></pre>
</div>

<div class="problem">
    <h3>13. Erreur lors de la création de l'initramfs / GRUB</h3>
    <p><strong>Cause :</strong> dans le chroot, certains modules peuvent ne pas se charger ou <code>grub-install</code> peut échouer.</p>
    <p><strong>Solution :</strong> entrez dans le chroot du système installé depuis la live USB :</p>
    <pre><code>sudo artix-chroot /mnt
mkinitcpio -P
grub-mkconfig -o /boot/grub/grub.cfg
exit</code></pre>
</div>

<div class="problem">
    <h3>14. Je veux tester le script en toute sécurité</h3>
    <p><strong>Solution :</strong> utilisez le mode simulation :</p>
    <pre><code>./artix-installer.sh --dry-run</code></pre>
    <p>Il ne modifiera pas les disques, mais affichera tout le plan d'action.</p>
</div>

<p>
    Retour à la <a href="/">page d'accueil</a>
    ou visitez le site <a href="/artix">Artix Linux</a>.
</p>
""").strip(),
        },
        "it": {
            "title": 'Possibili problemi — Artix Installer',
            "body": dedent("""\
<h1>Possibili problemi e soluzioni</h1>

<p>
    Di seguito sono raccolte le situazioni tipiche che puoi incontrare
    utilizzando l'installatore, insieme ai modi per risolverle.
</p>

<div class="problem">
    <h3>1. «Run this script as root»</h3>
    <p><strong>Causa:</strong> l'installatore deve essere eseguito con i privilegi di root.</p>
    <p><strong>Soluzione:</strong></p>
    <pre><code>sudo ./artix-installer.sh</code></pre>
</div>

<div class="problem">
    <h3>2. «No internet connection»</h3>
    <p><strong>Causa:</strong> l'installazione dei pacchetti tramite <code>basestrap</code> richiede Internet.</p>
    <p><strong>Soluzione:</strong> verifica la connettività:</p>
    <pre><code>ping -c 3 archlinux.org</code></pre>
    <p>Se usi il Wi-Fi, connettiti tramite <code>iwctl</code> o <code>nmtui</code> prima di avviare lo script.</p>
</div>

<div class="problem">
    <h3>3. Lo script ha cancellato il disco sbagliato</h3>
    <p><strong>Causa:</strong> è stato selezionato il disco sbagliato. Lo script non verifica se il disco è la chiavetta USB di avvio.</p>
    <p><strong>Soluzione:</strong></p>
    <ul>
        <li>Controlla attentamente modello e dimensione del disco.</li>
        <li>Avvia prima <code>--dry-run</code> per vedere quale disco verrà selezionato.</li>
        <li>In una macchina virtuale, scollega i dischi superflui.</li>
    </ul>
</div>

<div class="problem">
    <h3>4. «Disk is too small»</h3>
    <p><strong>Causa:</strong> il disco è più piccolo del necessario per EFI (512 MiB), swap e root minimo (5 GiB).</p>
    <p><strong>Soluzione:</strong> usa un disco di almeno 16–20 GiB. Per un uso confortevole di KDE si consigliano 40 GiB o più.</p>
</div>

<div class="problem">
    <h3>5. «Some partitions are currently mounted»</h3>
    <p><strong>Causa:</strong> sul disco selezionato sono già montate delle partizioni.</p>
    <p><strong>Soluzione:</strong> scegli un altro disco o smonta le partizioni manualmente:</p>
    <pre><code>sudo umount /dev/sdX1
sudo swapoff /dev/sdX2</code></pre>
</div>

<div class="problem">
    <h3>6. Errori di <code>parted</code>, <code>wipefs</code> o <code>sgdisk</code></h3>
    <p><strong>Causa:</strong> il disco è in uso o non accessibile.</p>
    <p><strong>Soluzione:</strong></p>
    <ul>
        <li>Assicurati che il disco non sia montato.</li>
        <li>Se il disco è "occupato", prova a smontare tutte le sue partizioni.</li>
        <li>In ultima istanza, usa <code>lsblk</code> per trovare il processo che blocca il disco.</li>
    </ul>
</div>

<div class="problem">
    <h3>7. <code>basestrap</code> chiede un provider di pacchetti</h3>
    <p><strong>Causa:</strong> più pacchetti forniscono la stessa funzionalità.</p>
    <p><strong>Soluzione:</strong> scegli le opzioni consigliate:</p>
    <ul>
        <li><code>iptables-nft</code> invece del vecchio iptables.</li>
        <li><code>mkinitcpio</code> per creare l'initramfs.</li>
        <li><code>xorg-server</code> per Xorg.</li>
    </ul>
</div>

<div class="problem">
    <h3>8. <code>basestrap failed</code></h3>
    <p><strong>Causa:</strong> solitamente un problema di rete, mirror o nome pacchetto errato.</p>
    <p><strong>Soluzione:</strong></p>
    <ul>
        <li>Verifica la connessione Internet.</li>
        <li>Aggiorna la lista dei mirror in modalità live:</li>
    </ul>
    <pre><code>sudo reflector --country Italy --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist</code></pre>
</div>

<div class="problem">
    <h3>9. La GPU non è stata rilevata</h3>
    <p><strong>Causa:</strong> <code>lspci</code> non vede la GPU o il suo output non è riconosciuto.</p>
    <p><strong>Soluzione:</strong> dopo l'installazione installa i driver manualmente. Per NVIDIA:</p>
    <pre><code>sudo pacman -S nvidia-dkms nvidia-utils nvidia-settings</code></pre>
    <p>Per AMD:</p>
    <pre><code>sudo pacman -S mesa vulkan-radeon xf86-video-amdgpu</code></pre>
</div>

<div class="problem">
    <h3>10. Problemi NVIDIA con Wayland</h3>
    <p><strong>Causa:</strong> il driver proprietario NVIDIA richiede parametri aggiuntivi.</p>
    <p><strong>Soluzione:</strong> lo script avrebbe dovuto aggiungerli automaticamente:</p>
    <ul>
        <li>Parametro del kernel <code>nvidia-drm.modeset=1</code>.</li>
        <li>Moduli <code>nvidia nvidia_modeset nvidia_uvm nvidia_drm</code> in <code>/etc/mkinitcpio.conf</code>.</li>
    </ul>
    <p>Se non è successo, aggiungili manualmente e rigenera l'initramfs:</p>
    <pre><code>sudo mkinitcpio -P
sudo grub-mkconfig -o /boot/grub/grub.cfg</code></pre>
</div>

<div class="problem">
    <h3>11. PipeWire non si avvia / nessun audio</h3>
    <p><strong>Causa:</strong> in OpenRC non ci sono sessioni utente systemd, quindi PipeWire potrebbe non avviarsi automaticamente.</p>
    <p><strong>Soluzione:</strong> lo script crea voci di autostart per l'utente. Se non c'è audio, controlla:</p>
    <pre><code>pactl info
ps aux | grep pipewire</code></pre>
    <p>Avvia manualmente:</p>
    <pre><code>pipewire &amp;
wireplumber &amp;</code></pre>
</div>

<div class="problem">
    <h3>12. Il Bluetooth non funziona</h3>
    <p><strong>Causa:</strong> il servizio potrebbe chiamarsi <code>bluetooth</code> invece di <code>bluetoothd</code> in alcune varianti init.</p>
    <p><strong>Soluzione:</strong></p>
    <pre><code>sudo rc-update add bluetooth default
sudo rc-service bluetooth start</code></pre>
</div>

<div class="problem">
    <h3>13. Errore durante la creazione di initramfs / GRUB</h3>
    <p><strong>Causa:</strong> dentro il chroot alcuni moduli potrebbero non essere caricati o <code>grub-install</code> potrebbe fallire.</p>
    <p><strong>Soluzione:</strong> entra nel chroot del sistema installato dalla live USB:</p>
    <pre><code>sudo artix-chroot /mnt
mkinitcpio -P
grub-mkconfig -o /boot/grub/grub.cfg
exit</code></pre>
</div>

<div class="problem">
    <h3>14. Voglio testare lo script in sicurezza</h3>
    <p><strong>Soluzione:</strong> usa la modalità di simulazione:</p>
    <pre><code>./artix-installer.sh --dry-run</code></pre>
    <p>Non modificherà i dischi, ma mostrerà l'intero piano d'azione.</p>
</div>

<p>
    Torna alla <a href="/">pagina principale</a>
    o visita il sito <a href="/artix">Artix Linux</a>.
</p>
""").strip(),
        },
        "de": {
            "title": 'Mögliche Probleme — Artix Installer',
            "body": dedent("""\
<h1>Mögliche Probleme und Lösungen</h1>

<p>
    Nachfolgend sind typische Situationen aufgeführt, die bei der Verwendung
    des Installationsassistenten auftreten können, sowie Möglichkeiten, sie zu lösen.
</p>

<div class="problem">
    <h3>1. „Run this script as root“</h3>
    <p><strong>Ursache:</strong> der Installationsassistent muss mit Root-Rechten ausgeführt werden.</p>
    <p><strong>Lösung:</strong></p>
    <pre><code>sudo ./artix-installer.sh</code></pre>
</div>

<div class="problem">
    <h3>2. „No internet connection“</h3>
    <p><strong>Ursache:</strong> für die Paketinstallation über <code>basestrap</code> ist Internet erforderlich.</p>
    <p><strong>Lösung:</strong> prüfen Sie die Konnektivität:</p>
    <pre><code>ping -c 3 archlinux.org</code></pre>
    <p>Wenn Sie Wi-Fi verwenden, verbinden Sie sich vor dem Start des Skripts über <code>iwctl</code> oder <code>nmtui</code>.</p>
</div>

<div class="problem">
    <h3>3. Das Skript hat die falsche Festplatte gelöscht</h3>
    <p><strong>Ursache:</strong> die falsche Festplatte wurde ausgewählt. Das Skript prüft nicht, ob es sich um das bootfähige USB-Laufwerk handelt.</p>
    <p><strong>Lösung:</strong></p>
    <ul>
        <li>Prüfen Sie Modell und Größe der Festplatte sorgfältig.</li>
        <li>Starten Sie zuerst <code>--dry-run</code>, um zu sehen, welche Festplatte ausgewählt wird.</li>
        <li>In einer virtuellen Maschine trennen Sie überflüssige Festplatten.</li>
    </ul>
</div>

<div class="problem">
    <h3>4. „Disk is too small“</h3>
    <p><strong>Ursache:</strong> die Festplatte ist kleiner als für EFI (512 MiB), Swap und minimales Root (5 GiB) erforderlich.</p>
    <p><strong>Lösung:</strong> verwenden Sie eine Festplatte mit mindestens 16–20 GiB. Für komfortable Arbeit mit KDE werden 40 GiB oder mehr empfohlen.</p>
</div>

<div class="problem">
    <h3>5. „Some partitions are currently mounted“</h3>
    <p><strong>Ursache:</strong> auf der ausgewählten Festplatte sind bereits Partitionen eingehängt.</p>
    <p><strong>Lösung:</strong> wählen Sie eine andere Festplatte oder hängen Sie die Partitionen manuell aus:</p>
    <pre><code>sudo umount /dev/sdX1
sudo swapoff /dev/sdX2</code></pre>
</div>

<div class="problem">
    <h3>6. Fehler von <code>parted</code>, <code>wipefs</code> oder <code>sgdisk</code></h3>
    <p><strong>Ursache:</strong> die Festplatte wird verwendet oder ist nicht zugänglich.</p>
    <p><strong>Lösung:</strong></p>
    <ul>
        <li>Stellen Sie sicher, dass die Festplatte nicht eingehängt ist.</li>
        <li>Wenn die Festplatte „beschäftigt“ ist, versuchen Sie, alle Partitionen auszuhängen.</li>
        <li>Im Notfall verwenden Sie <code>lsblk</code>, um den blockierenden Prozess zu finden.</li>
    </ul>
</div>

<div class="problem">
    <h3>7. <code>basestrap</code> fragt nach einem Paketprovider</h3>
    <p><strong>Ursache:</strong> mehrere Pakete bieten dieselbe Funktionalität.</p>
    <p><strong>Lösung:</strong> wählen Sie die empfohlenen Optionen:</p>
    <ul>
        <li><code>iptables-nft</code> statt des alten iptables.</li>
        <li><code>mkinitcpio</code> zum Erstellen des Initramfs.</li>
        <li><code>xorg-server</code> für Xorg.</li>
    </ul>
</div>

<div class="problem">
    <h3>8. <code>basestrap failed</code></h3>
    <p><strong>Ursache:</strong> in der Regel ein Netzwerk-, Spiegel- oder Paketnamenproblem.</p>
    <p><strong>Lösung:</strong></p>
    <ul>
        <li>Prüfen Sie Ihre Internetverbindung.</li>
        <li>Aktualisieren Sie die Spiegelliste im Live-Modus:</li>
    </ul>
    <pre><code>sudo reflector --country Germany --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist</code></pre>
</div>

<div class="problem">
    <h3>9. GPU wurde nicht erkannt</h3>
    <p><strong>Ursache:</strong> <code>lspci</code> sieht die GPU nicht oder die Ausgabe wird nicht erkannt.</p>
    <p><strong>Lösung:</strong> installieren Sie die Treiber nach der Installation manuell. Für NVIDIA:</p>
    <pre><code>sudo pacman -S nvidia-dkms nvidia-utils nvidia-settings</code></pre>
    <p>Für AMD:</p>
    <pre><code>sudo pacman -S mesa vulkan-radeon xf86-video-amdgpu</code></pre>
</div>

<div class="problem">
    <h3>10. NVIDIA-Probleme unter Wayland</h3>
    <p><strong>Ursache:</strong> der proprietäre NVIDIA-Treiber erfordert zusätzliche Parameter.</p>
    <p><strong>Lösung:</strong> das Skript hätte diese automatisch hinzufügen sollen:</p>
    <ul>
        <li>Kernelparameter <code>nvidia-drm.modeset=1</code>.</li>
        <li>Module <code>nvidia nvidia_modeset nvidia_uvm nvidia_drm</code> in <code>/etc/mkinitcpio.conf</code>.</li>
    </ul>
    <p>Wenn nicht, fügen Sie sie manuell hinzu und regenerieren Sie das Initramfs:</p>
    <pre><code>sudo mkinitcpio -P
sudo grub-mkconfig -o /boot/grub/grub.cfg</code></pre>
</div>

<div class="problem">
    <h3>11. PipeWire startet nicht / kein Ton</h3>
    <p><strong>Ursache:</strong> in OpenRC gibt es keine systemd-Benutzersitzungen, daher startet PipeWire nicht immer automatisch.</p>
    <p><strong>Lösung:</strong> das Skript erstellt Autostart-Einträge für den Benutzer. Wenn es keinen Ton gibt, prüfen Sie:</p>
    <pre><code>pactl info
ps aux | grep pipewire</code></pre>
    <p>Starten Sie manuell:</p>
    <pre><code>pipewire &amp;
wireplumber &amp;</code></pre>
</div>

<div class="problem">
    <h3>12. Bluetooth funktioniert nicht</h3>
    <p><strong>Ursache:</strong> der Dienst kann auf einigen Init-Varianten <code>bluetooth</code> statt <code>bluetoothd</code> heißen.</p>
    <p><strong>Lösung:</strong></p>
    <pre><code>sudo rc-update add bluetooth default
sudo rc-service bluetooth start</code></pre>
</div>

<div class="problem">
    <h3>13. Fehler beim Erstellen von Initramfs / GRUB</h3>
    <p><strong>Ursache:</strong> innerhalb des Chroot konnten nicht alle Module geladen werden oder <code>grub-install</code> ist fehlgeschlagen.</p>
    <p><strong>Lösung:</strong> betreten Sie das Chroot des installierten Systems von der Live-USB aus:</p>
    <pre><code>sudo artix-chroot /mnt
mkinitcpio -P
grub-mkconfig -o /boot/grub/grub.cfg
exit</code></pre>
</div>

<div class="problem">
    <h3>14. Ich möchte das Skript sicher testen</h3>
    <p><strong>Lösung:</strong> verwenden Sie den Trockenlauf-Modus:</p>
    <pre><code>./artix-installer.sh --dry-run</code></pre>
    <p>Er wird keine Festplatten ändern, sondern den gesamten Aktionsplan anzeigen.</p>
</div>

<p>
    Zurück zur <a href="/">Startseite</a>
    oder zur Website <a href="/artix">Artix Linux</a>.
</p>
""").strip(),
        },
    },
}

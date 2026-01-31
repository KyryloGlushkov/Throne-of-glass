################################################################################
## Ініціалізація
################################################################################

## Оператор "init offset" змушує оператори ініціалізації у цьому файлі
## виконуватися перед операторами "init" в будь-якому іншому файлі.
init offset = -2

## При виклику "gui.init" стилі відновлюються до розумних стандартних значень, а
## також встановлюються ширина і висота гри.
init python:
    gui.init(1920, 1080)

## Увімкнути перевірку на наявність недійсних або нестабільних властивостей в
## екранах або трансформаціях
define config.check_conflicting_properties = True


################################################################################
## Змінні конфігурації інтерфейсу
################################################################################


## Кольори #####################################################################
##
## Кольори тексту в інтерфейсі.

## Акцентний колір інтерфейсу для позначення і підсвічування тексту.
define gui.accent_color = '#9933ff'

## Колір текстової кнопки, коли її не вибрано і не наведено вказівником.
define gui.idle_color = '#888888'

## Малий колір використовується для маленького тексту, який має бути яскравішим/
## темнішим для досягнення того самого ефекту.
define gui.idle_small_color = '#aaaaaa'

## Колір для кнопок і смуг при наведенні вказівником.
define gui.hover_color = '#c184ff'

## Колір текстової кнопки, коли її вибрано, але не сфокосовано. Кнопку вибрано,
## якщо вона на поточному екрані або значенням налаштування.
define gui.selected_color = '#ffffff'

## Колір текстової кнопки, коли її неможливо вибрати.
define gui.insensitive_color = '#8888887f'

## Кольори частин смуг, які не заповнені. Вони не використовуються
## безпосередньо, але застосовуються під час повторного створення файлів
## зображень смуг.
define gui.muted_color = '#3d1466'
define gui.hover_muted_color = '#5b1e99'

## Кольори тексту діалогу та меню вибору.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Шрифти та розміри шрифтів ###################################################

## Шрифт для тексту в грі.
define gui.text_font = "DejaVuSans.ttf"

## Шрифт для імен персонажів.
define gui.name_text_font = "DejaVuSans.ttf"

## Шрифт для тексту поза грою.
define gui.interface_text_font = "DejaVuSans.ttf"

## Розмір звичайного тексту діалогу.
define gui.text_size = 33

## Розмір імен персонажів.
define gui.name_text_size = 45

## Розмір тексту в інтерфейсі гри.
define gui.interface_text_size = 33

## Розмір міток в інтерфейсі гри.
define gui.label_text_size = 36

## Розмір тексту на екрані сповіщень.
define gui.notify_text_size = 24

## Розмір назви гри.
define gui.title_text_size = 75


## Головне меню та меню гри ####################################################

## Зображення, використані для головного меню і меню гри.
define gui.main_menu_background = "images/main.jpg"
define gui.game_menu_background = "gui/game_menu.png"


## Діалог ######################################################################
##
## Ці змінні визначають, як діалог виводиться на екран по одному рядку.

## Висота текстового поля, що містить діалог.
define gui.textbox_height = 278

## Розташування текстового поля по вертикалі на екрані. 0,0 — верх, 0,5 — центр,
## 1,0 — низ.
define gui.textbox_yalign = 1.0


## Розташування імені персонажа, відносно текстового поля. Значення може бути
## цілим числом пікселів від лівого краю або верхнього краю, або 0,5 до центру.
define gui.name_xpos = 360
define gui.name_ypos = 0

## Горизонтальне вирівнювання імені персонажа. Значення може бути 0,0 для
## вирівнювання по лівому краю, 0,5 по центру і 1,0 по правому краю.
define gui.name_xalign = 0.0

## Ширина, висота та межі поля, що містить ім’я персонажа, або None для
## автоматичного визначення розміру.
define gui.namebox_width = None
define gui.namebox_height = None

## Межі поля, що містить імʼя персонажа, у порядку зліва, зверху, справа, знизу.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Якщо задано "True", тло поля імені буде мозаїчним. Якщо задано "False", тло
## поля імені буде масштабованим.
define gui.namebox_tile = False


## Розташування діалогу відносно текстового поля. Значення може бути цілим
## числом пікселів відносно лівого або верхнього краю текстового поля, або 0,5
## для вирівнювання по центру.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## Максимальна ширина тексту діалогу у пікселях.
define gui.dialogue_width = 1116

## Горизонтальне вирівнювання тексту діалогу. Значення може бути 0,0 для
## вирівнювання по лівому краю, 0,5 по центру і 1,0 по правому краю.
define gui.dialogue_text_xalign = 0.0


## Кнопки ######################################################################
##
## Ці змінні, разом із файлами зображень у теці "gui/button", визначають аспекти
## показу кнопок.

## Ширина та висота кнопки у пікселях. Якщо задано "None", Ren'Py обчислюватиме
## розмір.
define gui.button_width = None
define gui.button_height = None

## Межі з кожного боку кнопки в порядку: ліворуч, зверху, праворуч, знизу.
define gui.button_borders = Borders(6, 6, 6, 6)

## Якщо задано "True", зображення тла буде мозаїчним. Якщо задано "False",
## зображення тла буде лінійно масштабуватися.
define gui.button_tile = False

## Шрифт кнопки.
define gui.button_text_font = gui.interface_text_font

## Розмір тексту кнопки.
define gui.button_text_size = gui.interface_text_size

## Колір тексту кнопки у різних станах.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Горизонтальне вирівнювання тексту кнопки. (0,0 — ліворуч, 0,5 — по центру,
## 1,0 — праворуч).
define gui.button_text_xalign = 0.0


## Ці змінні замінюють налаштування для різних типів кнопок. Дивіться
## документацію по GUI, щоб дізнатися про типи доступних кнопок та їх
## призначення.
##
## Ці налаштування використовуються стандартним інтерфейсом:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Ви також можете додати власні налаштування, додавши правильно названі змінні.
## Наприклад, ви можете розкоментувати наступний рядок, щоб задати ширину кнопки
## навігації.

# define gui.navigation_button_width = 250


## Кнопки вибору ###############################################################
##
## Кнопки вибору, які використовуються у меню гри.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Кнопки комірок збережень ####################################################
##
## Кнопка комірки збереження — особливий вид кнопки. Вона містить мініатюру і
## текст, що описує уміст комірки збереження. Комірка збереження використовує
## файли зображень у "gui/button", як і інші типи кнопок.

## Кнопка комірки збереження.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Ширина та висота мініатюр, які використовуються комірками збереження.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Кількість стовпців і рядків у сітці комірок збереження.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Позиціонування та інтервал ##################################################
##
## Ці змінні визначають позиціонування та інтервал різних елементів інтерфейсу.

## Позиція лівої сторони навігаційних кнопок відносно лівої сторони екрана.
define gui.navigation_xpos = 60

## Вертикальна позиція індикатора пропуску.
define gui.skip_ypos = 15

## Вертикальна позиція екрана сповіщень.
define gui.notify_ypos = 68

## Інтервал між елементами у меню виборів.
define gui.choice_spacing = 33

## Кнопки в розділі навігації головного меню і меню гри.
define gui.navigation_spacing = 6

## Визначає величину відстані між параметрами.
define gui.pref_spacing = 15

## Визначає відстань між кнопками параметрів.
define gui.pref_button_spacing = 0

## Відстань між кнопками сторінки збережень.
define gui.page_spacing = 0

## Відстань між комірками збережень.
define gui.slot_spacing = 15

## Позиція тексту головного меню.
define gui.main_menu_text_xalign = 1.0


## Рамки #######################################################################
##
## Ці змінні визначають вигляд рамок, які можуть містити компоненти інтерфейсу,
## коли накладення або вікно відсутні.

## Стандартні рамки.
define gui.frame_borders = Borders(6, 6, 6, 6)

## Рамка, яка використовується як частина екрана підтвердження.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## Рамка, яка використовується як частина екрана пропуску.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## Рамка, яка використовується як частина екрана сповіщень.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Чи слід тла рамок викласти плиткою?
define gui.frame_tile = False


## Смуги, смуги прокрутки та повзунки ##########################################
##
## Ці визначають вигляд і розмір смуг, смуг прокруток і повзунків.
##
## Стандартний інтерфейс використовує лише повзунки та вертикальні смуги
## прокрутки. Усі інші смуги використовуються лише на екранах, написаних
## автором.

## Висота горизонтальних смуг, смуг прокруток і повзунків. Ширина вертикальних
## смуг, смуг прокруток і повзунків.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## True, якщо зображення смуги мають бути викладено плиткою. False, якщо вони
## повинні бути лінійно масштабовані.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Горизонтальні межі.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Вертикальні межі.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## Що робити з не прокручуваними смугами прокрутки у меню гри. Параметр "hide"
## приховує їх, а "None" показує їх.
define gui.unscrollable = "hide"


## Історія #####################################################################
##
## Екран історії показує діалоги, які гравець уже закрив.

## Кількість блоків історії діалогів, які Ren'Py збереже.
define config.history_length = 250

## Висота рядку на екрані історії або "None", щоб зробити висоту змінною шляхом
## швидкодії.
define gui.history_height = 210

## Додатковий простір для додавання між рядком на екрані історії.
define gui.history_spacing = 0

## Позиція, ширина та вирівнювання тексту з іменем персонажа.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## Позиція, ширина та вирівнювання тексту діалогу.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## Режим NVL ###################################################################
##
## Екран режиму NVL показує діалоги, які ведуть персонажі в режимі NVL.

## Межі тла вікна заднього плану режиму NVL.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## Максимальна кількість рядків у режимі NVL, які Ren'Py покаже. Якщо потрібно
## показати більше рядків, найстаріший рядок буде видалено.
define gui.nvl_list_length = 6

## Висота рядку в режимі NVL. Задайте значення "None", щоб рядки динамічно
## регулювали висоту.
define gui.nvl_height = 173

## Відстань між рядками режиму NVL, коли "gui.nvl_height" має значення "None",
## та між рядками режиму NVL і меню режиму NVL.
define gui.nvl_spacing = 15

## Позиція, ширина та вирівнювання тексту з іменем персонажа.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## Позиція, ширина та вирівнювання тексту діалогу.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

##  Позиція, ширина та вирівнювання тексту "nvl_thought" (текст, який вимовляє
##  персонаж "nvl_narrator").
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## Позиціонування nvl "menu_buttons".
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Локалізація #################################################################

## Визначає, де дозволений розрив рядка. Стандартне значення підходить
## для більшості мов. Список доступних значень можна знайти на https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Мобільні пристрої
################################################################################

init python:

    ## Збільшує розмір кнопок швидкого меню, щоб їх було легше торкатися на
    ## планшетах і телефонах.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## Змінює розмір і відстань між різними елементами інтерфейсу, щоб вони були
    ## видимими на телефонах.
    @gui.variant
    def small():

        ## Розміри шрифтів.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Відрегулювати розташування текстового поля.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Змінити розмір і відстань між різними речами.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## Макет кнопки збереження.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Режим NVL.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30

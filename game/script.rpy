init python:
 
    renpy.register_shader("name.gradient",
        variables="""
            uniform vec4 u_left;
            uniform vec4 u_right;
            uniform vec2 u_model_size;
            varying float v_done;
            attribute vec4 a_position;
        """,

        vertex_300="""
            v_done = a_position.x / u_model_size.x;
        """,

        fragment_300="""
            gl_FragColor *= mix(u_left, u_right, v_done);
        """
    )

    def get_char_center (tag):
        match tag:
            case "Селена": image_name = "селена"
            case "Принц Дорін": image_name = "дорін"
            case "Герцог Перрантгон": image_name = "перрантгон"
            case "Кальтена": image_name = "кальтена"
            case "Капітан Єстфол": image_name = "шаол"
            case "Нехемія": image_name = "нехемія"
            case "Гвардієць 1": image_name = "гвардієць1"
            case "Гвардієць 2": image_name = "гвардієць2"
            case "Фаліпа": image_name = "фаліпа"
            case "Король": image_name = "король"
            case "Спутниця 1": image_name = "спутниця1"
            case "Спутниця 2": image_name = "спутниця2"            
            case "Кейн": image_name = "кейн"
            case "Брулло": image_name = "брулло"
            case "Ксав'єр": image_name = "ксавєр"
        
        char_pos = renpy.get_image_bounds(image_name)

        if (char_pos == None or float((char_pos[0] + (char_pos[2] / 2))/config.screen_width) < 0.5):
            return 0.2
        else:
            return 0.8

transform grad_selena:
    shader "name.gradient"
    u_left (0.0, 0.65, 0.2, 1.0)   
    u_right (1.0, 1.0, 1.0, 1.0)   

transform grad_dorin:
    shader "name.gradient"
    u_left (0.4, 0.6, 1.0, 1.0)
    u_right (1.0, 1.0, 1.0, 1.0)

transform grad_duke:
    shader "name.gradient"
    u_left (1.0, 0.6, 0.2, 1.0)
    u_right (1.0, 1.0, 1.0, 1.0)

transform grad_kalt:
    shader "name.gradient"
    u_left (0.1, 0.1, 0.1, 1.0)
    u_right (1.0, 1.0, 1.0, 1.0)

transform grad_captain:
    shader "name.gradient"
    u_left (0.5, 0.3, 0.1, 1.0)
    u_right (1.0, 1.0, 1.0, 1.0)

transform grad_nehemia:
    shader "name.gradient"
    u_left (1.0, 0.9, 0.2, 1.0)
    u_right (1.0, 1.0, 1.0, 1.0)

transform grad_falipa:
    shader "name.gradient"
    u_left (0.5, 0.0, 0.0, 1.0)
    u_right (1.0, 1.0, 1.0, 1.0)

transform grad_guard:
    shader "name.gradient"
    u_left (0.6, 0.6, 0.6, 1.0)
    u_right (1.0, 1.0, 1.0, 1.0)
    
transform grad_king:
    shader "name.gradient"
    u_left (0.0, 0.1, 0.45, 1.0)
    u_right (1.0, 1.0, 1.0, 1.0)
    
transform grad_companion:
    shader "name.gradient"
    u_left (0.7, 0.7, 0.7, 1.0)
    u_right (1.0, 1.0, 1.0, 1.0)

transform grad_kain:
    shader "name.gradient"
    u_left (0.5, 0.0, 0.7, 1.0)
    u_right (1.0, 1.0, 1.0, 1.0)

transform grad_brullo:
    shader "name.gradient"
    u_left (0.35, 0.35, 0.35, 1.0)
    u_right (1.0, 1.0, 1.0, 1.0)

transform grad_xavier:
    shader "name.gradient"
    u_left (0.58, 0.44, 0.86, 1.0)
    u_right (1.0, 1.0, 1.0, 1.0)


transform appear_fade:
    alpha 0.0
    linear 0.35 alpha 1.0   

transform disappear_fade:
    linear 0.35 alpha 0.0   



define c   = Character("Селена",   callback=name_callback, cb_name="селена")
define pr  = Character("Принц Дорін", callback=name_callback, cb_name="дорін")
define g   = Character("Герцог Перрантгон", callback=name_callback, cb_name="перрантгон")
define ka  = Character("Кальтена", callback=name_callback, cb_name="кальтена")
define sh  = Character("Капітан Єстфол", callback=name_callback, cb_name="шаол")
define n   = Character("Нехемія", callback=name_callback, cb_name="нехемія")
define f   = Character("Фаліпа", callback=name_callback, cb_name="фаліпа")
define ke  = Character("Кейн", callback=name_callback, cb_name="кейн")
define b   = Character("Брулло", callback=name_callback, cb_name="брулло")
define ks  = Character("Ксав'єр", callback=name_callback, cb_name="ксав'єр")
define K   = Character("Король", callback=name_callback, cb_name="король")
define gv1 = Character("Гвардієць 1", callback=name_callback, cb_name="гвардієць1")
define gv2 = Character("Гвардієць 2", callback=name_callback, cb_name="гвардієць2")
define spk1 = Character("Спутниця 1", callback=name_callback, cb_name="спутниця1")
define spk2 = Character("Спутниця 2", callback=name_callback, cb_name="спутниця2")
define no   = Character("Нокс",   callback=name_callback, cb_name="нокс")
define pe   = Character("Пелор",   callback=name_callback, cb_name="пелор")
define ve   = Character("Верін",   callback=name_callback, cb_name="верін")
define G   = Character("Королева Георгіна",   callback=name_callback, cb_name="георгіна")


image селена = At("images/Selena/селена.png", sprite_highlight("селена"))
image дорін = At("images/Dorin/Дорін.png",   sprite_highlight("дорін"))
image шаол = At("images/Shaol/Шаол.png", sprite_highlight("шаол"))
image кальтена = At("images/Kaltena/Кальтена.png", sprite_highlight("кальтена"))
image перрантгон = At("images/Perrantgon/Перрантгон.png", sprite_highlight("перрантгон"))
image нехемія = At("images/Nehemia/Нехемія.png", sprite_highlight("нехемія"))
image фаліпа  = At("images/Phalipa/Фаліпа.png", sprite_highlight("фаліпа"))
image кейн   = At("images/Kane/Кейн.png",   sprite_highlight("кейн"))
image король = At("images/King/Король.png",   sprite_highlight("король"))
image спутниця1 = At("images/Companion/Спутниця1.png",   sprite_highlight("спутниця1"))
image спутниця2 = At("images/Companion/Спутниця2.png",   sprite_highlight("спутниця2"))
image гвардієць1   = At("images/Guardsmen/Гвардієць1.png",   sprite_highlight("гвардієць1"))
image гвардієць2  = At("images/Guardsmen/Гвардієць2.png",   sprite_highlight("гвардієць2"))
image брулло  = At("images/Brullo/Брулло.png",   sprite_highlight("брулло"))
image ксавєр  = At("images/Xavier/Ксав'єр.png",   sprite_highlight("ксав'єр"))

style name_grad_common is namebox:
    font "Indira_K.ttf"
    size 40

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"

                if who == "Селена":
                    text who style "name_grad_common" at grad_selena xalign get_char_center(who)

                elif who == "Принц Дорін":
                    text who style "name_grad_common" at grad_dorin xalign get_char_center(who)

                elif who == "Герцог Перрантгон":
                    text who style "name_grad_common" at grad_duke xalign get_char_center(who)

                elif who == "Кальтена":
                    text who style "name_grad_common" at grad_kalt xalign get_char_center(who)

                elif who == "Капітан Єстфол":
                    text who style "name_grad_common" at grad_captain xalign get_char_center(who)

                elif who == "Нехемія":
                    text who style "name_grad_common" at grad_nehemia xalign get_char_center(who)

                elif who == "Гвардієць 1" or who == "Гвардієць 2":
                    text who style "name_grad_common" at grad_guard xalign get_char_center(who)

                elif who == "Фаліпа":
                    text who style "name_grad_common" at grad_falipa xalign get_char_center(who)

                elif who == "Король":
                    text who style "name_grad_common" at grad_king xalign get_char_center(who)

                elif who == "Спутниця 1" or who == "Спутниця 2":
                    text who style "name_grad_common" at grad_companion xalign get_char_center(who)

                elif who == "Кейн":
                    text who style "name_grad_common" at grad_kain xalign get_char_center(who)

                elif who == "Брулло":
                    text who style "name_grad_common" at grad_brullo xalign get_char_center(who)

                elif who == "Ксав'єр":
                    text who style "name_grad_common" at grad_xavier xalign get_char_center(who)

                else:
                    text who style "name_grad_common"

        text what id "what"



label start:
    stop music fadeout 1.0
    scene black
    with fade

    scene expression "images/episodes/ep1.jpg" at scale_to_1080p
    with dissolve

    play sound "audio/Transition.mp3"

    pause 3.0

    scene black
    with dissolve

    scene expression "images/backgrounds/The_corridor.jpg" at scale_to_1080p
    with fade
play music "audio/Neutral.mp3" fadein 2.0
"Коридори палацу здавалися нескінченними. Кам’яні стіни відбивали кожен звук, і навіть тихе клацання кроків лунало, наче удари молота."
"Селену вели вперед. Її руки були скуто, але голова піднята високо — вона не дозволяла собі виглядати зламаною."
"Попри лахміття й сліди копалень на обличчі, у її очах жевріла грізна сила, яка змушувала охоронців відводити погляд."
show шаол at right, size_shaol, appear_fade 
sh "Тримайся рівно. Принц не любить слабкості."
show селена at left, size_selena, appear_fade
c "Я не слабка."
sh "Побачимо."
show селена at left, size_selena, disappear_fade
show шаол at right, size_shaol, disappear_fade
scene expression "images/backgrounds/the throne room.jpg" at scale_to_1080p
"Вони зупинилися перед високими дверима, прикрашеними золотими візерунками. Двері відчинилися, і світло тронної зали залило простір."
"На підвищенні сидів принц Дорін. Його погляд був уважний, але сповнений цікавості — він розглядав ту, про кого чув легенди."
"Поруч стояв герцог Перрантгон, його усмішка була холодною, а очі — пильними, наче він оцінював здобич."
play music "audio/S&D.mp3" fadeout 1.0 fadein 2.0
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Отже, це й є Селена Сардотін."
show селена at left, size_selena, disappear_fade
show дорін at right, disappear_fade 
"Принц кинув короткий погляд на капітана Єстфола."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Я ж наказував привести її в належному вигляді. Чому вона досі в лахмітті?"
show дорін at right, disappear_fade
show шаол at right, size_shaol, appear_fade 
sh "Вона відмовилася. До того ж я хотів привести її до вас якомога швидше."
c "Я не річ, яку можна прикрасити для вашого задоволення."
show селена at left, size_selena, disappear_fade
show шаол at right, size_shaol, disappear_fade 
"Герцог Перрантгон тихо засміявся, але його сміх був більше схожий на шипіння."
show селена at left, size_selena, appear_fade  
show дорін at right, appear_fade 
pr "Герцогу Перрантгону, ви вже зустрічалися з казначеєм Ендов’єра?"
show дорін at right, disappear_fade
show перрантгон at right, appear_fade 
g "…"
show селена at left, size_selena, disappear_fade
show перрантгон at right, disappear_fade 
"На мить його усмішка зникла, і він нахмурився, але все ж кивнув."
show селена at left, size_selena, appear_fade 
show перрантгон at right, appear_fade 
g "Так, Ваша Високість. Я виконаю те, що ви просите."
show селена at left, size_selena, disappear_fade
show перрантгон at right, disappear_fade 
"Перрантгон зробив легкий уклін і, не приховуючи роздратування, покинув залу."
"Коли двері зачинилися, Дорін відкинувся вперед, сперся ліктями на коліна й уважно подивився на Селену."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Ти виглядаєш молодшою, ніж я очікував."
pr "Про тебе розповідають неймовірні історії."
pr "Скажи, як тобі Ендов’єр після такої запаморочливої долі, яку ти мала в Рафтхолі?"
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"«Напищений індик», — подумала Селена."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
c "Неможливо уявити більше щастя."
pr "Після року в копальнях ти не втратила живості. Це дивує. Зазвичай там витримують місяць."
c "Сама дивуюся цій загадці."
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Вона опустила погляд і поправила кайдани, наче це були мереживні рукавички."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "У неї гострий язик, — усміхнувся принц до капітана. — І говорить правильно, не як простий сброд."
c "Сподіваюся, — буркнула Селена."
show дорін at right, disappear_fade 
show шаол at right, size_shaol, appear_fade 
sh "При зверненні до принца додавай «ваше високість»."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена відповіла йому усмішкою й знову повернулася до Доріна. Той засміявся."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Ти знаєш, що тут рабиня. Приговор нічого тебе не навчив?"
c "Копальня вчить лише тримати кирку."
pr "І ти жодного разу не намагалась утекти?"
c "Один раз."
pr "Мені про це не казали."
show дорін at right, disappear_fade
show шаол at right, size_shaol, appear_fade
sh "Через чотири місяці вона спробувала втекти."
c "Це не найкраща частина історії."
show шаол at right, size_shaol, disappear_fade 
show дорін at right, appear_fade 
pr "А яка ж найкраща?"
show дорін at right, disappear_fade
show шаол at right, size_shaol, appear_fade 
sh "Ваше високість, втеча з Ендов’єра — самогубство. Але вона вижила."
c "Так, — тихо сказала Селена."
show шаол at right, size_shaol, disappear_fade 
show дорін at right, appear_fade 
pr "Що ж тобі завадило?"
c "Гілка хруснула під ногою."
show дорін at right, disappear_fade
show шаол at right, size_shaol, appear_fade 
sh "Перед тим вона вбила наглядача й двадцять три стражники. Її перехопили біля стіни."
c "Від моєї шахти до стіни — триста шістдесят три фути. Я рахувала."
sh "Зазвичай втікач не проходить і трьох футів."
show шаол at right, size_shaol, disappear_fade 
show дорін at right, appear_fade 
pr "Тебе могли вбити. Чому ж залишили живою?"
c "Король наказав, щоб я пройшла всі жахи Ендов’єра."
c "Я й не збиралась тікати, — прошепотіла вона."
pr "У тебе багато шрамів?"
show дорін at right, disappear_fade
show селена at left, size_selena, disappear_fade 
"Селена знизала плечима. Принц підійшов ближче."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Тут лише бруд. І запах жахливий!"
c "А як інакше пахнути, якщо я забула, коли востаннє милася? Вибачте… ваше високість."
show дорін at right, disappear_fade
show селена at left, size_selena, disappear_fade 
"Принц обійшов її, розглядаючи. Стражники напружилися."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Я бачу кілька шрамів, але думав, що буде гірше. Це сховають сукні."
c "Сукні?"
pr "У тебе чудові очі. І які ж вони злі!"
show дорін at right, disappear_fade
show селена at left, size_selena, disappear_fade 
"Селена ледь стримувалася, щоб не кинутися на нього. Капітан різко відтягнув її назад."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Полегше! Я не збиралася вбивати принца."
sh "Думай, що кажеш, інакше поверну тебе в копальні!"
c "Не зробиш цього. Бо вам обом від мене щось потрібно. Ви перевіряли мене, чи я не зламалася. Але я жива й при розумі. Тож скажіть, навіщо я тут і що вам від мене треба?"
show селена at left, size_selena, disappear_fade
show шаол at right, size_shaol, disappear_fade
"Принц і капітан переглянулися."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, disappear_fade 
show дорін at right, appear_fade 
pr "Є до тебе одна пропозиція."
c "Слухаю."
show дорін at right, disappear_fade
show селена at left, size_selena, disappear_fade 

#Епізод 2
stop music fadeout 1.0

scene black
with fade

scene expression "images/episodes/ep2.jpg" at scale_to_1080p
with dissolve

play sound "audio/Transition.mp3"

pause 3.0

scene black
with dissolve
scene expression "images/backgrounds/the throne room.jpg" at scale_to_1080p
with fade
play music "audio/S&D.mp3" fadein 2.0
"Принц Дорін повільно підвівся з трону."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Тобі пропонують шанс, Селено Сардотін. Змагання за титул Чемпіона короля."
c "Я чула про це. Двадцять чотири вбивці, злодії, найманці. Один виходить живим. Інші — трупи."
pr "Саме так. Переможець служить королю чотири роки. Потім — повна свобода. Гроші. Земля. Ім’я, яке знову матиме вагу."
show дорін at right, disappear_fade
show селена at left, size_selena, disappear_fade 
"Селена повільно крутила кайдани на зап’ястях."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
c "А якщо я скажу «ні»?"
pr "Тоді завтра на світанку тебе повезуть назад. До Ендов’єра. До тієї самої шахти."
c "Гарно сказано. Ви просто хочете подивитися, як швидко я зламаюся остаточно."
show дорін at right, disappear_fade
show селена at left, size_selena, disappear_fade 
"Дорін усміхнувся — не глузливо, а майже з цікавістю."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Ні. Я хочу побачити, чи ти дійсно та, про кого шепочуться. Та, що вбила двадцять три охоронці за одну ніч. Та, що рахувала кожен фут до стіни."
pr "Ти отримаєш їжу. Гарячу воду щодня. Ліжко. Кімнату з дверима, які зачиняються зсередини. Тренування. Зброю. І — шанс."
show дорін at right, disappear_fade
show селена at left, size_selena, disappear_fade 
"Селена мовчала довго. Потім тихо, майже пошепки:"
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
c "Чотири роки. А якщо я виграю раніше?"
pr "Ні. Чотири роки — обов’язково. Але після них — ти вільна. Я даю слово."
show дорін at right, disappear_fade
show селена at left, size_selena, disappear_fade 
"Вона підняла підборіддя."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
c "Слово принца. Воно багато важить у цьому палаці?"
show дорін at right, disappear_fade
show селена at left, size_selena, disappear_fade 
"Дорін підійшов ближче — настільки, що вона відчула легкий аромат сандалу."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Моє слово важить саме стільки, скільки я захочу."
show дорін at right, disappear_fade
show селена at left, size_selena, disappear_fade 
"Селена дивилася йому прямо в очі. Довго. Потім видихнула."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
c "Гаразд. Я згодна."
show дорін at right, disappear_fade
show селена at left, size_selena, disappear_fade 
"Принц кивнув капітанові."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Відведи її. Нехай помиється. Дай нормальний одяг. І прослідкуй, щоб їй принесли їжу — справжню, не тюремну баланду."
show дорін at right, disappear_fade
show шаол at right, size_shaol, appear_fade 
sh "Так, Ваша Високість."
show шаол at right, size_shaol, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Коли вони вже дійшли до дверей, Селена раптом зупинилася й обернулася."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
c "Принце, якщо я виграю ці змагання… ви точно пошкодуєте, що випустили мене з кайданів."
pr "Можливо. Але я вже пошкодував би, якби не спробував."
show дорін at right, disappear_fade
show селена at left, size_selena, disappear_fade 
"Двері зачинилися з важким стуком."
# комната Селены вечером
scene expression "images/backgrounds/room_night.jpg" at scale_to_1080p
with fade
"Коли Селена нарешті впала на ліжко після зустрічі з принцом, сон не йшов. Тіло горіло від втоми, але біль і збудження не давали заснути."
"Гаряча вода й мило стали справжньою тортурою. Дві кремезні служниці терли її так, ніби мали зішкребти до кісток. Шрами на спині палали вогнем, обличчя здавалося стертим до черепа."
"Шаол зняв кайдани перед миттям. Ключ клацнув, залізо розімкнулося, окови гупнули на підлогу. Але примарні ланцюги залишилися — тепер у повітрі. Селена з насолодою крутила зап’ястями й ворушіла пальцями ніг, попри біль."
"Лежати на справжній перині з шовковими простирадлами було дивно. Під головою — подушка, а не власна рука."
"Шлунок відвик від нормальної їжі. Вечеря — смажена курка — не мала смаку. Після кількох шматочків Селену ледь не вивернуло. Вона вискочила з-за столу, тримаючись за живіт."
"Хотілося наїстися досхочу. Але шлунок розучився. Нічого. У Рафтхолі вона наздожене. Чисте тіло показало правду: форми зникли. Лише кістки, обтягнуті шкірою."
"Селена ледь не заплакала. Перевернулася на спину — шрами знову занили. У дзеркалі — чужа жінка: вилиці гострі, очі запалі, щелепа випирає. Вік не визначити."
"Селена закусила губу. Сльози не допоможуть. Завтра — не шахта, а Рафтхол. Вона буде їсти. Тренуватися. Стане сильною. Переможе всіх. Доведе, що досі — найкраща асасин Адарлану."
"З цими думками вона заснула."
scene expression "images/backgrounds/room_daylight.jpg" at scale_to_1080p
with fade
"Вранці Шаол знайшов її на підлозі, закутану в ковдру."
show шаол at right, size_shaol, appear_fade 
sh "Ей, Сардотін, вставай!"
show шаол at right, size_shaol, disappear_fade 
"Селена буркнула й зарилася в подушку."
show шаол at right, size_shaol, appear_fade 
sh "Чому на підлозі?"
show шаол at right, size_shaol, disappear_fade 
"Вона розплющила одне око. Капітан навіть не коментував її вигляд — чисту, без бруду."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Ліжко незручне."
show шаол at right, size_shaol, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Вона підвелася. Нічна сорочка прикривала худе тіло. Сонячна смуга пробилася крізь штори. Селена простягнула руку — світло торкнулося блідої шкіри. Із того, що каторга не знищила, — вишуканість рухів."
"Вона кинулася до вікна, ледь не зірвавши штори. За склом — сірі гори Ендов’єра, вартові внизу, що ніколи не дивляться в небо."
"Голубувато-сіре небо. Повільні хмари. «Я не буду боятися». Ці слова вперше стали правдою. Селена усміхнулася. Шаол здивовано глянув, але промовчав."

"Служниці заплели їй косу. Одягли в елегантний дорожній костюм — він сховав худорлявість."
"Селена завжди любила тканини: шовк, бархат, атлас, замша, шифон. Стежки, мереживо, тиснення… Коли переможе — купить усе, що захоче."
"Вона простояла біля дзеркала п’ять хвилин, посміхаючись собі. Шаол ледве силоміць вивів її з кімнати."
scene expression "images/backgrounds/Main_courtyard.jpg" at scale_to_1080p
with fade
"По коридорах Селена йшла, пританцьовуючи й заглядаючи у вікна. Але на головному дворі радість згасла."
"Знайомі гори — кольору вибіленої кістки. Печери — входи в шахти. Фігурки каторжників уже працювали. Вони працюватимуть, коли вона поїде. Сьогодні. Завтра. До смерті."
"Живіт скрутило. Селена відвернулася й прискорила крок до каравану."
"Раптом — веселе гавкання. Три чорні собаки — піджарі, мов стріли вискочили назустріч."
"Породисті, з псарні принца. Оббігли Селену. Вона опустилася на коліно, погладила, почухала за вухами. Собаки лизали обличчя й пальці, махаючи тонкими хвостами."

"Біля неї зупинилися чорні, майже ебенові чоботи. Собаки миттєво сіли. Селена підняла погляд — Дорін."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Мої собачки тебе прийняли. Чим ти їх підкупила?"
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Вона похитала головою."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Ти любиш собак?"
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Селена кивнула."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Я удостоюся відповіді голосом, чи ти мовчатимеш увесь шлях?"
c "Ваші питання й так не потребують слів."
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Дорін нахилився й прошепотів:"
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Тоді прийміть мої вибачення, пані Сардотін. Наступного разу придумаю цікавіші запитання."
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Він розвернувся й пішов. Собаки потрусили за ним."

"Настрій зіпсувався. Селена помітила ухмилку Шаола — й захотіла когось розмазати по стіні. Їй підвели кобилу. Селена сіла в сідло. Небо стало ближчим."
"Вчора це було б сном. Ендов’єр позаду. Вона глибоко вдихнула. І тут — клац. Кайдани знову на зап’ястях."
"Шаол прив’язав ланцюг до свого жеребця. Селена уявила, як смикає — і зриває його з сідла."
"Караван: двадцять вершників. Попереду — знаменосці. Потім принц і герцог Перрантгон. За ними — шестеро гвардійців, схожих на кашу."
"Селена вдарила ланцюгом по сідлу. Шаол не ворухнувся."

"Сонце піднялося. Караван рушив. Хлист. Крик позаду. Селена обернулася — нічого не видно. Один із безіменних."
"Вона подумала про шрами на спині. Навіть на свободі вони нагадуватимуть."
#ворота Ендовьера
scene expression "images/backgrounds/Courtyard_entrance.jpg" at scale_to_1080p
with fade
"Ворота. Проїзд крізь товщу стіни — темний, гулкий. Потім зовнішні — з написом Ендов’єр."
"Ворота зачинилися. Пекло позаду. Селена смикнула ланцюг — перевірила. Шаол глянув пильно. Вона насмішкувато знизала плечима й відпустила."
#Лес (The_forest)
scene expression "images/backgrounds/The_forest.jpg" at scale_to_1080p
with fade
"Небо стало чисто-синім. Дорога пішла лісом — Задубілий ліс, межа між Сходом і диким Заходом."
"Легенди про жорстоких нащадків Відьомського королівства. Селена колись убила одну з них — кров текла так само."

"Через кілька годин мовчання Селена заговорила:"
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Кажуть, після перемоги над Вендаліним король піде на західні землі."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Шаол мовчав."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Пустелі, жалюгідні гори. Нудно."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Він стиснув зуби."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Ти й далі мене ігноруватимеш?"

sh "Я не знав, що ігнорую."
c "Скільки тобі років?"
sh "Двадцять два."
c "Молодий! А вже капітан."
sh "А тобі?"
c "Вісімнадцять."
sh "Преступлення — не досягнення."
c "А стати найвідомішою асасинкою — ще й яке!"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Він мовчав."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Хочеш знати, як я це зробила?"
sh "Ні."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена дратувалася. Хотіла або вразити, або розлютити."
"Вона продовжувала:"
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Ти з принцом — близькі друзі?"
sh "Не твоя справа."
c "Знатного роду?"
sh "Достатньо."
c "Герцог?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Мовчанка."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Предводитель Шаол Естфол?"
sh "Не називай мене так. Титулу предводителя в мене немає."
c "Скандал? Тебе позбавили?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Шаол побілів губами."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Ти не вважаєш, що…"
sh "Кляп у рот — чи сама замовкнеш?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Він відвернувся."
#Лес (The_forest_var2)
scene expression "images/backgrounds/The_forest_var 2.jpg" at scale_to_1080p
with fade
"Караван зупинився на галявині. Шаол від’єднав ланцюг, різко смикнув — Селена змушена була зіскочити."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
sh "Привал."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
#Епізод 3
stop music fadeout 1.0

scene black
with fade

scene expression "images/episodes/ep3.jpg" at scale_to_1080p
with dissolve
play sound "audio/Transition.mp3"
pause 3.0
scene black
with dissolve
scene expression "images/backgrounds/The_forest_var 2.jpg" at scale_to_1080p
with fade
play music "audio/S&D.mp3" fadein 2.0
"Селена мотнула головою, відкидаючи з обличчя пасмо волосся, й рушила за капітаном. Якби вона зараз вирішила втекти, починати треба було б із Шаола. "
"Спокуса майнула, але кайдани й озброєні гвардійці стримували сильніше. Усі вони, як і вона, вміли вбивати без роздуму."
#Лес (The_forest_var3)
scene expression "images/backgrounds/The_forest_var 3.jpg" at scale_to_1080p
with fade
"На галявині запалили багаття. Замість сидінь служили стовбури гілок. Собаки принца раділи привалу. Побачивши Селену, вони підбігли, тицьнулися носами й уляглися біля її ніг."
"«Хоч комусь приємне моє товариство», — подумала вона з гіркою усмішкою."
"Шаол довго дивився попереджувально, перш ніж зняти кайдани з рук — і тут же застібнув їх на щиколотках. Селена ледь не поперхнулася, але вдавано байдуже взяла шматок м’яса й повільно жувала."
"Солдати не звертали уваги. Вони їли й балакали. Навколо багаття сиділи Шаол і п’ятеро гвардійців. Принц із герцогом Перрантгоном розташувалися окремо. Дорін виглядав напруженим. Дружби між ними явно не було."
"Коли набридло дивитися на принца, Селена почала розглядати дерева. У лісі панувала тиша. Гончі лише зрідка ворушили вухами. Навіть гвардійці поступово замовкли."
"Серце закалатало. Цей ліс був іншим."
"Листя звисало рубінами. Трава переливалася відтінками. Адарлан спустошив багато земель, але цей куточок залишився недоторканим."
"Їй було вісім, коли Аробінн Хемел знайшов її напівмертву на березі замерзлої річки й привів у вежу на кордоні Адарлану й Террасену. Він навчав її мистецтва асасинів. Потім вони переїхали в Рафтхол."
"У Террасен вона ніколи не поверталася — так велів Аробінн. Та й навіщо? Король Адарлану перетворив її батьківщину на попіл. Але красу рідних земель вона пам’ятала."
"Аробінн не був балакучим, але Селена навчилася розуміти його без слів. Якби вона відмовилася, він не вбив би її — просто віддав би тим, хто міг зробити з нею що завгодно."
"По суті, Аробінн подарував їй нове життя, нове ім’я, нову долю. Восьмирічна дівчинка не уявляла, що скоро її ім’я вимовлятимуть зі страхом."
show гвардієць1 at left, size_guard, appear_fade 
gv1 "Чортів ліс."
show гвардієць2 at right, size_guard, appear_fade 
gv2 "Чим швидше його спалять — тим краще."
show гвардієць1 at left, size_guard, disappear_fade 
show гвардієць2 at right, size_guard, disappear_fade 
"Інші закивали. Селена стиснулася."
show селена at left, size_selena, appear_fade 
c "А чого ви чекали від цього лісу?"
show селена at left, size_selena, disappear_fade 
"Рука Шаола лягла на ефес меча."
show селена at left, size_selena, appear_fade 
c "Це не простий ліс. Це ліс Бранона."
show гвардієць1 at right, size_guard, appear_fade 
gv1 "Батько в дитинстві розповідав казки, ніби тут жили феї. А потім зникли разом із цим поганим народом фе."
show гвардієць1 at right, size_guard, disappear_fade 
show гвардієць2 at right, size_guard, appear_fade 
gv2 "Ми очистили землі від погані!"
c "На вашому місці я б прикусила язика. Король Бранон належав до народу фе. Цей ліс — досі його. Дерева, мабуть, пам’ятають."
show селена at left, size_selena, disappear_fade 
show гвардієць2 at right, size_guard, disappear_fade 
"Солдати зареготали."
show гвардієць1 at right, size_guard, appear_fade 
gv1 "Деревам тоді дві тисячі років!"
show гвардієць1 at right, size_guard, disappear_fade 
show гвардієць2 at right, size_guard, appear_fade 
gv2 "Фе безсмертні."
show гвардієць2 at right, size_guard, disappear_fade 
show гвардієць1 at right, size_guard, appear_fade 
gv1 "А дерева — ні."
show гвардієць1 at right, size_guard, disappear_fade 
show гвардієць2 at right, size_guard, disappear_fade 
"Селена сердито мотнула головою й повернулася до їжі."
show шаол at right, size_shaol, appear_fade 
sh "Ти щось знаєш про цей ліс? (пошепки)"
show шаол at right, size_shaol, disappear_fade 
"Вона відчула підвох. Хоче висміяти при всіх?"
show селена at left, size_selena, appear_fade 
c "Поки Адарлан не прийшов, ліс був пронизаний магією."
show селена at left, size_selena, disappear_fade 
"Він чекав."
show селена at left, size_selena, appear_fade 
c "І все. Більше нічого не знаю."
show селена at left, size_selena, disappear_fade 
"Забава не вдалася. Солдати розчаровано уткнулися в миски."
"Селена збрехала — і Шаол зрозумів. Вона знала багато, але промовчала."
"Адарлан розростався. Королі ненавиділи сусідство з фе. Нинішній король вирішив винищити їх і всю магію. Фе втекли, а магію оголосили казками. Через місяць вона зникла сама."
"Селена пам’ятала запах пожеж — горіли книги, священні місця, маги, провидці, цілителі. Їхні крики снилися ночами. Уцілілих відправили в Ендов’єр — багато померли швидко."
"Магія зникла й у Селени. Залишилися лише спогади. Але втрата магії стала благом — поєднання її навичок і магії давно б її знищило."
"Дим багаття нагадав дитинство. Щоб відігнати спогади, вона зосередилася на їжі."
"Трапеза швидко скінчилася. Шаол знову застібнув кайдани на зап’ястях. Солдати посідали на коней."
"Караван рухався до ночі. Селена більше не розмовляла. Тяжкість у грудях не проходила, аж поки галявина не лишилася далеко позаду."
#tent
scene expression "images/backgrounds/tent.jpg" at scale_to_1080p
with fade
"На нічліг їй поставили маленький шатер, оточили охороною. Кайдани не зняли, але ланцюг тепер тримав гвардієць. Селена провалилася в сон без снів."
"Прокинулася — і не повірила очам. Біля ліжка лежали білі квіточки. На землі — сліди маленьких ніг. Селена швидко затерла сліди, квіти сховала в сумку."
#Лес (The_forest)
scene expression "images/backgrounds/The_forest.jpg" at scale_to_1080p
with fade
"За сніданком і привалом ніхто не згадував фе, але Селена крадькома стежила за обличчями солдатів. Можливо, вони теж щось помітили, але мовчали."
"Вона їхала напружено, тримаючись за луку сідла, вдивляючись у дерева. Подорож на північ тривала вже два тижні. Дні коротшали, ночі холоднішали. Чотири доби йшли під крижаним дощем."
"Все мокре й холодне. Пальці ніг майже не відчувала. Спати лягала, загортаючи ноги в сухі ганчірки. Та одного дня дощі скінчилися."
"У напівдрімоті не відразу помітила принца. Темне волосся майоріло на вітрі. Червоний плащ хвилювався. Біла сорочка, синій камзол із золотом, високі коричневі чоботи, шкіряний пояс. Лише мисливський ніж — занадто всипаний камінням."
"Дорін поравнявся з Шаолом."
show дорін at right, appear_fade 
pr "Їдемо. (кивнув до крутого холму)"
show шаол at left, size_shaol, appear_fade 
sh "Куди?"
pr "Полюбуємося краєвидом. І її візьмемо."
show шаол at left, size_shaol, disappear_fade 
show дорін at right, disappear_fade 
"Селена поперхнулася. «Її»? Як тюк?"
"Шаол виїхав із каравану, різко смикнувши. Коні принца й капітана понесли галопом — її кобила мусила бігти слідом."
#The glass castle day
scene expression "images/backgrounds/The glass castle day.jpg"   at scale_to_1080p
with fade
"У розриві хмар блиснуло сонце. Між деревами з’явився скляний шпиль, потім три, потім ще півдюжини. Кожен прагнув проткнути небо."
"З вершини пагорба відкрився вид на головний шедевр Адарлану — скляний замок Рафтхолу."
"Величезне створіння. Місто зі скляних веж, мостів, сходів, переходів, залів, коридорів. Збудований поверх старого кам’яного замку."
"Селена згадала, як бачила його вперше — вісім років тому, десятирічною. Замок здавався без смаку. Гроші викинуті, таланти марно витрачені."
"Вона перебирала пальцями бірюзовий плащ, боялася порвати чулки й забруднити червоні оксамитові черевички. Але думки були лише про людину, яку вона вбила три дні тому."
show дорін at right, appear_fade 
pr "— Ще одна вежа — і вся громада завалиться."
show дорін at right, disappear_fade 
"Він зупинився праворуч від Шаола. Караван підтягувався."
show дорін at right, appear_fade 
pr "Залишилося кілька миль, але краще їхати при денному світлі. Ночуємо тут."
show шаол at left, size_shaol, appear_fade 
sh "Цікаво, що подумає ваш батько про неї."
pr "Все буде добре, поки вона триматиме рот на замку. Сподіваюся, в батька зараз важливіші справи."
show дорін at right, disappear_fade 
show шаол at left, size_shaol, disappear_fade 
"Принц розвернув коня й поїхав униз."
"Селена не могла відірвати очей від замку. Навіть здалеку він гнітив."
"Гвардійці знайшли місце для табору. Запалили багаття."
show шаол at right, size_shaol, appear_fade 
sh "Про що задумалася? Виглядаєш, ніби їдеш не на свободу, а на шибеницю."
show шаол at right, size_shaol, disappear_fade 
"Селена перебирала пальцями поводдя."
show селена at left, size_selena, appear_fade 
c "Дивно бачити все це."
show шаол at right, size_shaol, appear_fade 
sh "Місто?"
c "Місто, замок, халупи, річку… Я досі не розумію, як це сталося."
sh "Як тебе схопили?"
show шаол at right, size_shaol, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Селена кивнула."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Знать і асасини схожі. Зовні — сила імперії, закони, але таємно знищують одне одного. Так і асасини — кодекс честі, але при нагоді…"
sh "Думаєш, тебе зрадив хтось зі своїх?"
c "Усі знали, що я беру найкращі замовлення й можу просити будь-яку ціну. Хтось хотів моє місце."
sh "Даремно сподівалася на повагу в такій компанії."
c "Я й не сподівалася. Я їм не довіряла. Знала, що ненавидять."
sh "Уявляю, яким пеклом став Ендов’єр."
c "Так. Ендов’єр був пеклом."
show шаол at right, size_shaol, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Він чекав продовження. Селена вирішила — не зашкодить."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Привезли — обрізали волосся, вдягли в брудне ганчір’я, сунули кирку. Рани терли сіллю. Тією самою, що я видобувала. Шкіра не встигала гоїтися. Дякувати ейлуейцям — ночами очищали спину, жертвуючи сном."
show шаол at right, size_shaol, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Шаол мовчав. Лише глянув і зліз із коня."
"Розговорилася… дурна — лаяла себе Селена."
#The glass castle night
scene expression "images/backgrounds/The glass castle night.jpg" at scale_to_1080p
with fade
"Того вечора капітан більше не говорив — лише віддавав накази."
"Селена прокинулася від руки на горлі. Знову сон — вона в загальній могилі Ендов’єра, жива серед мертвих. Чіпляється за слизькі руки й ноги, але трупи тягнуть униз. Кричить — ніхто не чує."
"Вона сіла, обхопивши коліна. Сон. Лише сон. Дихала глибоко. Вдих-видих. Запрокинула голову, упершись підборіддям у коліна."
"Ніч тепла не по сезону — спали під відкритим небом. Замок світився зеленавим пульсуючим світлом над сплячим містом."
"Селена уявила: світ засинає в сяйві замку. Гори піднімаються й руйнуються. Рослини обвивають будинки, ховають місто під листям і колючками. Вона — єдина, хто прокинувся."
"Вона сиділа, закутана в плащ. Переможе в змаганнях. Послужить королю. Зникне. Не думатиме про замки, владарів, асасинів."
"Не правитиме містом. Магія мертва. Фе вигнані або вбиті. Більше ніяких державних справ. Ніяких казок про призначення. Вона з них виросла."

#Епізод 4
stop music fadeout 1.0

scene black
with fade

scene expression "images/episodes/ep4.jpg" at scale_to_1080p
with dissolve

play sound "audio/Transition.mp3"

pause 3.0

scene black
with dissolve
scene expression "images/backgrounds/Raftholl Street1.jpg" at scale_to_1080p
with fade
play music "audio/S&D.mp3" fadein 2.0
"Гінця, надісланого заздалегідь, уже попередили в Рафтхолі: прибув спадкоємний принц. Щойно караван наблизився до замку, залунали привітальні звуки труб. На вітрі тріпотіли малиново-червоні прапори із золотими вивернами."
"Селена їхала попереду Шаола — розодягнена, припудрена, нарум’янена. Без кайданів і ланцюга."
"Вздовж тротуарів тулилися городяни. Усі зачаровано дивилися на спадкоємного принца. Дорін Хавільярд усміхаючись привітно махав рукою."
"Принц, як і Шаол, був у червоному плащі з брошкою королівської печатки на лівому плечі. На акуратному чорному волоссі — золота корона. Він виглядав саме так, як має виглядати спадкоємець престолу."
"Цілу юрбу гарно вбраних молодих городянок чекали саме його появи. Вони розмахували капелюшками, кожна намагалася привернути увагу його високості. Дорін лиш усміхався."
"Селена помітила, як уважно ці дівчата розглядали її намагаючись зрозуміти, що за особа затесалася в свиту принца."
"Вона уявила себе збоку: в найкращому разі — важлива полонянка, яку везуть до замку. Щоб позлити цих дурочок, Селена привітно їм усміхнулася й навіть помахала."
"Раптом пальці Шаола боляче стиснули їй руку."
show селена at left, size_selena, appear_fade 
c "Що таке? (пошепки)"
show шаол at right, size_shaol, appear_fade 
sh "Ти виглядаєш дурно (пошепки)"
c "На мою думку, це вони виглядають дурно. (пошепки)"
sh "Заспокойся й поводься пристойно (пошепки)"
c "Я зараз можу зістрибнути з коня й утекти. (пошепки) — Селена всміхнулася якомусь простакові."
sh "Можеш. Тільки навряд чи далеко втечеш із трьома стрілами в спині."
c "Яка приємна в нас із тобою бесіда."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
#Raftholl_Street2
scene expression "images/backgrounds/Raftholl_Street2.jpg"   at scale_to_1080p
with fade
"Процесія в’їхала в торгову частину міста. Над дахами височів скляний замок — настільки високий, що верхні вежі видно лише задерши голову."
"Далі шлях пролягав набережною Авері. Біля причалів стояли кораблі, всюди валялися сплутані сіті й канати. Матроси голосно перегукувалися — їм було ніколи дивитися на процесію."
"Селена замилувалася парусниками, коли раптом почула знайомий звук хлиста."
"Вона повернула голову. З торгового корабля по сходнях зганяли рабів. Як завжди — скуті спільним ланцюгом, очі в землю, байдужі до всього."
"Такі обличчя вона надивилася в Ендов’єрі досхочу. Більшість — полонені з завойованих країн. Найупертіших карали показово, решту — в ланцюгах на користь королівства."
"У гавані рабів було повно — видавав погляд: у землю чи в небо, ніколи просто перед собою."
"Селені раптом захотілося зістрибнути з коня, кинутися до них і крикнути, що вона не має жодного стосунку до двору спадкоємного принца. Не так давно вона сама була рабинею соляних копалень, і по її спині гуляли батоги наглядачів."
"Можливо, в Ендов’єрі зараз рідні чи друзі цих нещасних. Хотілося сказати: два роки тому вона звільнила майже дві сотні рабів, що належали Предводителеві піратів. Нехай знають — вона не з породи адарланських чудовиськ."
#The_courtyard_of_the_glass_castle
scene expression "images/backgrounds/The_courtyard_of_the_glass_castle.jpg"   at scale_to_1080p
with fade
"Місто відсунулося, і раптом — раніше, ніж їй хотілося — попереду виросли масивні, скляні ворота замку. З обох боків мощеного проходу вишикувалися королівські гвардійці."
"Дорога вивела на широкий внутрішній двір. Ноги затекли — хтось витяг її з сідла й поставив. Скрізь сяяло й виблискувало скло. Слуги швидко повели коней до стайні."
"Селена озирнулася — принц ішов до неї."
show дорін at right, appear_fade 
pr "Подумати тільки: шістсот кімнат, покої для слуг і варти, три сади й садочок для ігор, стайні та всілякі господарські прибудови. Навіщо мені стільки простору?"
show селена at left, size_selena, appear_fade 
c "Не уявляю, як ви спите вночі, коли від смерті вас відділяє лише скляна стіна."
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Вона глянула вгору — й одразу опустила голову. Висоти не боялася, але думка, що під ногами лише скло, стиснула живіт."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Значить, ми з тобою схожі. Хвала богам, я розпорядився відвести тобі покої в кам’яному замку. Не хочу, щоб тобі було незручно."
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Слова можна було сприйняти як витончену насмішку, але Селена не була в становищі, щоб ображатися. Усміхатися принцу розхотілося — вона вдавала, ніби роздивляється масивні вхідні двері."
"Димчасто-червоне скло, обрамлене залізом — наче роззявлена паща чудовиська. Але всередині — камінь. Хто вигадав ідіотську ідею — поверх кам’яного замку будувати скляний?"
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "А ти за дорогу трохи поповнішала. І рум’янець з’явився. Ласкаво просимо до мого дому, Селено Сардотін. Змагання починаються завтра. Капітан Естфол проведе тебе до покоїв."
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Селена розправила плечі — сподіваючись побачити хоч когось із майбутніх суперників. Нікого. Мабуть, ще не приїхали."
"Принц повернувся до Шаола."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Мені треба зустрітися з батьком. Увечері побачимося."
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Забувши про Селену, Дорін пішов до сходів палацу."
# Selena's Room (The Glass Castle)
scene expression "images/backgrounds/Selena's Room (The Glass Castle) Day.jpg"   at scale_to_1080p
with fade
"Спадкоємний принц стримав слово. Покої Селени справді були в кам’яній частині замку. Більші, ніж вона уявляла: спальня з умивальнею й гардеробною, затишна їдальня, кімната для ігор і музикування. Скрізь витончено розставлені кушетки й м’які стільці."
"Переважали два кольори: малиново-червоний і золотий. Спальню прикрашала величезна старовинна шпалера. З балкона відкривався вид на фонтан у саду."
"Все виглядало приємно — окрім стражників унизу."
"Селена нетерпляче чекала, коли Шаол нарешті піде. Поки він водив її кімнатами, вона встигла порахувати вікна"
"Єдиний вхід ретельно охороняли. Караульних — дев’ятеро. У кожного меч, кинджал, арбалет."
"У спальні вона пригнулася, просклизнула до вікна, притиснулася до мармурової стіни й глянула вниз. Караульні, напевно, вже розрядили арбалети й повісили за спину. Зарядити знову — кілька секунд. За цей час вона встигла б заволодіти мечами, перерізати горлянки й зникнути."
"Усміхаючись своїм думкам, Селена почала вивчати сад. Далекий його край межував із садочком для ігор. Вона ще пам’ятала план замку — її поселили в південній частині. Минути садочок — упрешся в кам’яну стіну. А за стіною — річка Авері й… свобода."
"Вона обстежила всі полиці, шухляди, тумбочки, туалетний столик. Зброї, звісно, не було. Навіть камінну кочергу прибрали. Але в нижній шухляді комода знайшла кілька кістяних шпильок, у порожньому кошику для рукоділля — моток мотузки."
"Нема ні голок, ні ножиць."
"Селена перейшла до гардеробної — абсолютно порожньої. Опустилася на коліна, косячи оком на двері, й узялася до справи: обламала голівки шпильок, міцно зв’язала кістяні палички мотузкою."
"Звичайно, це не нагадувало ніж, але гострими краями можна роздерти горло. Селена поскребла пальцем — дрібний осколок уп’явся в мозоль. Якщо встромити в шию караульному — виграєш секунди й заволодієш його зброєю."
"Вона повернулася до спальні. Глянула на ліжко та зітхнула, бажання лягти було сильним, але спочатку справи. Встала на перину, потягнулася й сховала саморобку в складках балдахіна. Сплигнула на підлогу, ще раз оглянула кімнату."
"Перед тим, як привести її сюди, Шаол точно наказав усе обшукати. Цікаво, як скоро йому захочеться нової перевірки?"
"На пальцях підійшла до дверей спальні, прислухалася. Нікого. Перейшла в кімнату для ігор. Біля дальньої стіни — три більярдні киї, на зеленому сукні столу — важкі кулі."
"Селена усміхнулася. Шаол вважав себе передбачливим, але його дії доводили протилежне."
"Вона подолала спокусу сховати кий і кулю. Це відразу викликало б підозру."
"Втомившись, повернулася до спальні й нарешті розтяглася на широкому ліжку і її одразу здолав сон."
"Через годину розбудила служниця: прийшов кравець, треба зняти мірки й показати зразки тканин. Майже всі викликали огиду. Коли Селена спробувала сказати, які кольори їй пасують, кравець лише скривився й відмахнувся."
"Селені відчайдушно захотілося вихопити в цього самовпевненого дурня булавку й устромити в око."
"Після кравця її повели митися. За подорож вона знову обросла брудом майже як в Ендов’єрі. Але здешні служниці поводилися делікатно, терли шрами обережно."
"Потім її трохи підстригли, обробили нігті. У дзеркалі гардеробної Селена задоволено усміхалася."
"Корсаж сукні з довгими рукавами кольору індиго розшитий тонкою золотою ниткою. Зі спини спадала хвилями білосніжна накидка. Волосся укладене локонами, стягнуте пурпуровою стрічкою."
"Але варто згадати, як вона опинилася в цих розкішних покоях — усмішка згасла."
"Невже захисниця короля має виглядати так? Селені раптом став огидний новий наряд. Так виглядають не захисниці, а королівські собачки!"
show фаліпа at right, size_falipa, appear_fade 
f "Як гарно!"
show фаліпа at right, size_falipa, disappear_fade 
"Пролунав позаду жіночий голос. Селена обернулася — й навіть прикусила губу. Рухатися в такому вбранні можна було лише повільно. Особливо заважав туго зашнурований корсаж."
"Перед нею стояла дама років на двадцять старша. Крупна, але струнка. Сукня — витончене поєднання кобальтового й персикового. Ознака королівської служби. Дама вклонилася."
show фаліпа at right, size_falipa, appear_fade 
show селена at left, size_selena, appear_fade 
f "Мене звати Фаліпа Спандель. Я твоя особиста служниця. А ти, мабуть…"
c "Селена Сардотін"
show фаліпа at right, size_falipa, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Очі Фаліпи округлилися."
show фаліпа at right, size_falipa, appear_fade 
f "Раджу нікому не називати свого імені. Я одна його знаю. Мабуть, і твоя охорона теж."
show селена at left, size_selena, appear_fade 
c "А придворним і всім іншим не здасться дивним, що біля моїх дверей стоять вартові?"
show фаліпа at right, size_falipa, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Фаліпа, не звертаючи уваги на гнівні очі Селени, підійшла й почала поправляти складки сукні."
show фаліпа at right, size_falipa, appear_fade 
f "До інших претендентів теж приставлена охорона. Тож вартові біля твоїх дверей нікого не здивують. І не дивись таким поглядом. Коли ти так дивишся — твоє обличчя втрачає всяку привабливість."
show фаліпа at right, size_falipa, disappear_fade 
"Фаліпа простягнула руку, щоб поплескати по щоці, але Селена різко відсмикнулася."
show селена at left, size_selena, appear_fade 
c "Ви з глузду з’їхали? Я асасин, а не придворна дурочка!"
show фаліпа at right, size_falipa, appear_fade 
f "При цьому ти залишаєшся жінкою. І поки тебе передали під мою опіку — поводитимешся як придворна дама."
show фаліпа at right, size_falipa, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Селена здивовано заморгала."
show селена at left, size_selena, appear_fade 
c "А я-то прийняла вас за безсловесну рохлю. Ви з усіма придворними дамами так поводитеся?"
show фаліпа at right, size_falipa, appear_fade 
f "Ні. Усе залежить від того, як вони поводяться зі мною. Тому мене й призначили прислужувати тобі."
c "Тоді вам повинно бути відомо, що мене сюди привезли не для придворних церемоній!"
f "Мені відомо. Але я хочу, щоб і ти знала: не варто виявляти таке явне неповагу до тих, хто ставиться до тебе по-доброму."
show фаліпа at right, size_falipa, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Селена проводила служницю поглядом і хвилину здивовано дивилася на зачинені двері."
"Через деякий час"
#The Glass Throne Room
scene expression "images/backgrounds/The Glass Throne Room.jpg"   at scale_to_1080p
with fade
"Спадкоємний принц Адарлану не кліпаючи дивився на батька й чекав, коли той заговорить. Король мовчки сидів на скляному троні й теж дивився на сина. Іноді Дорін забував, наскільки мало він схожий на батька."
"Інша справа молодший брат Холлін — успадкував і кремезність, і кругле обличчя з гострими очицями. Дорін же — високий, стрункий, ніби народився від іншого батька. А глибокі сині очі — взагалі загадка. Таких не було навіть у матері. Залишалося лише гадати, від якого предка вони дісталися."
show король at right, appear_fade 
K "Ви її привезли?"
show дорін at left, appear_fade 
pr "Поки вона тут то ніякої загрози не становить."
show дорін at left, disappear_fade 
show король at right, disappear_fade 
"Селена Сардотін — претендентка спадкоємного принца. Це нагадувало азартну гру з непередбачуваним результатом. Випробування батьківського терпіння. Сам факт її появи в замку ще нічого не вирішував. Король міг одним словом перекреслити всі задуми сина."
show король at right, appear_fade 
show дорін at left, appear_fade 
K "Ти міркуєш, як усі ті дурні, яких вона вбила. Ця дівчисько вірна лише собі. Якщо з’явиться нагода — без вагань ударить тебе кинджалом у серце."
pr "У такому разі в неї всі шанси виграти ваше змагання. Можна було б і взагалі не влаштовувати ніяких змагань."
K "Ти так говориш, бо боїшся втратити чималу суму грошенят, — відповів король."
show дорін at left, disappear_fade 
show король at right, disappear_fade 
"Він, на щастя, не розумів, що пошуки претендента принц затіяв зовсім з іншою метою. Доріна цікавили не гроші й не виграш. Він ухопився за ці пошуки, щоб вирватися з-під батьківського гніту й на якийсь час відчути себе вільною людиною."
"Дорін зібрався внутрішньо й промовив слова, які повторював подумки весь зворотний шлях з Ендов’єра"
show дорін at left, appear_fade 
show король at right, appear_fade 
pr "Можу ручатися: вона здатна негайно приступити до виконання обов’язків. Її не треба вчити й готувати. Я вже казав вам, батьку: дурно влаштовувати ці змагання."
K "Якщо ти не почнеш думати над своїми словами, я велю віддати тебе цій дівці… для вправ."
pr "І що тоді? Холлін стане спадкоємним принцом?"
K "Я знаю, що кажу, Доріне, і не тобі сумніватися в моїх словах! Ти думаєш, що ця… дівка здатна перемогти. Не забувай: герцог Перрантгон виставив набагато сильнішого претендента — Кейна. Ти вчинив би розумніше, якби знайшов когось йому під стать. Кейн загартований кров’ю й залізом на полях битв."
show дорін at left, disappear_fade 
show король at right, disappear_fade 
"Дорін стиснув кулаки в кишенях — король не помітив."
show дорін at left, appear_fade 
show король at right, appear_fade 
pr "Батьку, а вам не здається, що саме слово «захисник» звучить тут досить дивно, якщо врахувати, що наші «захисники» — не більше ніж злочинці?"
show дорін at left, disappear_fade 
show король at right, disappear_fade 
"Король підвівся з трону й указав на карту на дальній стіні зали для нарад."
show дорін at left, appear_fade 
show король at right, appear_fade 
K "Я король Адарлану, а скоро стану правителем усієї Ерілеї. Ти не смієш сумніватися в моїх рішеннях."
show дорін at left, disappear_fade 
show король at right, disappear_fade 
"Дорін зрозумів — зайшов надто далеко. Існувала тонка межа між синівським свавіллям і відкритим непокорою. Межа, яку спадкоємний принц завжди намагався не переступати. Він поквапливо пробурмотів вибачення."
show дорін at left, appear_fade 
show король at right, appear_fade 
K "Ми воюємо з Вендаліном, мене скрізь оточують вороги. Хто краще виконає мою волю, як не той, кому я дам не лише шанс почати життя заново, а й щедро винагороджу за вірну службу?"
show дорін at left, disappear_fade 
show король at right, disappear_fade 
"Бачачи, що Дорін мовчить, король усміхнувся. Принцу коштувало великих зусиль не здригнутися під пильним поглядом батька."
show дорін at left, appear_fade 
show король at right, appear_fade 
K "Перрантгон сказав, що в дорозі ти поводився гідно."
pr "Маючи такого сторожового пса, як Перрантгон, я й не міг поводитися інакше."
K "Я був змушений послати його з тобою. Не вистачало ще, щоб потім якась селянка голосила біля воріт замку, що ти розбив їй серце."
show дорін at left, disappear_fade 
show король at right, disappear_fade 
"Дорін спалахнув, але погляду не відвів."
show дорін at left, appear_fade 
show король at right, appear_fade 
K "Я надто довго й важко працював, створюючи свою імперію, і не хочу, щоб ти ускладнював мені справу незаконними спадкоємцями. Женися на гідній дівчині, подаруй мені пару онуків, а потім можеш путатися з ким завгодно. Коли сам станеш королем — зрозумієш правоту моїх слів."
pr "Коли я стану королем, я не стверджуватиму, що влада над Террасеном належить мені за сумнівним правом спадкування."
K "Не дурій, Доріне. Розраховуєш задобрити цих бунтівників? Та хоч самоуправління їм запропонуй — вони все одно насадять твою голову на спис і виставлять перед воротами Оринфа."
pr "Можливо, разом із головами моїх незаконних спадкоємців, якщо пощастить їх завести."
show дорін at left, disappear_fade 
show король at right, disappear_fade 
"Король нагородив його їдкою усмішкою."
show дорін at left, appear_fade 
show король at right, appear_fade 
K "Сину мій срібноустий, твоє дитинство давно скінчилося, а ти так і не зрозумів, що слова бувають небезпечніші за знаряддя."
show дорін at left, disappear_fade 
show король at right, disappear_fade 
"Якийсь час батько й син мовчки дивилися один на одного. Потім Дорін заговорив знову:"
show дорін at left, appear_fade 
show король at right, appear_fade 
pr "Я знаю: наші війська несуть втрати, штурмуючи прибережні фортеці Вендаліну. Хіба ви не бачите в цьому знак межі ваших можливостей? Скільки можна грати в бога?"
K "Граю? Я не граю. І те, чим я займаюся, аж ніяк не гра. Якою б милою не здавалася тобі ця дівчисько — вона відьма. Тримайся від неї подалі, зрозумів?"
pr "Ви про кого? Про Селену? Я бачу в ній насамперед вмілого асасина."
K "Вона небезпечна. Не думай, що за визволення з Ендов’єра вона буде тобі вдячна до гробу. У неї на думці лише одне — втекти звідси. А в тобі вона бачить лише засіб для втечі, і не більше."
K "А ще ти не лише мій син, ти насамперед мій підданий а Я — твій правитель. Тож будь ласка, підкоряйся мені, Доріне Хавільярде, інакше тобі це дорого обійдеться."
show дорін at left, disappear_fade 
show король at right, disappear_fade 
"Знаючи, що кожна зайва хвилина в залі лише погіршить становище, спадкоємний принц Адарлану мовчки вклонився й вийшов, переповнений ледь стримуваною люттю."

#Епізод 5
stop music fadeout 1.0

scene black
with fade

scene expression "images/episodes/ep5.jpg" at scale_to_1080p
with dissolve

play sound "audio/Transition.mp3"

pause 3.0

scene black
with dissolve
scene expression "images/backgrounds/Marble Hall.jpg" at scale_to_1080p
with fade
play music "audio/S&D.mp3" fadein 2.0
#Marble Hall
"Селена йшла мармуровим залом разом із Шаолом, який здавалося б ніколи не прибирав руку з ефеса меча."
show селена at left, size_selena, appear_fade 
c "А в сусідній залі є щось цікаве?"
show шаол at right, size_shaol, appear_fade 
sh "Ми ж там уже були. Ми обійшли з тобою всі три сади, бальні зали, кімнати історичних подій і милувалися всіма краєвидами з вікон кам’яного замку. Якщо не хочеш гуляти скляним — більше тут дивитися нічого."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена склала руки на грудях. Капітан клюнув на її хитрість і справді повірив, що їй остогидло сидіти в розкішних покоях і вона хоче, щоб він поводив її замком. Насправді Селена видивлялася нові шляхи для втечі. До того ж їй справді нестерпно було сидіти в своїй розкішній клітці, чекаючи завтрашніх змагань."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Не розумію, чому ти так уперто відмовляєшся прогулятися скляним замком. Внутрішнє оздоблення нічим не відрізняється від цього. Там є на що подивитися. А який вид із вікон!"
c "Тільки ідіот наважиться ходити по скляній будівлі."
sh "Скло там не поступається міцністю каменю й заліза."
c "Сумніваюся. Якщо туди зайде якийсь товстун і тупне посильніше — вся ця пишнота розлетиться на шматки."
sh "Туди заходило чимало товстунів, які звикли важко тупати. Але скляний замок, як бачиш, стоїть цілий."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Сама думка йти по скляній підлозі на висоті кількох поверхів викликала в Селени нудоту."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Скажи, а тут немає якогось звіринця? Чи бібліотеки?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Питання чомусь застало Шаола зненацька. Вони саме опинилися біля масивних, щільно зачинених дверей. Зсередини лунали голоси й мелодійні звуки арфи. Почувши це Селена одразу забула про бібліотеки та звіринці."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "А там що?"
sh "Двір королеви."
c "Двір королеви Георгіни?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Невже цей бравурний капітан не розумів, які цінні відомості щойно вибовкнув? Мабуть, втратив пильність і повірив, ніби в межах замку Селена не становить небезпеки. Дурненький хлопчисько!"
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Так. Там покої королеви Георгіни Хавільярд."
c "А юний принц теж тут?"
sh "Ти про Холліна? Ні, він у гірській школі. Подалі від спокус замку."
c "А він такий же чарівний, як старший брат?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Питання було задане просто так — перевірити щирість капітана. Селена знала: молодший брат ні зовнішністю, ні характером не був схожий на старшого. Кремезний, досить товстий хлопчисько, надмірно розпещений."
"За кілька місяців до того, як Селена потрапила в полон, по столиці поповзли чутки про скандал із молодшим нащадком королівського роду. Кухар, що варив кашу для Холліна Хавільярда, на мить відволікся — їжа підгоріла."
"Ніхто не помітив, і нещасну кашу подали його високості. Хлопчисько так розлютився, що сильно побив ні в чому не винну жінку, яка прислужувала йому за столом. Сім’ї щедро заплатили, але чутки просочилися за межі замку."
"Високородного оболтуса терміново відправили в гірську школу, а новина пішла гуляти адарланськими просторами. Після цього королева Георгіна цілий місяць не виходила зі своїх покоїв."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Холлін увесь у батька" 
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Кілька хвилин вони йшли мовчки. Раптом десь пролунав дивний гуркіт, схожий на вибух. За мить шум повторився."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "А це що ще за кошмарні звуки?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Капітан пройшов крізь двері в сад."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Це б’ють годиники на вежі."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена подолала замішання, і, на щастя, скоро гуркіт припинився."
#Clock Tower
scene expression "images/backgrounds/Clock Tower.jpg"   at scale_to_1080p
with fade
"У цьому саду вони вже були, але з іншого боку, де Часову вежу ховали дерева. Тепер перед Селеною височіла похмура споруда з чорного, з чорнильним відливом, каменю. Усі чотири циферблати прикрашали парні горгульї. Їхні морди застигли в беззвучному крику."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Яка страшна вежа (пошепки)"
sh "У дитинстві я боявся підходити до цієї вежі."
c "Таке швидше побачиш біля адських воріт, а не в саду. І давно її збудували?"
sh "Король наказав звести її незадовго до народження Доріна."
c "Нинішній король? Його батько?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Шаол кивнув."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Навіщо йому тут така жахливість?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Шаол лише махнув рукою приказуючи йти далі."
"Селена й сама рада була швидше піти, але чомусь захотілося ще раз глянути на похмуру споруду. Вона обернулася — і побачила, що скрючений палець однієї з горгулій вказує прямо на неї. Селена могла б заприсягтися, що чудовисько навіть трохи роззявило пащу."
"Поквапливо відвернувшись, вона пішла за Шаолом. Але тут її увагу привернула дивна плитка на доріжці."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "А це що?"
sh "Ти про що?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена кивнула на чорну матову плитку з нерівними краями. На ній був нашкрябаний знак: коло, пересічене вертикаллю. Лінія трохи виступала за межі й закінчувалася гачками — один вгору, інший вниз."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Що це означає?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Капітан підійшов, придивився."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Поняття не маю."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена ще раз глянула на горгулью й сказала"
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Її палець вказує прямо на плитку. Що означає цей символ?"
sh "Він означає… безсоромну витрату мого часу. Якийсь ремісник від нудьги нашкрябав цей знак, коли мостив доріжку. Нічого особливого."
c "А на інших доріжках теж є знаки?"
sh "Якщо поповзаєш — напевно знайдеш."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена не стала випробовувати терпіння капітана й дозволила відвести себе з саду, від похмурої вежі й чудовиськ на циферблатах. Разом із Шаолом вона повернулася в мармурові коридори замку, але ніяк не могла позбутися відчуття, що вирячені очі горгульї досі стежать за нею."
# The door to the library
scene expression "images/backgrounds/The door to the library.jpg"   at scale_to_1080p
with fade
"Далі шлях пролягав повз кухонні приміщення. Далі Шаол швидко завів Селену в інший коридор, де нікого не було. Пройшовши кілька кроків, вона зупинилася як укопана."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "А це що? (пошепки, вказуючи на височенні дубові двері.)"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Очі Селени ще більше округлилися, коли вона помітила двох драконів, що ніби охороняли вхід. Здавалося, дракони ось-ось злетять зі стіни. У них було по чотири лапи — не те що у злих, огидних двоногих виверн, що прикрашали королівський герб."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Бібліотека."
c "Бібліо… А туди можна зайти?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена покосилася на важкі залізні ручки у формі кігтистих лап. Капітан неохоче штовхнув масивні двері."
# The library
scene expression "images/backgrounds/The library.jpg"   at scale_to_1080p
with fade
"На стінах блищали канделябри — в деяких горіла по одній свічці. Підлога — чорно-білий мармуровий шаховий візерунок."
"Рівними рядами стояли столи з червоного дерева й такі ж стільці з червоними оксамитовими спинками. У мармуровому каміні тьмяно світилися тліючі вуглинки. А далі — простір, заповнений височенними шафами."
"До верхніх полиць можна було дістатися лише драбинами. Бібліотека мала другий ярус — туди вели кілька сходів. І скрізь лише книги."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Скільки ж тут книг? (пошепки)"
sh "Коли востаннє хтось рахував — набрався мільйон. Але це було двісті років тому. Думаю, їх навіть більше. Ходять легенди, ніби під цією бібліотекою є інша — і в її тунелях та катакомбах теж зберігаються книги."
c "Більше мільйона? Це правда?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Серце Селени радісно закалатало, і вона усміхнулася."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Мабуть, мені життя не вистачило б, щоб просто перегорнути половину цих книг!"
sh "Ти любиш читати?"
c "А ти хіба ні?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Не чекаючи відповіді, Селена кинулася до найближчих полиць і почала читати назви на корінцях. Усі книги були їй незнайомі. Усміхаючись, вона пішла далі, торкаючись фоліантів. Скоро руки вкрилися пилом — але це їй навіть подобалося."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Я й не знав, що асасини люблять читати. Ти казала, що родом із Террасену. Ти коли-небудь була в Головній бібліотеці Оринфа? Кажуть, вона вдвічі більша за цю, і колись там збирали знання з усього світу."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена неохоче відірвалася від полиць."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Так, це правда. У Головній бібліотеці я була лише раз — зовсім маленькою. Мене привели туди, дорослі пильно стежили, щоб я нічого не порвала й не зіпсувала. Мені лише сказали, що на столах лежать безцінні манускрипти, і заборонили торкатися."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Вона зітхнула. Це було її першим і єдиним відвідуванням Головної бібліотеки. Важко уявити, скільки справжніх скарбів знань загинуло, коли війська Адарлану вторглися на її батьківщину й батько Доріна оголосив магію поза законом."
"Значить, усе, що збиралося століттями, зникло безповоротно? Але в глибині душі Селена тримала надію: Верховні хранителі знань усе ж змогли сховати найцінніші книги й рукописи."
"Після вбивства правителя Террасену й його родини ці мудрі люди зрозуміли: наближаються важкі й небезпечні часи — треба рятувати те, що вдасться. Але коли йдеться про мудрість і знання, накопичені за дві тисячі років, як обрати найголовніше?"
"Селена раптом відчула всередині холод і порожнечу. Бажаючи змінити тему, спитала"
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "А чому біля бібліотеки немає вартових?"
sh "Бо тут нема чого охороняти."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Як же він помилявся! Бібліотекарі були страшніші за асасинів. Ці люди постійно читали, у їхніх головах безперервно бродили думки й народжувалися ідеї. А ідеї, як відомо, — найнебезпечніша зброя."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Скажи, а придворні знають про існування бібліотеки?"
sh "Думаю, так."
c "Тоді чому тут порожньо?"
sh "Просто читання нині… трохи вийшло з моди."
c "Чудово. Тоді мені ніхто не заважатиме."
sh "Ти збираєшся приходити сюди й читати?"
c "Звичайно."
sh "Але ці книги належать королю."
c "Ну то й що? Я ж їх не зіпсую."
sh "Бібліотека — власність короля, і вільний доступ сюди відкритий лише людям знатного походження. Якщо хочеш, щоб тобі дозволили приходити в бібліотеку — потрібен дозвіл від короля чи принца."
c "Дуже сумніваюся, що хтось із них помітить тимчасове зникнення кількох книг. Я ж потім усе поверну на місце."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Шаол позіхнув."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Вже пізно. Я зголоднів."
c "Ну то йди поїж. Я якось сама знайду дорогу."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Капітан королівської гвардії жарту не оцінив. Він щось буркнув і силоміць вивів Селену з бібліотеки."
# Selena's Room (The Glass Castle) Night
scene expression "images/backgrounds/Selena's Room (The Glass Castle) Night.jpg"   at scale_to_1080p
with fade
"Вечеряла вона на самоті. Поки їла, знову думала про втечу й про те, з чого ще зробити зброю. Після їжі почала блукати кімнатами. Цікаво, у якій частині замку розмістили її майбутніх суперників? А якщо їм захочеться почитати — їх пустять у бібліотеку?"
"Селена відчувала втому, але не настільки, щоб завалитися спати — сонце щойно зайшло. Не вийшло з читанням — можна знайти інше заняття. Наприклад, пограти на клавікордах… Селена згадала, як довго її пальці не торкалися клавіш, і скривилася."
"Ні, навіть на самоті її вуха не витримають такого «музикування». Вона перебирала пальцями сукню, а думки поверталися до бібліотеки. Стільки книг, яким нікому читати!"
"І тут її осяяло. Селена скочила й підбігла до письмового столу, узяла пергамент і швидко вмочила скляне перо в чорнило."
# Другой шрифт
"Ваше високосте! Як мені стало відомо, Ваша бібліотека є не бібліотекою в звичному розумінні цього слова, а радше приватним зібранням книг, насолоджуватися якими можете лише Ви та Ваш високошановний батько."
"Оскільки дуже й дуже багато з мільйона книг, що там знаходяться, як мені здалося, ніхто ніколи не брав до рук, прошу Вашого люб’язного дозволу взяти з бібліотеки кілька подібних книг, аби приділити їм заслужену увагу."
"Щиро Ваша Селена Сардотін"
# конец другого шрифта
"Потім відчинила двері своєї розкішної в’язниці й попросила вартових покликати служницю. На щастя, це виявилася не Фаліпа, а миловидна жінка, трохи старша за Селену. Селена вручила їй записку, попросивши негайно передати принцу."
"Через пів години служниця повернулася, несучи стопку книг, поверх яких лежала відповідь Доріна. Селена усміхнулася й почала читати рядки, написані вишуканим почерком."
# Другой шрифт
"Моєму найвірнішому асасину. Надсилаю тобі сім книг із моєї особистої бібліотеки, які я нещодавно прочитав і від яких отримав величезне задоволення. Звичайно, я даю тобі дозвіл брати будь-які книги в бібліотеці замку, але спочатку ти мусиш прочитати ці, аби згодом ми могли обговорити їхній зміст."
"Обіцяю: їхнє читання тебе не втомить, бо я сам терпіти не можу гортати сторінку за сторінкою, позіхаючи над порожніми промовами героїв чи найдовшими й найнуднішими описами пейзажів, оздоблення кімнат тощо. Сподіваюся, тобі сподобаються твори цих письменників, які самі про себе дуже високої думки."
"З увагою, Дорін Хавільярд"
# конец другого шрифта
"Селена засміялася, взяла в служниці книги, подякувала за клопоти. Затишно вляглася у ліжку і почала читати."
# Selena's Room (The Glass Castle) Day
scene expression "images/backgrounds/Selena's Room (The Glass Castle) Day.jpg"   at scale_to_1080p
with fade
"Селену розбудив огидний бій годин на чорній вежі. Крізь сон вона порахувала удари. Полудень. Вона протерла очі й сіла на ліжку. Де ж Шаол? І коли почнуться змагання? А може, тому він і не прийшов її будити, що змагання перенесли на інший день?"
"Селена вистрибнула з ліжка, виглянула за двері, потім подивилася у саду з балкону."
"Думки перервалися появою трьох жінок, що вийшли з-за живої огорожі. Безтурботно балакаючи, вони йшли до фонтану. Жінки були майже її ровесницями, гарно вбрані, та, що йшла посередині — помітно вирізнялася вишуканістю вбрання. Обидві супутниці в скромніших блідо-блакитних сукнях скоріше за все були служницями."
"Красунька в червоному церемонно розправила поділ свого плаття."
# Garden
scene expression "images/backgrounds/Garden.jpg"   at scale_to_1080p
with fade
show кальтена at right, size_kaltena, appear_fade
ka "Дарма я не вдягла біле, Дорін любить біле. Б’юся об заклад: сьогодні всі вирядяться в біле."
show спутниця1 at left, appear_fade 
spk1 "Накажете перевдягнути Вас?"
ka "Ні, мені подобається ця сукня, хоч вона й далеко не нова."
show спутниця1 at left, disappear_fade 
show спутниця2 at left, appear_fade 
spk2 "Але…"
show кальтена at right, size_kaltena, disappear_fade 
show спутниця1 at left, disappear_fade 
show спутниця2 at left, disappear_fade 
"Спробувала розтулити рота друга й одразу замовкла після незадоволеного жесту пані."
"Селена навшпиньках повернулася до перил. Сукня зовсім не здалася їй старою."
show кальтена at right, size_kaltena, appear_fade 
ka "Переконана, Дорін не забариться покликати мене на приватну аудієнцію. Боюся, як би справу не зіпсували настирливі залицяння Перрантгона, але я все одно йому дуже вдячна. Адже це він запросив мене до Рафтхолу. Не здивуюся, якщо моя матуся перевертається в могилі від заздрощів! Але ось хто та…"
show спутниця1 at left, appear_fade 
spk1 "Про кого Ви, пані?"
ka "Про ту дівку, яку принц привіз до Рафтхолу. Кажуть, він їхав за нею через усю Ерілею, а під час урочистої процесії містом вона красувалася поруч із капітаном королівської гвардії. Але це все, що мені відомо. Я навіть імені її не знаю. Втім, чого я хвилююся?"
ka "Ця блудниця — не більше ніж швидкоплинна забава принца. Нехай не розраховує на теплий прийом двору."
show спутниця1 at left, disappear_fade
show селена at left, size_selena, appear_fade 
c "Як вона мене назвала? (подумки)"
show кальтена at right, size_kaltena, disappear_fade 
show спутниця1 at left, disappear_fade
show селена at left, size_selena, disappear_fade 
"Чорноволоса терла скроні й нила"
show кальтена at right, size_kaltena, appear_fade 
ka "Де моє зілля від мігрені? Невже вона знову укладе мене в ліжко? Ходімо!"
show кальтена at right, size_kaltena, disappear_fade
"Вона повернулася до Селени спиною, збираючись іти."
show кальтена at right, size_kaltena, appear_fade
ka "І все одно треба буде розвідати, що за пташку привіз принц. Думаю, я навіть…"
show кальтена at right, size_kaltena, disappear_fade
"Шмяк!"
"Фрейліни так і не дізналися, про що думає їхня примхлива пані. Шум змусив вартових схопитися за арбалети й націлити їх на балкон. Але балкон був порожній… Квітковий горщик, кинутий Селеною, пролетів повз ціль. Що ж, наступного разу вона не промахнеться."
"Забувши про мігрень, чорноволоса відпускала такі соковиті прокльони, що Селена навіть затулила долонею рот, боячись сміхом видати себе. Фрейліни заметушилися, зчищаючи землю зі складок сукні пані та її замшевих черевиків."
show кальтена at right, size_kaltena, appear_fade 
ka "Відчепіться!"
show кальтена at right, size_kaltena, disappear_fade 
"Стражники зробили кам’яні обличчя, намагаючись не видати здивування."
show кальтена at right, size_kaltena, appear_fade 
ka "Геть звідси!"
show кальтена at right, size_kaltena, disappear_fade
# Selena's Room (The Glass Castle) Day
scene expression "images/backgrounds/Selena's Room (The Glass Castle) Day.jpg"   at scale_to_1080p
with fade
"Коли всі троє зникли, «принцева блудниця» вбігла до спальні й через вартових покликала служниць, звелівши принести їй найгарніший наряд, який вони знайдуть."
"Декілька годин потому Селена стояла перед дзеркалом, дивилася на своє відображення й усміхалася. Під корсажем найгарнішого плаття сховано саморобний кинджал, зроблений напередодні з кістяних шпильок."
"Тихо відчинилися двері, і в дзеркалі з’явилося відображення Фаліпи. Селена спробувала надати обличчю байдужий вираз, але служниця одразу зрозуміла, чим займалася колишня в’язниця."
show фаліпа at right, appear_fade, size_falipa 
f "Шкода, що ти… у такому становищі. Тобі б нічого не коштувало вскружити голову якомусь молодому аристократу й вийти за нього. А якщо постаратися — то й його високості."
show селена at left, size_selena, appear_fade 
c "Здається, про це вже пліткують. Вранці я підслухала розмову в саду. Одна особа казала, що принц привіз мене сюди для забави. А я-то думала, весь двір уже знає про це дурне змагання."
f "Наберися терпіння, через тиждень усе забудеться. Варто принцу звернути увагу на якусь жінку — і двір почне шепотітися про неї. І не сприймай ці слова за образу, моя мила. Спадкоємного принца постійно оточують гарні жінки. Тобі має лестити, що тебе приймають за його коханку."
c "А мені це не лестить і не польстить."
f "Краще називатися коханкою, ніж асасином."
show фаліпа at right, disappear_fade, size_falipa 
show селена at left, size_selena, disappear_fade 
"Селена хотіла насупитися, але, глянувши на Фаліпу, засміялася."
show фаліпа at right, appear_fade, size_falipa 
show селена at left, size_selena, appear_fade 
f "Усмішка тобі дуже пасує. Ти стаєш гарнішою. І навіть молодшою — хоч тобі зараз це навряд чи хочеться."
c "Можливо, ви маєте рацію."
show фаліпа at right, disappear_fade, size_falipa
show селена at left, size_selena, disappear_fade 
"Зітхнула Селена й плюхнулася на рожево-ліловий диван."
show фаліпа at right, appear_fade, size_falipa
show селена at left, size_selena, appear_fade 
f "Негайно встань! Ти помнеш сукню."
c "Але я не можу годинами стояти. Особливо в такому взутті, я що, і їсти маю стоячи?"
f "Потерпи ще трохи. Я хочу почути від інших, яка ти прекрасна в цьому вбранні."
c "Хто вам це скаже? Ніхто не знає, що ви моя служниця."
f "Помиляєшся, люба. Усі знають, що мене призначили прислужувати новій коханці принца, яку він привіз до Рафтхолу."
show фаліпа at right, disappear_fade, size_falipa
show селена at left, size_selena, disappear_fade 
"Селена прикусила губу й задумалася. Чи на руку їй це? А як її представлятимуть майбутнім суперникам?"
"З гуркотом відчинилися двері. Почулися знайомі кроки й не менш знайоме бурмотіння крізь зуби. У дзеркалі відобразився задиханий Шаол. Фаліпа проворно зробила реверанс."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Ти…"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Почав він і тут же замовк, роздивляючись нове вбрання Селени. Потім швидко отямився."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Ідемо нагору. Швидко."
c "Я б хотіла знати, куди нам так поспішно треба йти?"
show шаол at right, size_shaol, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Церемонно спитала вона, тріпотіючи віями."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Нічого зі мною кокетничати. Швидше давай!"
show шаол at right, size_shaol, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Він схопив Селену за руку, та потяг її в коридор."
# Hallway
scene expression "images/backgrounds/The_courtyard_of_the_glass_castle.jpg"   at scale_to_1080p
with fade
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Чому ж ти не попередив мене вчора? Я б одяглася раніше — і ми зараз не мчали б щодуху!"
show шаол at right, size_shaol, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Селена важко дихала. Цей клятий корсаж загрожував зламати їй ребра. Піднімаючись довгими сходами, вона однією рукою тримала волосся, боячись зіпсувати зачіску."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "У мене крім тебе клопотів вистачає, добре, що ти хоч здогадалася одягнутися. Але краще б ти нарядилася скромніше. Усе-таки до короля йдемо."
c "До короля?"
sh "Так, до короля. А ти думала, що не побачиш його?"
c "Я думала, що сьогодні мені доведеться змагатися. Так учора сказав принц."
sh "Аудієнція в короля — це офіційний початок змагань, а по-справжньому вони почнуться завтра."
show шаол at right, size_shaol, disappear_fade 
show селена at left, size_selena, disappear_fade 
#The door to the glass throne room  
scene expression "images/backgrounds/The door to the glass throne room.jpg"   at scale_to_1080p
with fade
"Руки Селени налилися свинцем. Вона забула й про садна на ногах, і про ребра, нещадно стиснуті корсажем. Селена з капітаном опинилися на початку довгого коридору. Майбутня королівська захисниця ледь дихала."
"У Селени крутилася голова. Вони прийшли в скляну частину замку — і це Селені дуже не сподобалося. Що завгодно, тільки не стояти в скляному замку."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Ну чому ти не сказав мені раніше?"
sh "Бо король не ділиться зі мною своїми планами. Але нічого, тепер зовсім недовго. Сподіваюся, ти не єдина запізнилася. Коли ввійдеш одразу кланяйся, і низько."
show шаол at right, size_shaol, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Потім, коли піднімеш голову, тримай її високо й не сутулься. Не дивися королю прямо в очі, він цього не терпить. Говори лише тоді, коли він спитає, і до кожної фрази додавай «ваше величносте». І ще: що б ти від нього не почула — ні в якому разі не смій заперечувати."
"Якщо ти йому не сподобаєшся — він накаже тебе повісити."
"У Селени відчайдушно заболів лівий скронь. Навколишній простір раптом став крихким і ненадійним — вони забралися на таку небезпечну висоту… Перед тим, як завернути за ріг, Шаол зупинився."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh"Яка ти бліда сьогодні."
show шаол at right, size_shaol, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Обличчя капітана розпливалося. Селена дихала ротом. Вона ненавиділа сукні з корсажем, королів і скляні замки."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Ну що ти так злякалася? Король — всього лише людина, але стоїть незрівнянно вище й тебе, й мене. Це вимагає особливого до нього ставлення. Аудієнція в короля — чиста формальність. Сьогодні тобі ні з ким не треба битися."
show шаол at right, size_shaol, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Капітан повільно підвів її до дверей. У ту ж саму мить двері розчинилися. Капітан і Селена опинилися в людній залі."

#Епізод 6
stop music fadeout 1.0

scene black
with fade

scene expression "images/episodes/ep6.jpg" at scale_to_1080p
with dissolve

play sound "audio/Transition.mp3"

pause 3.0

scene black
with dissolve
scene expression "images/backgrounds/The Glass Throne Room.jpg"   at scale_to_1080p
with fade
play music "audio/S&D.mp3" fadein 2.0
# The Glass Throne Room
"Відчуття сутінків тривало мить, бо зала освітлювалася самис сонцем через скляні стіни. Селена поквапливо озирнулася, намагаючись уявити розміри зали."
"Капітан зупинився на відкритому просторі перед троном. Селена теж завмерла і низько вклонилася королю."
"Шаол торкнувся її плеча, даючи знак підвестися, але ноги погано слухалися. На щастя, капітан відвів її з центру зали туди, де стояв Дорін. Камзол принца повторював державні кольори королівства — червоний і золотий."
show король at right, appear_fade 
K "Ну що ж, раз усі нарешті зібралися, можна починати"
show король at right, disappear_fade 
"Погляд Селени зупинився на рівні королівських грудей: широких, не особливо м’язистих, затягнутих у чорно-червоний мундир. На плечі короля був накинутий білий хутряний плащ, а на поясі висів меч. Ефес зроблений у вигляді роззявленої пащі виверни."
"Цей меч умів разити наповал. Селена знала про це — і знала його ім’я: Нотунг."
show король at right, appear_fade 
K "Вас зібрали з усієї Ерілеї, щоб ви послужили імперії."
show король at right, disappear_fade 
"Знать, яка обирала претендентів для змагань, майже повністю складалася з зморшкуватих старців, розодягнених і озброєних безглуздими церемоніальними мечами. Поруч стояли їхні обранці різного зросту й статури. Кожного претендента оточували не менше трьох озброєних стражників."
"Двадцять три претенденти — така відстань відділяла Селену від бажаної свободи. Вона спробувала оцінити їхні якості. У деяких — кремезних і широкоплечих — одразу помітила повільність рухів. Інші не поступалися їй швидкістю й спритністю. Трьох привели в залу в кайданах."
"Селена привернула увагу одного з претендентів. Це був досить приємний молодий чоловік. Він був високим і худорлявим. Вона встигла помітити важливу особливість: він спирався на ліву ногу. Незабаром хлопець відвернувся. Здається, його більше цікавили суперники."
"Поруч із герцогом Перрантгоном стояв кремезняк. Здавалося, усі його м’язи відлиті з заліза — що він усіляко підкреслював, бо був у обладунках без рукавів. Селена скривилася. Такі кулачища могли запросто проламати кінський череп. Не сказати, щоб у нього була огидна фізіономія."
"Швидше навпаки: рівна засмага додавала обличчю деякої привабливості. Але Селені не сподобалася його манера триматися, а чорні очиці й випираючі білі зуби викликали огиду."
"Тим часом король продовжував"
show король at right, appear_fade 
K "Кожному з вас доведеться змагатися за почесний титул мого захисника."
show король at right, disappear_fade 
"Селені стало гидко. Яке лицемірство — називати захисниками безжальних убивць! Чи зможе вона служити королю, виконуючи його накази? Вона нервово ковтнула. Доведеться. Іншого вибору немає."
show король at right, appear_fade 
K "Змагання триватимуть тринадцять тижнів. Удень вам належить наполегливо вправлятися, а наприкінці кожного тижня вас чекають випробування. І щоразу найслабші будуть виключатися з подальшої боротьби."
show король at right, disappear_fade 
"Двадцять чотири претенденти й усього тринадцять тижнів. Селену здивував такий розклад часу."
"Ніби відчувши її питання, король пояснив"
show король at right, appear_fade 
K " Випробування будуть нелегкими — як і підготовка до них. Можливо, хтось із вас не доживе до кінця змагань. Якщо ми вважатимемо за потрібне — ускладнимо випробування, щоб відсіяти непридатних."
K "І врахуйте: якщо хтось із вас наважиться виявити лінощі чи недбалість, якщо чимось мені не догодите — негайно повернетеся в ті смердючі нори, звідки вас витягли. На третій тиждень нового року, після святкування Ільмаса, четверо, що залишилися, зійдуться в поєдинках."
K "Двох, що вижили, чекає завершальний бій, результат якого остаточно вирішить, кому дістанеться титул королівського захисника. Хоча при дворі й знають про якесь змагання, затіяне моїми найближчими друзями й радниками подробиці триматимуться в таємниці до названого мною часу."
K "Проболтаєтеся хоч одним словом — підете на вогнище. Вам зрозумілі мої слова?"
show король at right, disappear_fade 
"Селена кивнула важкою головою. Їй не вистачить часу, щоб перемогти суперників. Одне випробування на тиждень. Або більше, якщо одному королю здасться замало."
show король at right, appear_fade 
K "Тоді я хочу почути ваші відповіді! Хіба ви не відчуваєте вдячності за даровану вам рідкісну можливість відзначитися? Хіба вам не хочеться подякувати своєму королю й заявити про вашу вірність йому?"
show король at right, disappear_fade 
"Селена вперлася очима в підлогу й пробурмотіла"
show селена at left, size_selena, appear_fade 
c "Дякую вам, ваше величносте, за виявлену мені милість."
show селена at left, size_selena, disappear_fade 
"Її слова потонули в гудінні голосів інших претендентів."
show король at right, appear_fade 
K "Я думаю — нас чекають тринадцять дуже веселих тижнів. Говорю кожному з вас: покажи свої найкращі якості, доведи, що гідний бути моїм захисником — і ти пізнаєш усю глибину моєї щедрості."
show король at right, disappear_fade 
"На завоювання свободи в Селени залишалося трохи більше трьох місяців."
show король at right, appear_fade 
K "Державні справи вимагають мого від’їзду зі столиці, я поїду наступного тижня й повернуся не раніше поєдинків між чотирма, що залишилися."
K " Але не думайте, що я перестану стежити за вами. Мені доповідатимуть про кожен ваш крок, і якщо я дізнаюся про найменші порушення чи якісь там випадковості… покарання неминуче."
show король at right, disappear_fade 
"Претенденти знову закивали."
show дорін at right, appear_fade 
pr "Якщо ви закінчили, покірно прошу дозволити мені видалитися."
show дорін at right, disappear_fade 
"Селена інстинктивно повернулася до принца, дивуючись його зухвалості. Дорін вклонився батькові й кивнув мовчазним радникам. Король поквапливо махнув рукою, навіть не глянувши на сина. Підморгнувши Шаолу, спадкоємний принц покинув залу."
show король at right, appear_fade 
K " Питання є?"
show король at right, disappear_fade 
"Сам його тон підказував, що будь-яке, навіть найневинніше питання може коштувати відправки на шибеницю. Претенденти мовчали. Знать — теж."
show король at right, appear_fade 
K "Ну, раз питань немає, дозволяю всім розійтися. І пам’ятайте: вас зібрали тут, аби примножити мою славу й славу моєї імперії. А тепер — ідіть. Усі геть."
show король at right, disappear_fade 
# Hallway
scene expression "images/backgrounds/Hallway.jpg"   at scale_to_1080p
with fade
"Селена й Шаол мовчки йшли коридором, поспішаючи якнайшвидше віддалитися від претендентів і їхніх покровителів. З кожним кроком до Селени поверталося життя й упевненість у собі. Лише коли вони завернули за ріг, Шаол полегшено зітхнув."
show селена at left, size_selena, appear_fade 
c "Хоч раз тобі вдалося тримати язик за зубами."
show дорін at right, appear_fade 
pr "Зате якими переконливими були її поклони й кивки"
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Пролунав поруч голос. Біля стіни стояв усміхнений Дорін."
show шаол at right, size_shaol, appear_fade 
sh "Що ви тут робите?"
show дорін at left, appear_fade 
pr "Вас чекав, більше нічого"
sh "Увечері у вас вечеря, не забули?"
pr "До вечора ще купа часу, а зараз я хочу поговорити з моєю захисницею, хочу вибачитися за батьківську грубість."
show дорін at left, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Згадавши, як учора він кокетував із придворною дамою, Селена старалася дивитися просто перед собою. Спадкоємний принц пішов ліворуч від Шаола."
"Він обернувся й, переконавшись, що за ними ніхто не стежить і продовжив"
show дорін at right, appear_fade 
pr "Думаю, Шаол не став присвячувати тебе в наш задум раніше часу. Перед королівською аудієнцією це було б дещо ризиковано."
show селена at left, size_selena, appear_fade
c "Який ще задум?"
pr "Задум стосується твоєї особи. Ніхто не повинен знати твого справжнього імені. Якщо твої суперники хоч трохи пронюхають про Адарланського асасина — це тобі тільки зашкодить."
c "І хто ж я насправді, якщо не безжальна вбивця?"
pr "Для всіх у замку ти — Ліліана Гордена. Твоя мати померла, а батько — успішний торговець із Бельхевена. Ти єдина спадкоємиця його стану. Але в розумної й благопристойної дівчини, якою ти є, є й темна сторона, яку ти до пори до часу вміло приховувала."
pr "Справа в тому, що ночами ти… крала коштовності. Я зустрів тебе цього літа в Бельхевені, куди приїхав відпочити. Ти намагалася мене обікрасти, але мені сподобалися твої задатки, і я не став розголошувати цю історію."
pr "Однак твій батько випадково дізнався про твої нічні забави й від гріха подалі спровадив тебе з Бельхевена в містечко поблизу Ендов’єра. Коли король вирішив влаштувати змагання, я спеціально поїхав за тобою й привіз сюди як мою претендентку."
pr "Такий основний сюжет. Недостаючі подробиці можеш придумати сама."
c "Ну у вас і фантазія! Зробити мене… крадійкою коштовностей!"
pr "Скажи, а відведені покої тебе влаштовують?"
c "Дуже приємні кімнатки,"
pr "Дуже приємні кімнатки? Може, мені варто було поселити мою захисницю в просторіших апартаментах?"
c "Якщо вже ви так на цьому наполягаєте…"
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Дорін усміхнувся."
show дорін at right, appear_fade 
show селена at left, size_selena, appear_fade 
pr "Радий, що споглядання твоїх майбутніх суперників не позбавило тебе зухвалості. До речі, як тобі Кейн?"
c "Спитайте у Перрантгона, чим він годує свого улюбленця, і нехай мені готують таку ж їжу."
show дорін at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Дорін хотів почути серйозну оцінку."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
c "Що вам сказати, ваше високосте? Такі гіганти, як Кейн, не відрізняються ні швидкістю, ні особливою спритністю. Їхня головна властивість — сила. Він цілком може прихлопнути мене одним ударом, але для цього йому спочатку треба мене спіймати."
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Селена швидко глянула на капітана, думаючи, що той почне заперечувати. Але Дорін його випередив"
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Що ж, твої думки збіглися з моїми. А що ти скажеш про інших? Побачила серед них гідних суперників? У декого з них досить погана репутація."
c "Інші здалися мені досить жалюгідними."
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Селена збрехала. Принц усміхнувся ще ширше."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Б’юся об заклад: вони й не підозрюють, що поразку їм завдасть дівчина."
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Селена не сприйняла його слова всерйоз і навіть хотіла спитати, чи не навчався він у дитинстві мистецтву говорити компліменти. Але поставити це питання їй завадила якась дама, що несподівано опинилася на їхньому шляху."
show кальтена at right, size_kaltena, appear_fade 
ka "Ваше високосте! Який сюрприз!"
show кальтена at right, size_kaltena, disappear_fade 
"Вигукнула дама, роблячи глибокий реверанс. Глянувши на неї, Селена одразу впізнала свою ранкову мішень, у яку запустила квітковий горщик. За цей час дама встигла змінити червоне плаття на біле з золотою вишивкою."
"Щодо несподіванки — це вона прибрехала. Швидше за все, знала, що принц проходитиме тут."
show дорін at right, appear_fade 
pr "Добрий день, пані Кальтена"
show дорін at right, disappear_fade 
show кальтена at right, size_kaltena, appear_fade 
ka "Я щойно від її величності. Королева бажає вас бачити. Я сказала їй, що його високість перебуває на королівській аудієнції й тому…"
show кальтена at right, size_kaltena, disappear_fade 
show дорін at right, appear_fade 
pr "Пробачте, пані Кальтена. Я ж ще не познайомив вас зі своєю супутницею."
show дорін at right, disappear_fade 
"Дама помітно здригнулася."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
c "«Зовсім як кінь, якого огріли батогом» (подумки)"
pr "Дозвольте вам представити пані Ліліану Гордену. Пані Ліліана, дозвольте вам представити пані Кальтену Ромпір."
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Найбільше Селені зараз хотілося повернутися й піти, але вона змусила себе усміхнутися й зробити реверанс. Кальтена у відповідь вклонилася, сяючи золотими візерунками на сукні."
show селена at left, size_selena, appear_fade 
show дорін at right, appear_fade 
pr "Пані Ліліана родом із Бельхевена. Вона лише вчора приїхала до столиці."
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Кальтена окинула Селену швидким, оцінюючим поглядом і ніби забула про її існування."
show кальтена at right, size_kaltena, appear_fade 
ka "Ваше високосте, довго ми ще зможемо насолоджуватися вашою присутністю в замку? А то ж чоловіки обожнюють зникати, змушуючи нас, бідних жінок, нудьгувати."
show кальтена at right, size_kaltena, disappear_fade 
show дорін at right, appear_fade 
pr "Думаю, найближчі кілька років я нікуди не поїду."
show дорін at right, disappear_fade 
show кальтена at right, size_kaltena, appear_fade 
ka "Кілька років? Який чудовий жарт, ваше високосте. А якщо це не жарт ви робите нам по-справжньому королівський подарунок."
show кальтена at right, size_kaltena, disappear_fade 
show дорін at right, appear_fade 
pr "До речі, пані Ліліана й капітан Естфол — давні й дуже близькі друзі. Боюся, я їм встигну намозолити очі."
show дорін at right, disappear_fade 
show кальтена at right, size_kaltena, appear_fade 
ka "Намозолити очі? Для нас усіх — велике щастя перебувати у вашому товаристві. А дозвольте спитати, ваше високосте: наше товариство вас не втомлює?"
show кальтена at right, size_kaltena, disappear_fade 
"Все це було сказано грайливим тоном, але під грайливістю ховалося роздратування. Напевно, Кальтена щиро вважала, що центром уваги в замку буде вона."
show дорін at right, appear_fade 
pr "Не знаю, як ви, а от пані Ліліана встигла втомитися від мого товариства. Навіть не знаю, хто з нас за час довгої дороги більше втомився один від одного."
show дорін at right, disappear_fade 
show кальтена at right, size_kaltena, appear_fade 
ka "Де ви знайшли таке приголомшливе плаття? – промуркотіла Кальтена, зрозумівши, що далі виявляти зневагу до Селени не в її інтересах."
show кальтена at right, size_kaltena, disappear_fade 
show дорін at right, appear_fade 
pr "Я наказав його пошити для пані Ліліани."
show дорін at right, disappear_fade 
"Він переглянувся з Селеною — і в очах обох відбилося однакове намірення. Селена відчула, що в них із принцом є один спільний ворог."
show дорін at right, appear_fade 
pr "Пошито точно за міркою, тому так чудово сидить. Правда, пані Кальтена?"
show дорін at right, disappear_fade 
"Кальтена стиснула губи, але одразу змусила себе усміхнутися якнайщиріше."
show кальтена at right, size_kaltena, appear_fade 
ka "Я зачарована. Ось тільки… цей непримітний відтінок… він підсилює природну блідість шкіри."
show кальтена at right, size_kaltena, disappear_fade 
show дорін at right, appear_fade 
pr "До речі, батько пані Ліліани надзвичайно пишається тим, що в його доньки така бліда шкіра. Дуже велика рідкість для уродженців Бельхевена."
show селена at left, size_selena, appear_fade 
c "Ваше високосте, ви мене вгоняєте в фарбу. У порівнянні з пані Кальтеною я просто бліда копія."
show селена at left, size_selena, disappear_fade 
show дорін at right, disappear_fade 
"Кальтена струснула головою."
show кальтена at right, size_kaltena, appear_fade 
ka "Ви дуже добрі."
show кальтена at right, size_kaltena, disappear_fade 
"Принц переминався з ноги на ногу."
show дорін at right, appear_fade 
pr "Ви казали, королева бажає мене бачити? Тоді поспішу до неї."
show дорін at right, disappear_fade 
"Він ввічливо уклонився й пішов у бік покоїв королеви."
show шаол at right, size_shaol, appear_fade 
sh "Нам теж треба йти. Пані Кальтена, вас провести?"
show шаол at right, size_shaol, disappear_fade 
"Пропозиція була нещирою — і капітан навіть не приховував цього."
show кальтена at right, size_kaltena, appear_fade 
ka "Ні, – сухо відповіла Кальтена, припинивши гру в чемність. – У мене зустріч з його світлістю, герцогом Перрантгоном. Пані Ліліана, сподіваюся, ми з вами ще побачимося. Нам із вами неодмінно варто подружитися."
show кальтена at right, size_kaltena, disappear_fade 
"Вимовляючи ці слова, Кальтена пильно стежила за Селеною."
show селена at left, size_selena, appear_fade 
c "Звичайно."
show селена at left, size_selena, disappear_fade 
"Кальтена пішла. Селена з капітаном навмисне йшли повільно, чекаючи, поки звук кроків Кальтени остаточно змовкне."
show шаол at right, size_shaol, appear_fade 
sh "Ну як, зачарована видовищем?"
show селена at left, size_selena, appear_fade 
c "Незвичайно."
sh "Я помітив, у вас із Доріном однакове почуття гумору."
c "А уявляєш, раптом ми з ним станемо близькими друзями, а тобі доведеться в’янути на самоті."
sh "Дорін воліє сходитися з жінками більш знатного походження й більш гарними."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена різко повернулася до нього, і капітан усміхнувся"
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Скільки ж у тобі самозадоволення, «пані Ліліана»!"
c "Просто я ненавиджу дамочок на кшталт цієї Кальтени! Вони так відчайдушно борються за чоловічу увагу, що готові зраджувати найкращих подруг і ламати життя іншим. І ми ще стверджуємо, що чоловічі мізки не годяться для мислення! Принаймні чоловіки пряміші й цілеспрямованіші."
sh "Кажуть, батько Кальтени за багатством не поступається королю. Тому-то Перрантгон так і витанцьовує навколо неї. Уявляєш, вона прибула в замок не верхи, не в кареті, а в паланкіні розміром із селянську хату, якщо не більше. Її несли майже двісті миль."
c "Яка нісенітниця."
sh "Мені шкода її слуг."
c "А мені шкода її батька!"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Вони обидва засміялися, не помітивши, що за розмовою дійшли до покоїв Селени."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Ти сьогодні снідав? Я не встигла."
sh "Мене чекають важливі справи. Треба підготувати супровід для короля."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена відчинила двері, але все ще дивилася на Шаола. Усмішка знову осяяла його обличчя."
"З покоїв смачно пахло і в Селени потекли слинки."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Коли ти встиг?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Шаол похитав головою"
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Я тут ні до чого. Найкращий асасин Адарлану не повинна чекати, поки їй приготують їжу."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Відійшовши на кілька кроків, капітан зупинився й, обернувшись до неї, сказав"
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Не забувай: завтра — справжній початок змагань. Хоч ти й стверджуєш, що не особливо потребуєш вправ, виспатися тобі треба обов’язково."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена витріщила очі й шумно грюкнула дверима. Але потім, за обідом, вона згадувала слова капітана й наспівувала собі під ніс."
"На наступний день"
# Selena's Room (The Glass Castle) Day
scene expression "images/backgrounds/Selena's Room (The Glass Castle) Day.jpg"   at scale_to_1080p
with fade
"Селені здавалося, що вона ледве встигла задрімати, як раптом чиясь рука торкнулася її плеча. Їй хотілося спати, і ранкове сонце, що хлинуло крізь розсунуті штори, зовсім її не порадувало. Селена щось буркнула крізь сон, збираючись повернутися на інший бік."
show шаол at right, size_shaol, appear_fade 
sh "Вставай!"
show шаол at right, size_shaol, disappear_fade 
"Звичайно, це був Шаол."
"Селена юркнула під ковдру, вкрившись із головою, але Шаол скинув її на підлогу."
show селена at left, size_selena, appear_fade 
c "Мені холодно!"
show селена at left, size_selena, disappear_fade 
"Зараз її не хвилювало, що треба перемогти понад двадцять претендентів, а часу обмаль. Вона відчайдушно хотіла спати. І чому спадкоємний принц не витягнув її з Ендов’єра парою місяців раніше?"
"Тоді б у неї вистачило часу відпочити й відновити сили. Чи Доріан поїхав за нею щойно, як дізнався про майбутні змагання?"
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Вставай. Ти безжально витрачаєш мій час."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Шаол витягнув з-під її голови подушку"
"Бурмочучи лайку, вона підповзла до краю ліжка й простягнула руку, торкаючись підлоги."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Будь ласка, принеси мені туфлі. Підлога зовсім крижана."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"У відповідь Шаол щось буркнув, але не зрушив з місця. Селена зробила кілька кроків по холодній підлозі туди, де підошвами догори валялися туфлі. Потім пішла до їдальні. Там її вже чекав сніданок."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Їж більше. Через годину почнуться змагання."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Ніби молода ведмедиця, вона плюхнулася на стілець. Вилки, ложки, ложечки — і жодного ножа. Довелося ткнути виделкою в цілий шматок смаженої ковбаси."
"Шаол не сів за стіл, а залишився стояти в дверях."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Дозволь спитати, де це ти встигла так втомитися?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена залпом допила гранатовий сік і промокнула рот серветкою, згадавши, що ще якийсь місяць тому вона витиралася брудним рукавом."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Читала майже до четвертої ранку. Я послала записку його високості, спитавши дозволу брати книги з королівської бібліотеки. Він мені дозволив і передав зі служницею сім книг зі своєї особистої бібліотеки, наказавши спочатку прочитати їх."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Шаол недовіриво похитав головою."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Хто тобі дозволив слати принцу записки?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена задоволено усміхнулася й узялася за шинку, яку, за браком ножа, теж довелося розковирювати виделкою."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Невже й на це треба питати дозволу? Подумаєш, усього-на-всього записка. Принц міг би на неї й не відповісти. І потім, я ж його захисниця. У поводженні зі мною він не зобов’язаний брати приклад із тебе."
sh "Але ти ж асасин."
c "І що? Тому мені заборонено читати книги? А якщо я назвуся злодійкою коштовностей — ти станеш ставитися до мене з більшою люб’язністю?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена зачерпнула кашу, спробувала й додала в сірувату масу чотири ложки тростинного цукру. Зараз вона думала тільки про суперників. Дійсно чи треба побоюватися лише Кейна? Щоб прогнати тривожні думки, Селена переключилася на розглядання чорного мундира Шаола."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Тебе що, зобов’язують постійно ходити в формі? Невже тобі не хочеться одягнутися по-іншому?"
sh "Поспішай."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Їй раптом розхотілося їсти. Вона відштовхнула тарілку з кашею."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Тоді я мушу перевдягнутися."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена озирнулася на двері, щоб покликати Фаліпу, потім передумала."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Я ж мушу знати, яким буде сьогоднішнє змагання. Раптом не так наряджуся. Від одягу багато залежить."
sh "Так я сам нічого не знаю. Подробиць мені не повідомляли."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена скочила, збираючись іти до гардеробної. Капітан покликав служницю."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Одягни пані в штани й блузу. Вибери ті, що посвободніше. І накидка зверху."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Служниця мовчки пройшла до гардеробної. Селена — слідом."
"Через кілька хвилин Селена з’явилася вже одягнена й хмуро оглянула свій наряд."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Я виглядаю як опудало. Ну що це за балахон? Я просто тону в цих штанях. І блуза на мені телімпається."
sh "Досить нити. Там взагалі ніхто на це не подивиться."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
# Hallway2
scene expression "images/backgrounds/Hallway2.jpg"   at scale_to_1080p
with fade
"Капітан відчинив двері в коридор. Караульні тут же витяглися по стійці «струнко»."
"У коридорах замку було по-ранковому холодно. Шаол провів Селену повз казарми. Караульні, одягнені в шкіряні й металеві обладунки, салютували їм обом. Крізь відчинені двері Селена побачила простору кімнату, де гвардійці снідали."
# Training room
scene expression "images/backgrounds/Training room.jpg"   at scale_to_1080p
with fade
"Шлях закінчився на першому поверсі. Зала, куди вони нарешті прийшли, не поступалася розмірами головній бальній залі. Верхню галерею тут підтримували ряди колон. Чорно-білі плитки підлоги нагадували гігантську шахівницю."
"Скляні двері до самої стелі займали майже всю стіну — вони були відчинені. За ними починався сад, і звідти дув холодний вітер, змушуючи тріпотіти напівпрозорі завіси. У залі вже зібралися майже всі претенденти."
"Не гаючи часу, вони вправлялися — але не між собою, а з наставниками. Швидше за все, наставників для них обирали ті самі, хто обирав і їх. Гвардійці пильно стежили за кожним претендентом."
"Коли Селена з’явилася в залі, ніхто й не глянув на неї — якщо не рахувати сіроокого хлопця, що запам’ятався їй учора. Він злегка усміхнувся їй і продовжив стріляти з лука по мішені. Усі стріли з лякаючою точністю потрапляли в самісінький центр."
"Селена уважно розглядала стійку зі зброєю."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Думаєш, я схоплюся за булаву? У таку ранню годину?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Шаол знизав плечима. Тим часом у залу увійшли ще шестеро гвардійців і приєдналися до своїх товаришів. Усі стражники були з оголеними мечами."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Ці приставлені стежити за тобою. Раджу не намагатися влаштувати якусь дурницю.(пошепки)"
c "Ти, здається, забув, що я — злодійка коштовностей."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена зупинилася біля стійки зі зброєю. Охорона охороною, але все одно безглуздо виставляти в залі стільки зброї. Мечі основні й полегшені (для лівої руки), сокири, луки, списи, мисливські кинджали, булави, піки, метальні ножі, дубинки…"
"Улюбленою зброєю Селени були невеликі кинджали з вузьким лезом, але вона вміла тримати в руках усе, що тут знаходилося. Вона оглянула залу й постаралася приховати презирливу гримасу."
"Як і вчора, більшість претендентів не здавалися їй серйозними суперниками. І тут краєчком ока вона побачила, як у залу входить Кейн."
"Він з’явився в супроводі двох караульних і кремезного чоловіка, вкритого шрамами. Напевно, це був його наставник. Селена розправила плечі. Кейн ішов прямо до неї. Його товсті губи розпливалися в усмішці."
show кейн at right, appear_fade 
ke "Доброго ранку"
show кейн at right, disappear_fade 
"Темні очі Кейна ковзнули по її фігурі, потім зупинилися на обличчі."
show кейн at right, appear_fade 
ke "А я думав, ти вже втекла додому."
show кейн at right, disappear_fade 
"Селена теж усміхнулася — але не розтуляючи губ."
show селена at left, size_selena, appear_fade 
c "Навіщо ж мені додому, якщо забава тільки починається?"
show селена at left, size_selena, disappear_fade 
"Розправитися з ним було зовсім просто. Груди м’язів її не лякали. Достатньо зробити різкий поворот, схопити Кейна за шию й точним ударом збити з ніг, щоб він ткнувся обличчям у підлогу. Всередині в неї кипіла справжня лють. Шаол уловив її стан."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Свій запал прибережи для змагань (пошепки)"
c "Я вб’ю його (пошепки)"
sh "Нічого подібного. Навіть не намагайся. Якщо варта не прихлопне тебе на місці — повернення в Ендов’єр тобі забезпечене. Не розумію, чим він тобі так противний. Звичайний верзила з королівської армії. Краще доживися поєдинку з ним і не витрачай сили на ненависть."
c "Велике спасибі за щедро виявлену турботу про мене."
sh "Це так, підказка з боку."
c "Усе одно приємно."
sh "Прийми ще одну підказку: займися тим, заради чого я тебе сюди привів. Вибери собі щось."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Кінчиком меча Шаол указав на стійку зі зброєю."
"Селена мовчки розв’язала шнурки плаща й скинула його на підлогу."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Я хочу переконатися, що всі твої хвалькуваті заяви відповідають дійсності."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Це вже не було підказкою. Це була відверта насмішка. Гаразд, із Кейном вона встигне розібратися. Селена вже уявила, як цього верзилу ховають у безіменній могилі… А Шаол… вона покаже йому, на що здатна. Нехай тоді бере свої слова назад."
"Уся зброя була чудової якості. Леза мечів, клинків і кинджалів приємно блищали на ранковому сонці. Селену зараз займало тільки одне: знайти відповідну зброю, здатну максимально зіпсувати посмішку капітана."
"У Селени калатало серце. Як давно вона не тримала в руках зброї! Її пальці пробували гостроту лез і перевіряли зручність ефесів."
"Її однаково приваблювали мисливський кинджал і вишукана рапіра з химерно прикрашеною гардою. Рапіра мала довге лезо — це дозволяло з безпечної відстані вдарити капітана прямо в груди."
"Селена вибрала рапіру. Лезо відгукнулося мелодійним дзвоном. Зручна зброя, сильна й легка. Як дивно: за обідом їй не дають навіть тупих ножів для масла, а тут… Чи його величність і його високість сподіваються на пильність і спритність своїх гвардійців?"
"Шаол кинув свій плащ поверх її плаща, залишившись у чорній форменій сорочці."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "До бар’єру!"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Сказав він, витягаючи меч. Шаол став в оборонну позу. Селена скривилася."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "А може, ти спочатку покажеш мені, що до чого?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Досить голосно спитала Селена, граючись рапірою. Її пальці насолоджувалися прохолодою ефеса."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Я ж цілий рік проторчала в Ендов’єрі. Там недовго всі навички забути."
sh "Я пам’ятаю, скількох ти вбила, коли намагалася втекти. Сумніваюся, що ти втратила навички."
c "Убивала я не благородною зброєю, а звичайною киркою. Кому череп розколола, кому живіт розполосувала."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Усмішка Селени ставала все хижіше. На щастя, ніхто з претендентів не чув її слів. Усі, крім Шаола, забули про її присутність."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Якщо ти прирівнюєш грубу розправу з наглядачами до мистецтва поєдинку… якою ж твоя манера бою, капітане Естфоле?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Для більшого ефекту Селена приклала ліву руку до серця й заплющила очі."
"Капітан королівської гвардії проричав і зробив випад."
"Селена чекала цього. Почувши легкий скрип каблуків капітанських чобіт, вона миттєво розплющила очі й парирувала удар. Метал зіткнувся з металом. Ноги Селени приросли до підлоги. Скрегіт зброї подіяв на неї сильніше, ніж сам удар."
"Капітан завдав другого удару — і Селена легко його відбила. У неї нили руки, що відвикли тримати зброю, і все ж вона не пропустила жодного капітанського випаду."
"Бій на мечах подібний до танцю. І в танцях, і в поєдинку за одними рухами неодмінно мають іти інші — інакше зіб’єшся."
"Але якщо, танцюючи, можна весело балакати з партнером і встигати озиратися по боках — тут ти мовчки стежиш за його мечем, забувши про навколишній світ. Претенденти, караульні й уся зала перестали існувати, злившись в узор тіней і сонячних плям."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Добре. Навіть дуже добре."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Ті самі слова могла б сказати й Селена. Капітан був дуже хорошим противником. Набагато кращим, ніж вона думала. Проте говорити йому про це вона не збиралася."
"І знову метал ударився об метал. Капітан був сильнішим. Селена стиснула зуби, щоб устояти й не дати себе відтіснити. Але при всій своїй силі Шаол поступався дівчині в швидкості."
"Селена відступила й зробила фальшивий випад, що змінився вишуканим піруетом. Капітана це застало зненацька — і він ледве встиг парирувати удар."
"Вона продовжувала наступати. Її рука з рапірою то здіймалася вгору, то стрімко опускалася. Їй навіть подобався тупий біль у плечі. Біль посилювався щоразу, коли леза рапіри й меча стикалися."
"Селена насолоджувалася цією грою й ще деякий час дражнила капітана. Шаол спробував збентежити її, завдавши несподіваного удару на рівні обличчя. Його випад лише розлютив Селену. Вона різко вскинула лікоть, змусивши капітана опустити руку."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Коли б’єшся зі мною, рекомендую пам’ятати одну мою особливість."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Важко дихаючи, кинув їй капітан. В його золотисто-карих очах грало сонце."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Яку ж?"
sh "Я не програю."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Шаол усміхнувся їй — і перш ніж до Селени дійшов сенс його слів, щось врізалося їй у ногу й… Тріумф змінився подивом. Ще через секунду Селена опинилася на мармуровій підлозі. Рапіра вислизнула з її пальців. Кінчик меча Шаола застиг над серцем Селени."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Я виграв."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Вона підвелася на ліктях."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Ти підставив мені підніжку. Це не можна вважати перемогою."
sh "Але не я зараз лежу на підлозі, і меч спрямований не в моє серце."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"З вух Селени ніби вишибли пробки. Навколо вправлялися, сопіли й пихтіли претенденти, наповнюючи залу дзвоном і скреготом зброї. Усім було не до неї. Усім, крім Кейна. Той широко усміхався. Від образи й безсилля Селена оскалила зуби."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Навички в тебе є. Але багато твоїх рухів зовсім розхристані."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена повернулася до нього й нагородила сердитим поглядом."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
c "Мені це ніколи не заважало успішно вбивати."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Шаол усміхнувся й кінчиком меча вказав на стійку зі зброєю, дозволяючи Селені підвестися."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Вибери собі іншу зброю. Хочеться подивитися, як ти нею володієш. І зроби так, щоб я спітнів. Прошу тебе."
c "Ти вдосталь спітнієш, коли я живцем здеру з тебе шкіру й позбавлю зору."
sh "Мені подобається твій настрій."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена, не думаючи, витягла зі стійки пару мисливських кинджалів."
show селена at left, size_selena, appear_fade 
c "«Мої давні друзі» (подумки)"
show селена at left, size_selena, disappear_fade 

#Епізод 7
stop music fadeout 1.0
scene black
with fade
scene expression "images/episodes/ep7.jpg" at scale_to_1080p
with dissolve
play sound "audio/Transition.mp3"
pause 3.0
scene black
with dissolve
scene expression "images/backgrounds/Training room.jpg"   at scale_to_1080p
with fade
play music "audio/S&D.mp3" fadein 2.0
"Селена вже збиралася кинутися з кинджалами на капітана, коли раптом пролунали гучні удари списа об підлогу. Чийсь гучний голос вимагав тиші. Селена обернулася й побачила кремезного лисого чоловіка."
show брулло at right, appear_fade 
b "Підійдіть ближче, у мене до всіх вас розмова."
show брулло at right, disappear_fade 
"Селена запитально глянула на Шаола. Той кивнув, забрав у неї зброю, після чого вони приєдналися до інших претендентів, що оточили новоприбулого."
show брулло at right, appear_fade 
b "Я Теодас Брулло, головний королівський зброяр і суддя цих змагань. Як ви чули вчора, король надовго виїжджає з Рафтхолу. Тож вирішувати, хто з вас гідний залишатися претендентом на титул королівського захисника, буду я. І робитиму це після кожного випробування. Його величність дав мені таке право."
b "Усе, що ви мали знати про змагання, король вам учора вже повідомив, але вас, звичайно, так і кортить побільше дізнатися один про одного."
show брулло at right, disappear_fade 
"М’ясистий палець королівського зброяра ткнув у бік Кейна."
show брулло at right, appear_fade 
b "От ти. Назви своє ім’я, чим займався і звідки родом. І говори правду. Я ж знаю: серед вас немає ні пекарів, ні лудильників."
show брулло at right, disappear_fade 
"Кейн знову заусміхався."
show кейн at left, appear_fade 
show брулло at right, appear_fade 
ke "Моє ім’я Кейн. Солдат королівської армії. Родом із Білокличих гір."
show кейн at left, disappear_fade 
show брулло at right, disappear_fade 
"Він не брехав. Селена чула, що жителі тих глухих місць вирізняються особливою жорстокістю. Коли адарланське панування дотягнулося й туди, білокличники піднімали бунт за бунтом. Що б сказали родичі Кейна, якби дізналися, де він зараз? Подумавши про це, Селена стиснула зуби. А що б про неї сказали жителі Террасену?"
"Брулло, судячи з усього, це анітрохи не хвилювало. Він навіть не удостоїв Кейна кивком і вказав на іншого чоловіка, що стояв поруч із білокличником."
show брулло at right, appear_fade 
b "А ти?"
show брулло at right, disappear_fade 
"Худорлявий чоловік із рідким світлим волоссям для чогось озирнувся по боках, потім усміхнувся."
show ксавєр at left, appear_fade 
show брулло at right, appear_fade 
ks "Ксав’єр Форул, головний злодій Мелісанди."
show ксавєр at left, disappear_fade 
show брулло at right, disappear_fade 
"Головною перевагою Ксав’єра була надзвичайна худорба, що дозволяла йому легко пролізати в найвужчу щілину. Здається, він не брехав."
"Опитування тривало. Окрім Кейна, на титул королівського захисника претендували ще шестеро бувалих солдатів."
"Було ще троє злодіїв, серед них сіроокий Нокс Оен, про якого Селена раніше щось чула й який цілий ранок розсилав їй променисті усмішки. Серед претендентів опинилися й троє найманців."
"Двох убивць вважали настільки небезпечними, що навіть тут, серед щільної охорони, тримали в кайданах. Ім’я першого було невиразним, зате прізвисько змусило Селену здригнутися. Окоїд. Вигляд у нього був цілком звичайний: волосся бурого кольору, засмагла шкіра, середній зріст."
"Селена з усіх сил старалася не дивитися на його понівечений шрамами рот. Ім’я другого вона запам’ятала: Нід. Три роки він орудував під прізвиськом Коса. Коса була його улюбленим знаряддям, за допомогою якого він катував і знущався з жертв, «скосячи» шматки їхніх тіл. Дивно, що обох злочинців досі не стратили."
"Але, судячи зі смаглявої шкіри, ці красені кілька років провели на каторзі під сонцем Калакулли, що лежала південніше Ендов’єра."
"Потім настала черга двох понівечених шрамами мовчазних чоловіків середнього віку. Ці приїхали здалеку, за рекомендацією якогось тамтешнього воєначальника. Після них ішли п’ятеро асасинів."
"Імена перших чотирьох Селена одразу забула: довготелесого хлопця з презирливим поглядом, квадратного верзили з приплюснутим лобом, жалюгідного коротунчика й ухмилястого горбоносого ідіота. Вони навіть не входили до гільдії асасинів. Втім, Аробінн Хемел їх би туди й не взяв."
"Можливо, згадана четвірка й володіла зносними навичками, але в них не було витонченості, яку Аробінн виховував у своїх учнів. Про всяк випадок Селена запам’ятала їхні обличчя, але четвірка й близько не стояла з Мовчазними — асасинами, що жили серед барханів Червоної пустелі."
"Її увагу привернув п’ятий асасин, на прізвисько Могила. Худорлявий, невисокий, але з обличчям, яке, побачивши раз, ніколи не захочеш побачити знову. Сюди його привели в кайданах. Кайдани зняли лише після солідного словесного внушення, зробленого п’ятіркою гвардійців, що його охороняли."
show брулло at right, appear_fade 
b "Ну а ти хто будеш?"
show селена at left, size_selena, appear_fade 
c "Ліліана Гордена, крадійка коштовностей із Бельхевена."
show брулло at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Кілька чоловіків презирливо хмикнули. Селена прикусила губу. Знали б вони, хто вона насправді — у них би миттєво відбило бажання сміятися."
show брулло at right, appear_fade 
b "Гаразд. Даю вам п’ять хвилин, щоб поставити зброю на місце й перевести дух після поєдинків. А потім усі відправляться бігати, аби я бачив, наскільки ви витривалі. Бігтимуть усі. Ваше перше випробування через п’ять днів."
show брулло at right, disappear_fade 
"Претенденти розійшлися. Селена ловила уривки розмов між ними та їхніми наставниками. Кожен називав тих, кого вважав найнебезпечнішими супротивниками. Хтось остерігався Кейна. Кілька разів вона чула ім’я Могили. Крадійку коштовностей із Бельхевена ніхто не злякався."
"Шаол стояв поруч, розсіяно поглядаючи на претендентів."
show селена at left, size_selena, appear_fade 
c"Я цілих вісім років заробляла собі ім’я й ще рік промучилася в Ендов’єрі. Якщо мені знову доведеться називати себе якоюсь крадійкою коштовностей…"
show шаол at right, size_shaol, appear_fade 
sh "Ти нею назвешся."
c "А знаєш, як принизливо виставляти себе нікчемною злодійкою з глухого куточка?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Шаол змерив її поглядом."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
sh "Невже в тобі стільки гордині?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена спалахнула, але капітан не дав їй заперечити."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
sh "Даремно я влаштував із тобою поєдинок. Ти вмієш битися, але через мене ти витратила сили. Я не знав, що Брулло змусить вас бігати. На щастя, ніхто на тебе й уваги не звернув. І хочеш знати чому?"
sh "Тому що для них ти — гарненька дівчинка, а не серйозна суперниця. Подумаєш, маленька злодійка з крихітного містечка! Поспостерігай за ними. Хіба хтось зараз дивиться на тебе? Хіба оцінюють твою силу? Ні. Тому що ніхто тебе й за суперницю не вважає."
c "Саме так! І це мене ображає!"
sh "Насправді тобі радіти треба. На мою думку, у твоєму ремеслі дуже цінується непомітність. І тому протягом усіх тижнів ти триматимешся тихіше води, нижче трави. Жодних витівок. Ти мусиш перебувати в золотій середині, де ніхто не зверне на тебе уваги."
sh "Нехай якомога довше вважають, що ти для них ніяка не загроза. І нехай зосереджують усю свою увагу на тому, щоб позбутися більших, сильніших і швидших претендентів на кшталт Кейна."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена сопіла, як маленька дівчинка, якій дуже не хочеться визнавати правоту дорослих."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
sh "Твоє головне завдання — виграти час. Нехай одного прекрасного ранку вони прокинуться й дізнаються, що ти їхня суперниця. Це стане твоєю помстою."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade
"Шаол простягнув руку й повів її в сад."
#Garden2
scene expression "images/backgrounds/Garden2.jpg"   at scale_to_1080p
with fade
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
sh "Що скажеш у відповідь на мої слова, пані Ліліана Гордена?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена усміхнулася приймаючи його руку"
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Що в мене є власна голова на плечах, але в умі тобі, капітане, не відмовиш. Ти настільки кмітливий, що я, мабуть, подарую тобі якийсь із коштовних камінців. Сьогодні вночі я думаю трохи розважитися й обчистити її величність."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Шаол стримано засміявся і вони пішли до місця змагань із бігу."
#Running competition
scene expression "images/backgrounds/Running competition.jpg"   at scale_to_1080p
with fade
"У легенях Селени палав вогонь. Ноги налилися свинцем, але вона вперто продовжувала бігти, тримаючись у середині натовпу претендентів. Брулло, Шаол, наставники й три дюжини гвардійців рухалися верхи, супроводжуючи бігунів."
"Декого, включно з Могилою, Нідом і Окоїдом, змусили бігти на довгому ланцюгу. Але зараз Селену найбільше дивувало, що верзила Кейн біжить попереду, відірвавшись від усіх ярдів на десять."
"Досягнувши повороту, Кейн рушив у зворотний бік — до замку. Решта, ніби пташина зграя, поспішила за ним. Головне — дихати рівно; на рівному диханні можна бігти дуже довго. Нехай усі стежать за Кейном. Їй нема потреби перемагати в цьому змаганні."
"Дерева розступилися показуючи широку арку. Там був кінець шляху. У Селени крутилася голова, але вона не сміла розсіювати увагу."
"Вона не одразу відчула, що забіг закінчився. Ті, хто біг разом із нею, переходили на крок, ловлячи ротом повітря. Їй хотілося повалитися на землю, але вона знала, що цього робити не можна. Треба іти й заспокоювати дихання, навіть якщо перед очима продовжують танцювати зірки."
show брулло at right, appear_fade 
b "Добре, випийте води й переведіть дух. Потім продовжимо вправи."
show брулло at right, disappear_fade 
"Крізь танець зірок Селена побачила Шаола. Вона пішла до нього, потім в бік найближчих кущів."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
sh "Ти куди?"
c "Я, коли бігла, впустила там перстень," 
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Збрехала Селена, з усіх сил зображуючи дурочку, засмучену втратою прикраси."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Я навіть знаю, де це було. Але нічого, я зараз знайду."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Не чекаючи його дозволу, Селена майже бігом попрямувала до чагарника. Сховавшись у заростях, Селена почула важкий тупіт відставшого бігуна й, трохи звернувши, забралася в саму гущавину. Там вона впала на коліна і її вивернуло."
"Прийшовши до тями, Селена встала, тримаючись за кущ, і попленталася на галявину. Там її вже чекав Шаол."
#Selena's Room (The Glass Castle) Cloudy
scene expression "images/backgrounds/Selena's Room (The Glass Castle) Cloudy.jpg"   at scale_to_1080p
with fade
"У полудень Брулло оголосив, що на сьогодні вправи закінчено. Селена звіряче зголодніла й буквально накинулася на їжу. У розпалі трапези двері їдальні широко розчинилися."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Навіщо пожалував?"
sh "Зайшов тебе провідати."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Капітан сів навпроти неї. Він встиг помитися й перевдягнутися. Підсунувши до себе страву із шматочками сьомги, Шаол майже все перекладав собі на тарілку. Побачивши це, Селена скривилася."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
sh "Ти що, не любиш сьомгу?"
c "Терпіти не можу рибу. Я швидше помру з голоду, ніж доторкнуся до неї."
sh "Дивно."
c "Чому?"
sh "Та тому що ти зараз пахнеш, як ця сьомга."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Такої відповіді Селена не чекала. Вона навіть розтулила рота. Шаол докірливо похитав головою."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
sh "Б’єшся ти добре, а от манери в тебе жахливі."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена думала, що капітан згадає випадок у кущах, але Шаол мовчав."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Коли мені хочеться, я можу поводитися й як придворна дама."
sh "Нехай тобі хочеться цього постійно."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Порадив Шаол і, трохи помовчавши, спитав"
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
sh "Як тобі твоя тимчасова свобода?"
c "Звичайно, зараз моє становище краще, ніж у підземних норах Ендов’єра. І навіть якщо я замкнена в межах цих кімнат у мене є книги. Навряд чи ти це зрозумієш."
sh "Чому ж? Нехай у мене не стільки часу на читання, як у вас із Доріном, але я теж дуже люблю читати."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена смачно хруснула яблуком."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "І які ж книги ти любиш?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Шаол назвав."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
c "Ого! Вони справді одні з найкращих. А що ще ти читав?"
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Cпитала здивована Селена. Розмова про літературу захопила їх обох і тривала б далі, але годинник на башні пробив першу годину дня, і капітан змінив тему"
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
sh "Решта дня — твоя. Розпоряджайся часом, як побажаєш."
c "А ти куди відправишся? Знову по невідкладних королівських справах?"
sh "Ні. Я маю намір дати відпочинок рукам, ногам і легеням."
c "Якщо зберешся читати прочитай щось цікаве. Буде про що поговорити."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Капітан встав і повів носом."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
sh "Я сподіваюся, що до того моменту, коли нам буде про що поговорити, ти зберешся помитися."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Коли за Шаолом зачинилися двері, Селена покликала служницю й попросила нагріти води. Їй хотілося якнайшвидше помитися, а потім сісти на балконі й читати."

scene expression "images/backgrounds/Selena's Room (The Glass Castle) Cloudy.jpg"   at scale_to_1080p
with fade
"Наступного ранку Шаолу вже не довелося будити Селену. Увійшовши до її спальні, капітан застав колишню в’язницю Ендов’єра за дивним заняттям. Селена підтягувалася, вхопившись за дверний карниз і прагнучи дістати його підборіддям. Ці вправи тривали вже цілу годину. У Селени тремтіли руки, і кожен новий підхід давався їй дедалі важче."
"Поява Шаола не змусила Селену зупинитися. Вона підтягнулася ще кілька разів, усміхаючись йому крізь стиснуті зуби. На її здивування, у відповідь капітан теж усміхнувся."
#Hallway2
scene expression "images/backgrounds/Hallway2.jpg"   at scale_to_1080p
with fade
"Того дня вибухнула сильна злива. Ні про яке змагання в бігу не могло бути й мови — і претендентів відпустили раніше. Потім злива вщухла так само раптово, як і почалася. Шаол запропонував Селені прогулятися садами. Капітан не був налаштований на розмову, але вона все одно раділа прогулянці. Їй набридло замкнутий простір кімнат."
"Селена вбралася в нову шовкову бузкову сукню з блідо-рожевими мереживами, розшитими перлинними бусинками. Вона пройшла разом із капітаном зовсім небагато, коли, завернувши за ріг, ледь не зіткнулася з Кальтеною Ромпір. На щастя, та була не сама і її супутниця, ейлуейська жінка, одразу привернула увагу Селени."
"Висока, худорлява незнайомка вирізнялася досконалими лініями тіла й таким же досконалим обличчям. Біла вільна сукня лише підкреслювала смаглявість її шкіри"
"На голові в неї був тонкий золотий обруч із підвісками. Жінку супроводжували двоє охоронців, озброєних до зубів ейлуейськими кривими мечами й кинджалами. Ця жінка була ейлуейською принцесою."
show кальтена at right, size_kaltena, appear_fade 
show нехемія at left, appear_fade 
ka "Добрий день, капітане Шаоле"
show кальтена at right, size_kaltena, disappear_fade 
show нехемія at left, disappear_fade 
"Кальтена присіла в реверансі. Чоловік середнього зросту, що йшов поруч із нею очевидно радник, судячи з чорно-червоного одягу,— стримано вклонився."
"Ейлуейська принцеса завмерла. Її карі очі з помітною тривогою дивилися на Селену й її супутника. Селена усміхнулася. Принцеса зробила крок ближче — від чого її охоронці напружилися."
"Кальтена нашвидку сховала невдоволення, викликане несподіваною зустріччю."
show кальтена at right, size_kaltena, appear_fade 
show нехемія at left, appear_fade 
ka "Дозвольте представити вам її королівське високість принцесу Нехемію Ітгер з Ейлуе."
show кальтена at right, size_kaltena, disappear_fade 
show нехемія at left, disappear_fade 
"Шаол низько вклонився. Принцеса відповіла легким кивком. Селена вже чула ім’я цієї жінки. В Ендов’єрі раби-ейлуейці з захопленням розповідали про красу й сміливість Нехемії. Її називали «світлом Ейлуе». Раби вірили, що одного дня принцеса визволить їх із неволі."
"А коли вона зійде на престол Ейлуе, король Адарлану отримає грізну противницю, яка покладе край його пануванню над її рідною країною. Захопленим шепітом вони розповідали Селені, що принцеса допомагає повстанським групам, які ховаються в різних куточках Ейлуе, постачаючи їм припаси й передаючи відомості про наміри адарланських загарбників."
"Але що змусило цю хоробру принцесу приїхати сюди?"
show кальтена at right, size_kaltena, appear_fade 
show селена at left, size_selena, appear_fade 
ka "Познайомтеся з пані Ліліаною"
show кальтена at right, size_kaltena, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Селена зробила найглибший реверанс, на який тільки була здатна."
show селена at left, size_selena, appear_fade 
show нехемія at right, appear_fade 
c "Ласкаво просимо до Рафтхолу, ваше високість (ейлуейською)"
show селена at left, size_selena, disappear_fade 
show нехемія at right, disappear_fade 
"Принцеса Нехемія заусміхалася. Охоронці здивовано витріщилися на Селену. Радник розплився в усмішці, витираючи спітнілий лоб."
show селена at left, size_selena, appear_fade 
show нехемія at right, appear_fade 
c"«Якщо Нехемія збиралася в Рафтхол — чому не поїхала в нашому каравані? Нам було б по дорозі. І чому навколо неї крутиться ця Кальтена?» (подумки)"
n "Дякую вам"
c "Уявляю, який довгий шлях ви подолали. Ваша високість прибули сьогодні? (ейлуейською)"
show селена at left, size_selena, disappear_fade 
show нехемія at right, disappear_fade 
"Охоронці переглянулися. Принцеса злегка підняла брови. Рідко хто з північан умів говорити ейлуейською."
show селена at left, size_selena, appear_fade 
show нехемія at right, appear_fade 
n "Так, я приїхала тільки сьогодні. Королева одразу приставила до мене ось цю… (ейлуейською)"
show селена at left, size_selena, disappear_fade 
show нехемія at right, disappear_fade 
"Вона злегка кивнула в бік Кальтени."
show селена at left, size_selena, appear_fade 
show нехемія at right, appear_fade 
n "І дала в супровід двоногого хробака. (ейлуейською)"
show селена at left, size_selena, disappear_fade 
show нехемія at right, disappear_fade 
"Радник, який не знав ейлуейської, дурнувато усміхався й без кінця витирав піт великою носовою хусткою. Можливо, він розумів, що Нехемія становить загрозу королівству. Тоді навіщо її привезли в замок?"
"Щоб не засміятися, Селена затиснула язик між зубами й сказала"
show селена at left, size_selena, appear_fade 
show нехемія at right, appear_fade 
c "Здається, двоногому хробаку трохи не по собі. (ейлуейською)"
show селена at left, size_selena, disappear_fade 
show нехемія at right, disappear_fade 
"Її й досі розбирав сміх. Щоб його погасити, Селена змінила тему."
show селена at left, size_selena, appear_fade 
show нехемія at right, appear_fade 
c "Як вам замок? (ейлуейською)"
n "Більш дурнуватої споруди я ще не бачила. Я б віддала перевагу замок із піску. (ейлуейською)"
show селена at left, size_selena, disappear_fade 
show нехемія at right, disappear_fade 
"Шаол дивився на них із подивом. Чим же ця чужоземка так полонила Селену, що та обійшлася без своїх звичних колкостей?"
show кальтена at right, size_kaltena, appear_fade 
ka "Ви мене, звичайно, вибачте, але я не зрозуміла ні слова"
show кальтена at right, size_kaltena, disappear_fade 
"Селена начисто забула про її існування."
show нехемія at right, appear_fade 
n "Ми говорили о погоду. (ламана адарланська)"
show нехемія at right, disappear_fade 
show кальтена at right, size_kaltena, appear_fade 
ka "Про погоду"
show кальтена at right, size_kaltena, disappear_fade 
"Тоном строгої вчительки поправила Кальтена."
show селена at left, size_selena, appear_fade 
c "Думайте, з ким говорите."
show кальтена at right, size_kaltena, appear_fade 
ka "Якщо принцеса вирішила освоїти наші манери — їй варто заодно навчитися правильно говорити адарланською. Я мушу її поправляти, щоб над нею не сміялися."
show селена at left, size_selena, disappear_fade 
show кальтена at right, size_kaltena, disappear_fade 
"Селена дуже засумнівалася в бажанні Нехемії перейняти манери загарбників. Але що змусило принцесу подолати далекий шлях і приїхати в Рафтхол?"
"Шаол ступив уперед, опинившись між принцесою й Селеною."
show шаол at right, size_shaol, appear_fade 
sh "Ваше високість, ви хотіли б здійснити ознайомчу прогулянку палацом?"
show шаол at right, size_shaol, disappear_fade 
"Принцеса вслухалася в його слова, не приховуючи, що погано розуміє адарланську. Водночас вона поглядала на Селену, запрошуючи її зіграти роль перекладачки. Селена усміхнулася. Тепер зрозуміло, чому «двоногий хробак» обливається потом. Красуня Нехемія являла собою ту силу, з якою мимоволі доводиться рахуватися."
"Селена переклала питання капітана."
show нехемія at right, appear_fade 
n "Якщо прийняти це божевільне нагромадження за палац то так. (ейлуейською)"
show селена at left, size_selena, appear_fade 
c "Її високість каже, що так."
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Переклала Селена, повертаючись до Шаола."
show кальтена at right, size_kaltena, appear_fade 
ka "Ніколи не думала, що стільки ейлуейських слів перекладається одним коротким нашим"
show кальтена at right, size_kaltena, disappear_fade 
"Із фальшивою чемністю зауважила Кальтена."
"Селена вп’ялася нігтями в м’якуш долонь і подумала: «Зараз ти в мене дограєшся». Шаол щось відчув і став між Селеною й Кальтеною."
show шаол at right, size_shaol, appear_fade 
sh "Ваше високість, я капітан королівської гвардії. Дозвольте мені супроводжувати вас."
show шаол at right, size_shaol, disappear_fade 
"Церемонно промовив він, прикладаючи руку до серця. Виявилося, принцеса справді погано знала адарланську мову. Селена переклала їй слова капітана."
show нехемія at right, appear_fade 
n "Я хочу звільнитися від її присутності, у неї огидний характер. (ейлуейською)"
show нехемія at right, disappear_fade 
"Нехемія махнула в бік Кальтени."
show селена at left, size_selena, appear_fade 
show кальтена at right, size_kaltena, appear_fade 
c "Ви вільні. Ваша присутність втомлює принцесу."
show селена at left, size_selena, disappear_fade 
show кальтена at right, size_kaltena, disappear_fade 
"Селена нагородила «вчительку» тіумфуючою усмішкою."
show кальтена at right, size_kaltena, appear_fade 
ka "Але королева…"
show кальтена at right, size_kaltena, disappear_fade 
show шаол at right, size_shaol, appear_fade 
sh "Якщо так бажає її високість — вам слід їй підкоритися."
show шаол at right, size_shaol, disappear_fade 
"Селена не удостоїла розлючену Кальтену навіть кивком. Принцеса, її охоронці й радник пішли разом із Селеною й капітаном далі."
show нехемія at right, appear_fade 
n "У вас усі придворні дами схожі на неї? (ейлуейською)"
show селена at left, size_selena, appear_fade 
c "Так, ваше високість. На жаль, таких, як Кальтена, дуже багато. (ейлуейською)"
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Нехемія делікатно, але уважно розглядала Селену, придивляючись до її постаті, ходи, одягу. Інтерес був явно не святковий."
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
n "Але ви відрізняєтеся. Де ви навчилися так добре говорити ейлуейською?"
c "Я завжди цікавилася чужими мовами. Вашу кілька років вивчала."
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"На ходу збрехала Селена."
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
n "Шкода тільки, що ваш учитель був низького походження. У нас із такою інтонацією говорять селяни. Хто ж вас учив?"
c "Одна ейлуейська жінка. Жила в нас."
n "Ваша рабиня?"
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Шаол запитально подивився на Селену."
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
c "Ні. Швачка. Її мама найняла… коли була жива. Батьки виховали мене противницею рабства."
n "Тоді ви дуже сильно відрізняєтеся від ваших придворних"
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Тихо й із раптовою теплотою сказала Нехемія. Селена лише кивнула."
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
c "Дозвольте спитати, що привело вас до Рафтхолу… ваше високість?"
n "Можете не додавати мій титул. Я не люблю церемоній. Сюди я приїхала з волі мого батька, короля Ейлуе, щоб навчитися вашій мові, манерам і звичаям. Це дозволить мені краще служити Ейлуе й моєму народові."
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Звичайно, принцеса сказала лише частину правди, але Селена чемно усміхнулася"
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
c "А довго ви маєте намір пробути в Рафтхолі?"
n "Поки батько не накаже мені повернутися. Якщо пощастить, я пробуду тут не довше наступної весни. Правда, в батька є задум видати мене заміж за якогось адарланця. Батько думає, це зробить мене хорошою дружиною. Тоді мені доведеться затриматися у вас… на невизначений час."
c "Пробачте за цікавість, але чи не принца Доріна ваш батько пророчить вам у чоловіки?"
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Питання пролунало бестактно. Задавши його, Селена тут же пошкодувала про допущену необачність. «Але Нехемія лише прицмокнула язиком і глузливо підняла брови.»"
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
n "Він буквально закидав мене усмішками, але при цьому не забував підморгувати іншим."
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Нехемія знову оцінююче глянула на Селену. Принцеса помітила шрами на її руках."
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
n "А ви звідки родом, Ліліано?"
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Селена недбалим жестом сховала руки."
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
c "Я з Бельхевена. Є таке містечко в провінції Фенхару. Славиться своєю рибною гаванню. Але знали б ви, яке зловоння йде звідти."
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Принцеса засміялася."
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
n "Рафтхол пахне ненабагато краще. Може, навіть гірше. У Банджалі допомагає сонце — воно все випалює. А в річковому палаці мого батька запах напоєний ароматом квітучих лотосів."
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Шаол кашлянув. Йому набридло слухати чужу мову, не розуміючи ні слова. Селена не втрималася від лукавої усмішки"
show селена at left, size_selena, appear_fade 
c "Капітане, не треба дутися. Ми мусимо догоджати принцесі."
show шаол at right, size_shaol, appear_fade 
sh "Досить глузувати. Ми супроводимо принцесу в залу королівської ради. Я поговорю з радниками і ми вирішимо, чи варто дозволяти Кальтені супроводжувати її."
show шаол at right, size_shaol, disappear_fade 
show нехемія at right, appear_fade 
n "Ви любите полювати?"
c "Ні, я люблю читати."
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Селена, знову перейшла на ейлуейську."
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
n "Майже всі наші книги були спалені п’ять років тому, коли армія Адарлану вторглася в наші землі. Жгли все без розбору, не розрізняючи, де історія, а де… магія. Бібліотеки просто спалювали, а з ними університети й музеї…"
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"На слові «магія» вона понизила голос. Селена відчула знайому біль у грудях."
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
c "Ейлуе — не єдина країна, де це сталося."
n "Тепер книгами нас постачає Адарлан. Я пробувала їх читати і майже нічого не зрозуміла. Мені треба якнайшвидше вивчити вашу мову."
c "До чого ж я ненавиджу цю огидну сукню! Щойно я її вдягла тканина почала натирати мені шкіру."
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Нехемія окинула поглядом вишукану сукню Селени."
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
n "Як ви ще можете ходити в такому вбранні?"
c "Якщо чесно, я так і чекаю, що ця клята сукня зламає мені ребра."
n "У такому разі не одна я страждаю від адарланських нарядів."
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Шаол зупинився перед дверима, біля яких стояли шестеро караульних. Їм він звелів уважно стежити за жінками й охоронцями принцеси."
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
n "Що задумав ваш капітан?"
c "Відвести вас у залу засідань і домовитися, щоб Кальтена вас не супроводжувала."
n "Я тут і дня не пробула, а вже мрію повернутися додому."
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Раптом Нехемія міцно схопила руку Селени. У принцеси виявилися на подив мозолисті пальці — причому в тих місцях, де вони стискали руків’я меча чи кинджала. Очі жінок зустрілися і Нехемія опустила руку."
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
n "Пані Ліліано, ви складете мені компанію, поки я тут?"
c "Звичайно, принцесо. Коли я вільна — я завжди до ваших послуг."
n "Може, ви мене не зрозуміли? Слуг мені й так вистачає. Я потребую співрозмовниці."
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Селена не втрималася й широко усміхнулася. У цей час із дверей вийшов Шаол і вклонився принцесі"
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
c "Ваше високість, королівська рада бажає вас бачити. Селена переклала."
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Нехемія ламаною адарланською подякувала капітанові й знову повернулася до Селени."
show нехемія at right, appear_fade 
show селена at left, size_selena, appear_fade 
n "Рада знайомству з вами, пані Ліліано. Нехай мир перебуває з вами."
c "І з вами."
show нехемія at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Коли за принцесою зачинилися двері, Селена раптом подумала, що можливо в неї з’явилась хоч одна подруга"

#Епізод 8
stop music fadeout 1.0
scene black
with fade
scene expression "images/episodes/ep8.jpg" at scale_to_1080p
with dissolve
play sound "audio/Transition.mp3"
pause 3.0
scene black
with dissolve
scene expression "images/backgrounds/Training room (light frost).jpg"   at scale_to_1080p
with fade
play music "audio/S&D.mp3" fadein 2.0
#Training room (light frost)
"Усі наступні чотири дні Селена прокидалася на світанку й тренувалася, використовуючи будь-які придатні для вправ предмети: стільці, дверний одвірок і навіть більярдний стіл із кулями, які виявилися чудовою допомогою для вироблення рівноваги."
"Їй вдавалося добряче попотіти годину-півтори, а тоді приходив Шаол, і вони снідали. Давши їжі трохи влягтися, капітан виводив Селену в сад для ігор, і там вони вдвох бігали. Після затяжних дощів помітно похолодало, і тепер разом із рештками листя під ногами хрустів іній. Дув пронизливий вітер, змушуючи Селену бігти швидше, щоб зігрітися."
"Усі її досягнення й недоліки Шаол сприймав мовчки. Він не сказав ні слова, коли вона зненацька зігнулася навпіл і, як тоді, під час першого бігу, вивергла з себе весь сніданок. Мовчав капітан і про те, що з кожним днем вона все краще тримала дихання й встигала пробігати більшу відстань."
"Після бігу починалися навчальні поєдинки. Усі ці дні Селена й Шаол займалися в окремому приміщенні. Але спуску капітан їй не давав. Наприкінці занять Селена валилася на підлогу й верещала, що ось-ось помре від виснаження й голоду."
"Кинджали залишалися її улюбленою зброєю, хоча вона відкрила для себе всі привабливі сторони дерев’яної дубинки: ось чим можна було збити капітана з ніг без ризику відтяпати йому руку. Після тієї зустрічі з принцесою Нехемією Селена її більше не бачила й нічого про неї не знала. Навіть у плітках служниць не згадувалося ім’я принцеси."
"Шаол завжди обідав разом із Селеною, після чого давав їй короткий відпочинок і знову вів до зали. Там вона вправлялася нарівні з усіма під пильним наглядом Брулло. Головному зброяру потрібно було переконатися, що претенденти володіють усіма видами зброї."
"Селена робила все, що належало, намагаючись нічим не привертати до себе увагу Брулло, не викликати ні його докорів, ні похвал, які той розсипав на адресу Кейна."
"Як же вона ненавиділа цього Кейна! А Брулло мало не боготворив його. Інші претенденти також намагалися виказати свою повагу цьому кремезнякові, щойно він опинявся поруч. Але ніхто не хвалив Селену. Втім, і в Аробінна її ніколи не хвалили. Аробінн вважав, що похвали розхолоджують асасина."
"Зате Кейн постійно за нею спостерігав: мовчки посміхався, хмикав, підморгував і чекав, коли вона припуститься помилки. Селена пообіцяла собі: під час першого випробування ні за що не відволікатися на цього здорованя. От тільки яким воно буде, перше випробування? Брулло мовчав, Шаол — теж."
"За день до випробування Селена відчула щось недобре. Усе почалося ще зранку. Шаол не прийшов на сніданок, а натомість наказав вартовим відвести Селену до зали, де їй належало вправлятися самій. Не прийшов він і на обід. Коли вартові з’явилися, щоб знову провести її до зали, Селену переповнювали запитання. Задати їх вартовим вона не наважилася."
"Вправлятися в залі без суперника — марна трата сил. Таких вправ їй вистачало й у кімнатах. Кілька претендентів мляво билися між собою, але більшість, як і Селена, вешталися залом, супроводжувані вартовим і наставниками. Брулло в залі також не було — ще одна дивина. Його відсутність компенсувалося збільшеною кількістю вартових."
no "Що в нас сьогодні діється?"
"Переконавшись, що він не хизується, багато претендентів були б не проти скрестити з ним клинки. Однак Нокс чомусь уникав їх, надаючи перевагу тренуванням наодинці."
c "Нічого особливого. Капітан Шаол Естфол сьогодні зайнятий і не зміг вправлятися зі мною."
"Ці слова навряд чи зашкодять капітанові."
no "Нокс Оен"
"Представився злодій, простягаючи руку. Селена потиснула йому руку у відповідь"
c "Мені відомо, хто ти."
"Рука в Нокса була міцною й мозолястою. Із шрамами. Відчувалося, що хлопець чимало пережив."
no "Я ці дні намагався бути непомітним. Особливо поблизу цього чурбана."
"Нокс кивнув у бік Кейна. Той стояв посеред зали, розглядаючи свої могутні м’язи. На пальці блищав перстень із великим чорним каменем. Дивно, що Кейн не знімав перстень на час вправ. Такі штуки тільки заважають. Бувало, люди й пальців позбувалися."
no "Бачила Веріна? Схоже, його зараз вивертати почне."
"Він ткнув пальцем у бік горластого злодія, якого Селені хотілося вгамувати раз і назавжди. Зазвичай Верин тримався поблизу Кейна, піддражнюючи інших претендентів. Але сьогодні горластий Верин був непривычно тихим. Він стояв біля вікна, блідий, з виряченими очима."
pe "Я чув, як він говорив із Кейном"
"Пролунав позаду боязкий голос Пелора, наймолодшого з тутешніх асасинів. Селена пів дня спостерігала за Пелором. Майже хлопчисько, але є в ньому щось небезпечне. Як він тут опинився? Навіть голос ще ламається."
no"І про що вони говорили?"
"Він стояв, тримаючи руки в кишенях. Його одяг помітно відрізнявся від лахміття, в яке були вдягнені решта претендентів. Мабуть, у своєму Перранті він і справді був успішним злодієм."
"Веснянкувате обличчя Пелора зблідло."
pe "Вранці цього… Глазопожирателя… словом, знайшли. Мертвим."
"Глазопожиратель? Досвідчений, безжальний убивця… мертвий?"
c "Як це сталося?"
"Пелор відповів не одразу. Озирнувся по боках, потім ковтнув ком сливи й лише тоді зашепотів:"
pe "Верин розповідав… видовище жахливе. Його ніби хтось намагався навпіл розірвати. Верин натрапив на труп, коли йшов сюди."
"Нокс вилаявся крізь зуби. Селена оглянула зал. Схоже, про загибель Глазопожирателя знали всі. У залі стояла непривычна тиша. Претенденти збилися в кілька купок і перешіптувалися."
pe "Верин казав… груди в клапті розірвані."
"У Селени похолола спина. Вона струснула головою, проганяючи страх. У цей час до зали увійшов ще один вартовій і оголосив, що Брулло дозволяє їм сьогодні вправлятися, кому як заманеться."
"Селена яскраво уявила собі розполосований труп Глазопожирателя й потім ніяк не могла позбутися жахливої картини. Вихід був лише один — якомога швидше чимось себе зайняти. Не сказавши ні слова Ноксу й Пелорові, вона підійшла до стійки зі зброєю й узяла пояс із метальними ножами."
"Місце для тренування Селена вибрала поблизу мішеней для лучників. Невдовзі до неї приєднався Нокс. Він мовчки почав метати в мішень свої ножі. Усі вони влучали в друге кільце, але ніяк не в середину. Метальник із нього був кепський. З лука він стріляв значно краще."
"Селена дістала перший ніж. Ну хто, хто міг із такою жорстокістю вбити претендента? І де? Просто в коридорі! Як убивцям удалося зникнути, якщо в замку повно гвардійців, вартових та іншої охорони?"
"Але скільки не став питання, Глазопожиратель мертвий, і вбили його напередодні першого змагання. Що це? Страшна випадковість? Чи хтось вирішив прискорити вибуття претендентів і це лише початок?"
"Зосередившись на маленькій чорній точці в центрі мішені, Селена заспокоїла дихання, прицілилася, розслабила зап’ястя. Усі інші звуки в залі перестали існувати. Чорний кружечок, схожий на бичаче око, манив її. Селена видихнула й метнула ніж."
"Лезо блиснуло сріблястою зірочкою й увійшло в чорну точку. Селена похмуро посміхнулася."
"Поруч заковилисто вилаявся Нокс. Чергові його ніж ще більше відхилився від цілі, влучивши в третє кільце. Селена посміхнулася ще ширше, на мить забувши про понівечений труп Глазопожирателя."
"Коли вона метнула другий ніж, її зненацька гукнув Верин. Він зараз вправлявся в парі з Кейном."
ve "Ей, послухай, красуне. Королівському захисникові ці балаганні трюки ні до чого."
"Селена глянула в його бік і зараз же знову вп’ялася поглядом у мішень."
ve "Напружуватися особливо не треба. Якщо хочеш, увечері можу тобі урок провести."
"Верин залився сміхом. Кейн теж загоготав. Селена до болю стиснула руків’я ножа."
no "Та не слухай ти їх (пошепки)"
"Він знову метнув ніж, і знову той увійшов у дерево далеко від чорного кружечка."
no "Суцільне бахвальство. Вони й не знають, з якого боку підступити до жінки, навіть якщо вона сама до них прийде."
"Ще один ніж Селени застряг майже поруч із попереднім, викликавши щире здивування Нокса. Селена прикинула вік сіроокого хлопця. Навряд чи йому було більше двадцяти п’яти."
no "А ти дуже влучна."
c "Влучна для жінки?"
no "Ні. Загалом влучнa."
"Він кинув останній ніж і влучив у третє кільце. Пожавши плечима, ніби успіх метання від нього не залежав, Нокс підійшов до мішені і витягнув усі ножі."
c "У тебе стійка неправильна. І пальці ти тримаєш не так. (пошепки)"
"Нокс опустив руку."
c "Дивись. Стаєш, як я."
"Нокс слухняно став у таку саму позу."
c "Тепер трохи зігни ноги в колінах. Розправ плечі й розслаб кистю. Метати треба на видиху. Отак."
"Селена метнула ніж і знову влучила точно в середину."
no "Покажи ще раз."
"Вона повторила. Потім кинула лівою рукою й мало не скрикнула від радості, коли цей ніж застряг у руків’ї попереднього."
"Нокс сумлінно наслідував усі її рухи, але його ніж увійшов вище середини."
no "Кидати поруч із тобою — тільки ганьбитися."
c "Кистю не затискай, вона має бути вільною. Ти ж не камінь кидаєш. Тому весь час і промазуєш."
"Нокс слухав її з відкритим ротом, наче старанний хлопчик-учень. Він постарався в точності повторити кожен рух Селени й після видиху метнув ніж. У середину не влучив, але його ніж уперше опинився у внутрішньому колі."
no "Ну от, уже краще."
c "Усього трішки."
"Охолодила його радість Селена. Вона дочекалася, поки Нокс звільнить мішені, після чого прибрала свої ножі в поясні тримачі."
c "Ти ж із Перранту?"
"Сама вона ніколи не бувала в Перранті — другому за величиною місті Террасена, але знайоме слово обпекло її хвилею страху, що швидко змінилася іншою хвилею — душевного болю, не менш пекучого, ніж перша. Як швидко летить час."
"Ось і десять років промайнуло з того дня, як убили короля Террасена та всю його родину. Десять років тому до них увірвалися адарланські загарбники, і рідна країна Селени зустріла їх із опущеними головами й у повному мовчанні."
"Краще взагалі не починати розмову на такі теми. Селена в черговий раз подумки вилаяла себе за те, що слова в неї випереджають думки."
"Вона постаралася зобразити на обличчі байдуже цікавість. Здається, Нокс нічого не запідозрив."
no "Так, із Перранту я. Доти й жив там безвиїзно. А ти, пам’ятаю, з Бельхевена?"
c "Так. Мій батько — великий торговець."
no "І як він ставиться до доньки, яка заробляє на життя крадіжкою коштовностей?"
"Селена посміхнулася й знову метнула ніж."
c "Коли він усе дізнався, страшенно розлютився й заявив, що на поріг мене не пустить."
no "Може, він тебе вже й простив."
c "Не знаю."
no "Пощастило тобі з наставником. Тобі дали найкращого. Я бачив, він тебе змушує щоранку бігати."
"Перрантський злодій кивнув у бік свого наставника. Той сидів на підлозі, притулившись до стіни, й дрімав."
no "Ну от, знову дрімає. Він або спить, або п’є. Я його мало не на колінах благав вивести мене в сад."
c "Іноді капітан дуже мене дістає своїми причіпками. Але ти правий: він справді найкращий."
"Нокс помовчав."
no "Знаєш, коли нам знову дозволять вправлятися самим, розшукай мене, і ми позаймаємося разом."
c "Навіщо?"
"Вона хотіла метнути черговий ніж, але поясні тримачі вже були порожні. Нокс метнув свій і цього разу влучив точно в середину."
no "Я хочу, щоб ти виграла ці кляті змагання."
c "А ти що, не хочеш стати королівським захисником?"
no "Не потягну я."
no "Тоді сподіваймося, що завтрашнє випробування не стане для тебе першим і останнім."
"Обнадійливо посміхнулася йому Селена. Вона знову, в котрий уже раз, оглянула зал. Жодних змін. Окрім Кейна й Веріна, решта мовчали. Судячи з мертвотної блідості облич, жорстоке вбивство Глазопожирателя загнало претендентів у ступор."
c "І давай сподіватися, що жоден із нас не скінчить, як Глазопожиратель"
"Їй дуже хотілося на це сподіватися."
#Selena's Room (The Glass Castle) light frost
scene expression "images/backgrounds/Selena's Room (The Glass Castle) light frost.jpg"   at scale_to_1080p
with fade
"Минув деякий час"
sh "Ти що, збираєшся сидіти з книжкою до самої ночі?"
"Передзахідне сонце, заглядаючи у вікно, приємно зігрівало обличчя. І вітер сьогодні був не пронизливий, а легкий. Але пізня осінь у цих краях ніколи не вирізнялася теплом. Ще пара днів — і почнеться зимовий холод."
"Селена закрила книгу й підвелася. Шаола не було весь день, і вона зовсім не думала, що він з’явиться саме зараз."
c "А що мені ще робити? Гуляти коридорами? Я не маю бажання натрапити на труп роздертого Глазопожирателя."
"Погляд капітана потемнів."
sh "Тебе це не стосується. І не намагайся приставати до мене з розпитуваннями. Що ти читаєш? «Вітер і дощ»? Я читав цю книгу. Усе хотів запитати, як тобі вона."
"Невже він прийшов поговорити про книжку? Навіщо він намагається поводитися так, ніби ніякого вбивства в замку не було? І вбили ж не якогось слугу й навіть не вартового. Убили одного з претендентів на титул королівського захисника."
c "Нуднувата книжка. Підтекст, алегорії. Кожну фразу по кілька разів перечитувати треба, поки сенс уловиш."
"Капітан мовчав."
c"Ти ж прийшов зовсім з іншої причини."
sh "У мене сьогодні був довгий і важкий день."
"Селена розтирала коліно, забите в залі."
c "Це було пов’язано з… ти знаєш, із чим?"
sh "Не вгадала. Принц затягнув мене на засідання ради, і мені довелося три години там сидіти."
"Ні, він явно щось недоговорював."
c "А я думала, ви з принцом — друзі."
sh"Ми друзі. Але коли принц кличе на нудне засідання, відмовитися я не можу."
c "І давно ви дружите?"
"Шаол відповів не одразу. Селена зрозуміла: він вирішує, про що їй можна говорити, а про що краще помовчати, щоб вона не вдарила його ж зброєю."
"Мовчання затяглося. Селені захотілося розворушити капітана якоюсь колкістю."
sh "Ми знайомі з дитинства. Ми з Доріном були єдиними однолітками… принаймні серед знаті. Отак і подружилися."
sh "Разом училися, разом гралися, разом вправлялися. Але коли мені виповнилося тринадцять, батько вирішив повернутися в Аньєль, і наша родина покинула Рафтхол."
c "Тож ти з міста на Срібному озері?"
"Тоді, дорогою до Рафтхола, вона вгадала правильно: Шаол походив зі знатного роду. Швидше за все, його родина правила Аньєлем та околицями. Мешканців цього міста називали прирожденими воїнами."
"Десятки років аньєльці служили живою стіною, що охороняла королівство від орд дикунів із гір. За схожість гірських вершин із білими іклами їх так і назвали — Білокликові гори. Мабуть, мешканці Аньєля тільки раділи, коли десять років тому адарланський король вирішив приборкати білокликів."
"Ті билися до останнього й дуже рідко потрапляли в адарланське рабство. Селені доводилося чути легенди про непокірних білокликів. Не бажаючи скоритися адарланському королеві, вони вбивали своїх дружин і дітей, а потім самі кидалися в прірву."
"Селена уявила, як це — жити в сусідстві з сотнями здорованів на кшталт Кейна, і внутрішньо здригнулася."
sh "Батько й мене готував до кар’єри радника. Він мені твердив, що настають нові часи, що з загрозою білокликів покінчено й бути радником тепер набагато почесніше й вигідніше, ніж військовим. Але я сумував за Рафтхолом."
c "І втік сюди?"
"Її дивувала незвична відвертість Шаола. Пам’ятається, дорогою сюди він категорично відмовлявся говорити про своє життя. Може, тепер став більше їй довіряти?"
sh "Утік? Ні, втеча нічого б не вирішила. Дорін умовив тодішнього капітана королівських гвардійців узяти мене на навчання. Брулло викликався допомагати. Але мій батько відмовлявся. Старшому синові завжди важче."
sh "Я ж мав успадкувати титул правителя Аньєля. У мене був єдиний вихід: я покликав стряпчого й у його присутності відмовився від титулу на користь молодшого брата. Наступного ж дня я поїхав до Рафтхола. Батько навіть не захотів зі мною попрощатися."
"Здається, капітан сказав їй усе, що дозволив собі сказати. Отже, у нього є молодший брат. Є впертий батько. А про матір — ні слова. Може, померла?"
sh "А що ти про себе розкажеш?"
c "Я думала, тебе взагалі не цікавить моє життя,"
"Капітан ледь усміхнувся. Він дивився не на Селену, а на небо, де сині й блакитні барви змінювалися помаранчевими."
sh "Чому ж, цікавить. І найбільше мені цікаво, як твої батьки наважилися віддати тебе на навчання ремеслу асасина. Чи вони пишалися славою доньки?"
c "Мої батьки мертві. Їх не стало, коли мені було вісім."
sh "Тож ти…"
"У Селени закалатало серце."
c "Я народилася в Террасені, потім стала асасином, потім опинилася в Ендов’єрі, а тепер перебуваю тут. Як бачиш, нічого цікавого."
"Селена думала, що на цьому розпитування закінчаться, але Шаол, помовчавши хвилин п’ять, раптом запитав:"
sh "Звідки в тебе шрам на правій руці? Він у тебе давній, не з Ендов’єра."
"Звісно, не з Ендов’єра. Там її нагородили іншими шрамами."
c "У свої дванадцять я була ще впертіша, ніж зараз. Аробінн Хемел — так звали мого наставника — весь час твердив нам: ліва рука в асасина має вміти те саме, що й права. Зокрема, володіти мечем. Спочатку він просто прив’язав мені праву руку до тіла, змусивши все робити лише лівою."
c "Мені це не сподобалося, і я перерізала мотузку. Він зав’язав удруге, пригрозивши, що якщо знову розв’яжу, буде гірше. Я не повірила. Тоді Аробінн сказав: «Вибирай: або ти сама зламаєш собі праву руку, або я». Того ж вечора я приклала руку до дверного одвірка й щосили рвонула двері на себе."
"Селена скривилася. Їй і зараз було моторошно згадувати про вимушене членовредительство."
c "Я зламала дві кістки. Рука зрослася лише через кілька місяців. Мені не залишалося нічого іншого, як усе робити лівою рукою. У тому числі й вправлятися з мечем. Сподіваюся, у Брулло були інші методи навчання."
sh "Рук насильно він не ламав, а в решті… Сама бачила, що поблажливості від нього не дочекаєшся."
"Шаол підвівся зі стільця."
sh "Завтра — перше випробування. Ти готова?"
c "Звісно."
"Збрехала Селена. Капітан постояв ще пару хвилин, дивлячись на неї."
sh "Завтра вранці я прийду."
"Сказав він і вийшов. Селена розмірковувала про почуте. Вона й не припускала, як багато схожого в її житті й житті капітана Естфола. І як багато абсолютно несхожого."
"Вона вийшла на балкон і стала, обхопивши себе руками. Сонце сідало. Вітер ставав дедалі холоднішим. Він тріпав її сукню, студив спину й нарешті змусив піти з балкона."
"Упевненість Селени була удаваною. Насправді її лякала невідомість майбутнього випробування. Після п’ятиденних вправ, після того, як у її руках побували всі види зброї, після виснажливих занять у залі, у саду й у кімнатах у її тілі не залишилося жодного м’яза, який би не болів. Цього вона теж намагалася не показувати, хоча спробуй сховати пульсуючий біль у руках і ногах!"
#Training room (dartboards)
scene expression "images/backgrounds/Training room (dartboards).jpg"   at scale_to_1080p
with fade
"Коли вранці Селена разом із Шаолом прийшла до знайомої зали, її зустріли здивовані обличчя претендентів. Зал був перегороджений величезною чорною завісою. Залишалося лише гадати, що ховалося за нею. Не так уже й важливо, що саме. Важливо інше: сьогодні тут вирішиться чиясь доля, і для когось перше випробування стане останнім."
"Претенденти тулилися до стін і своїх наставників. Говорили пошепки, але більше мовчали. Селена стояла поруч із Шаолом. Капітан був у своєму звичайному чорному мундирі. Він не вважав майбутнє випробування подією. А «благодійники» претендентів, що зібралися на галереї, думали інакше. Вбрані в пух і прах, вони нагадували птахів, що взирають на світ із висоти сідала."
"У Селени стиснуло горло, коли в їхній юрбі вона розгледіла спадкового принца. Після зустрічі на королівській аудієнції вони більше не бачилися. Вона не встигла прочитати всіх книжок, надісланих Доріаном, а тому в неї не було приводу писати йому. Принц теж помітив Селену й усміхнувся їй, блиснувши сапфіровими очима. Вона відповіла стриманою усмішкою й відвернулася."
"Біля завіси стояв Брулло. Його посічена шрамами рука стискала ефес меча."
"Зліва до неї хтось підійшов. Вона вже знала хто."
no "Трохи балаганом тхне (пошепки)"
"Селена глянула на нього. Шаол, що стояв позаду, насторожився. А раптом у цього злодійчука й Селени вже готовий план: утекти, попередньо вбивши всю королівську родину?"
c "Краще вже балаган, ніж тупі вправи. Хоч якась розвага."
"Нокс затрясся від беззвучного сміху."
no "І яка ж?"
"Селена знизала плечима, продовжуючи дивитися на завісу. Здається, зібралися всі. Невдовзі потворні баштові годинники прогуркочуть дев’ять, і змагання почнеться. Нокс був помітно збуджений. Але в таких змаганнях кожен сам за себе. Навіть якби вона й знала характер випробування, усе одно нічого б не сказала сіроокому злодійчукові."
c "Я так думаю, за завісою ховають зграю вовків-людожерів. Нам доведеться душити їх голими руками."
"Селена повернулася до Нокса, усмішкою показуючи злодієві, що жартує."
c "Правда, весело?"
"Шаол тихо кашлянув, попереджаючи Селену, що час балачок закінчився."
c "Удачі."
"Шепнула вона злодієві й рушила до завіси, недбало засунувши руки в кишені своїх чорних штанів. Відійшовши з капітаном на кілька кроків, Селена не втрималася й усе-таки запитала:"
c "Тож ти не знаєш, що там, за завісою?"
"Шаол похитав головою."
"Вона поправила щільний шкіряний ремінь, що гойдався на її стегнах. До нього можна було причепити непогану колекцію зброї. Нічого, через якийсь час ремінь перестане їздити по талії, а там, дивись, може, й наповниться різними корисними штучками. Загибель Глазопожирателя мала й позитивну сторону: одним суперником менше."
"Селена ковзнула поглядом по галереї. Дорінові звідти прекрасно видно обидві половини зали. Міг би й підказати, якщо справді хоче допомогти своїй захисниці."
"Недалеко від принца стояв виряджений Перангон. Бачачи його самовдоволену посмішку, Селена скривилася. Герцог взирав на свого улюбленця Кейна, а той, мабуть, бажаючи догодити панові, грав м’язами. А може, Кейн тому так і поводиться, що Перангон розкрив йому секрет змагання?"
"Брулло голосно прочистив горло."
b "А тепер увага!"
"Претенденти замовкли. Кожен намагався виглядати спокійним. Головний зброяр неквапливо підійшов до середини завіси."
b "От і настав час вашого першого випробування."
"Брулло широко всміхався, ніби за завісою їх чекала чортова дюжина різних капостей."
b "Як ви вже знаєте зі слів його величності, один із вас сьогодні покине змагання, оскільки буде недостойним їх продовжувати."
"‘Скільки ти ще нас маринуватимеш?’ — сердито подумала Селена."
"Ніби прочитавши її думки, Брулло клацнув пальцями, і вартові біля стіни взялися за складки завіси. Гвардійці не поспішали. Завіса повзла ледь-ледь. Мабуть, не одна Селена скрипіла зубами. І раптом…"
#Training room (dartboards2)
scene expression "images/backgrounds/Training room (dartboards2).jpg"   at scale_to_1080p
with fade
"Вона прикусила губу, щоб не засміятися. Стрільба з лука? Усього-на-всього?"
"Коли половинки завіси повністю розійшлися, стали видні п’ять мішеней, поставлених на різній відстані."
b "Правила прості.  Кожен отримає п’ять стріл — по стрілі на мішень. Той, кого за результатами визнають найгіршим стрільцем, відправиться геть."
"Претенденти зашепотіли: хто з полегшенням, а хто насторожено. Селена з усіх сил намагалася сховати тріумфальну усмішку. Тут у поле її зору потрапила глузлива фізіономія Кейна. Чому не він опинився на місці Глазопожирателя?"
b "Отже, стріляти будете по одному. Підходьте до столу, вишиковуйтеся в чергу. Оголошую, що випробування почалося."
"Селена думала, що претенденти мить же кинуться до довгого столу, куди солдати висипали абсолютно однакові луки й однакові сагайдаки, наповнені однаковими стрілами. Ні, кожен відтягував час. Навіть самовпевнений Кейн."
sh "Не поспішай. Краще, якщо ти опинишся в кінці черги. І не красуйся. Зрозуміла? (пошепки)"
"Селена обдарувала його чемною придворною усмішкою й смикнула плечем."
c "Постараюся,"
"Пообіцяла вона й пішла займати чергу. Невже всі ці виряжені й надуті старі не розуміли, на який ризик вони йдуть, даючи претендентам луки й стріли? Наконечники стріл були навмисне затуплені. Але навіть такою стрілою можна легко пробити горло Перангона чи Доріана. Тільки захотіти."
"Думка приємно лоскотала нерви, але Селена відігнала її. Зараз важливо стежити за претендентами. Вона стала майже в самий кінець черги — за нею було ще троє. Попереду — дев’ятнадцять осіб. Кожному треба зробити по п’ять пострілів."
"Змагання, що ще нещодавно лякало своєю невизначеністю, тепер загрожувало перетворитися на нудне заняття. Залишається розважати себе, спостерігаючи за чужими пострілами. Заодно побачить, чи справді Кейн майстерно володіє цією зброєю."
"Перші ж постріли показали Селені, що лук тримати претенденти вміють. Мішені являли собою величезні круги, усередині яких знаходилося п’ять кольорових кілець. Центр був жовтим, із маленькою чорною точкою посередині."
"Чим далі мішень, тим важче влучити не лише в чорний очко, а й у жовтий кружечок. А зал був великий, і п’ята мішень знаходилася на відстані сімдесяти ярдів."
"Селена провела пальцями по вигинах тисового лука. Уміння влучно стріляти — це абетка асасина, перше, з чого починається навчання ремеслу. Аробінн не був винятком; коли Селена потрапила до нього, він одразу почав учити її мистецтву лучника."
"Дивлячись на дії претендентів, Селена розуміла: ці двоє не збрехали. Судячи з манери стрільби, вони справді були асасинами. Правда, у чорні очка не влучив ніхто, а на дальніх мішенях їхні результати були більш ніж скромними. Проте стріляти вони вміли, і ті, хто вчив їх цьому, знали свою справу."
"Хирлявий Пелор не вирізнявся силою. Лук був для нього завеликий, через що дві стріли влучили в самий край мішеней, а три взагалі пролетіли повз. Очі асасина сердито палали. У залі пролунали смішки, а Кейн загоготав на весь голос."
b "Послухай, хлопче, ти що, перший раз лук у руках тримаєш?"
"Пелор підняв голову й зухвало подивився на головного зброяра."
pe "А мені не було потреби стріляти. Я майстер у отрутах і знаю їх, як свої п’ять пальців."
b "В отрутах? Але королеві потрібен захисник, а не отруйник. Ти ж не здатен влучити навіть у пасучуся корову."
"Головний зброяр махнув рукою, буквально проганяючи Пелора. Претенденти знову засміялися. Селені теж хотілося посміятися разом із ними. Пелор шумно вдихнув повітря, опустив плечі й поплентався туди, де стояли відстріляні претенденти."
"Селена була майже впевнена, що змагання для хлопця закінчилися. І куди йому тепер? У в’язницю? На каторгу? Селені розхотілося насміхатися з невмілого стрільця. Потішатися треба було над кимось із виряджених вельмож, що притягли Пелора сюди. Втім, може, для хлопця ще не все втрачено? Отруйники королям теж потрібні."
"Зате її чимало здивував Нокс. Три найближчі мішені він уразив точно в центр, а в двох дальніх його стріли лягли в межах жовтих кружечків. Мабуть, їй би не завадив такий союзник. Бачачи, якими поглядами проводжають Нокса решта претендентів, Селена зрозуміла: ця думка блукала не лише в її голові."
"Асасин із похмурим ім’ям Могила теж виявився вмілим стрільцем. Чотири влучання в очко. П’ята стріла лягла зовсім поруч із чорною точкою. Де ж його навчили так чудово стріляти? У цей час настала черга Кейна. Поблискуючи чорним каменем на персні, він укинув лук і… Стріли летіли одна за одною, ніби Кейн пускав їх навмання."
"Коли стихло відлуння від дзвону останньої стріли, у залі стало тихо. Селена зрозуміла причину цієї тиші, і в неї звело живіт. Усі п’ять стріл Кейн послав прямо в чорні очка… Ні, не зовсім. Придивившись, Селена побачила: стріли Кейна лягали поруч із центром. Одна — так дуже близько. Це трохи заспокоїло Селену."
"З незрозумілої причини черга стала рухатися швидше, але Селена не звернула на це уваги. Усі її думки займав Кейн. Вона бачила, з яким запалом Перангон аплодує своєму здорованю. Навіть суворий Брулло не втримався й поплескав Кейна по спині. Кейном захоплювалися мало не всі, і не тому, що білоклик був горою м’язів, а тому, що він справді заслуговував захоплення."
"Зайнята думками, Селена не одразу зрозуміла, що тепер її черга. Вона стояла біля білої крейдяної лінії, сам на сам із п’ятьма мішенями й простором зали. Хтось із претендентів хихикнув. Селена навіть не обернулася. Навпомацки дістала з сагайдака стрілу й вклала в лук."
"Днів три тому вони вправлялися в стрільбі з лука, і Селена була задоволена своїми результатами. Вона могла б стріляти й точніше, але пам’ятала вимогу Шаола — не привертати до себе зайвої уваги. У давні часи вона вражала й більш віддалені цілі, ніж мішень у кінці зали. Стріляла вона красиво й точно — прямо в горло жертви."
"У роті зовсім пересохло. Зараз не завадив би ковток води, але води їй ніхто не дасть."
"‘Я — Селена Сардотін, найкращий асасин у всьому Адарлані, — подумки твердила вона. — Якби ці люди знали, хто я, їм би розхотілося сміятися. Я — Селена Сардотін. Я переможу. Я не боятимуся’."
"Селена взялася за тетиву. Її руки нили від напруги. Усупереч волі вона викинула з поля уваги все, що не було пов’язане з луком, стрілою й мішенню. Потім глибоко вдихнула й на видиху відпустила тятива."
"Майже в ціль!"
"Судома в животі почала слабшати. Селена придивилася до мішені. Так, могла б послати стрілу точно в ціль. Але не варто. Вона — не Кейн і в зайвій увазі не потребує."
"Другу стрілу Селена цілила в жовтий кружечок. Якби вистачало стріл, вона могла б усіяти ними всю межу цього кружечка."
"Третя стріла знову лягла поруч із чорним очком мішені. Трохи вище. Випускаючи четверту стрілу, Селена взяла трохи нижче очка, і стріла слухняно полетіла туди."
"П’яту стрілу чекала така ж доля, але тут до вух Селени долинуло чуже зневажливе хихикання. Вона повернула голову. Це був рудий найманець на ім’я Ренальт. Селена не знала, чим же вона так його розсмішила, але хихикання найманця чомусь її зачепило. Вона взяла останню стрілу й сильно натягнула тятива."
"З сімдесяти ярдів різнокольорові кільця виглядали колечками, а очко — крихітною чорною порошинкою. Селена майже не розрізняла цю порошинку. Недаремно навіть Кейн не зумів туди влучити. Права рука заніла від напруги. Селена ще трохи відтягнула тятива й вистрілила."
"Стріла влучила прямо в чорне очко, і воно перестало існувати. Сміх припинився."
"Ніхто не сказав ні слова, коли Селена повернулася й кинула лук із порожнім сагайдаком у візок. Шаол зустрів її похмурим поглядом. Ще б пак! Дівчисько, що вражає дальню мішень точніше, ніж ближні, мимоволі привертає до себе увагу. Зате Доріан обнадійливо всміхався. Вона не відповіла йому усмішкою, а стала осторонь."
"Змагання закінчилося. Брулло прискіпливо звіряв результати. Найгіршим виявився не Пелор, а один із солдатів королівської армії, який і вибув із подальших змагань. Селені хотілося насолодитися своєю перемогою, але щось заважало. Якесь дивне відчуття марно витрачених зусиль."

#Епізод 9
stop music fadeout 1.0
scene black
with fade
scene expression "images/episodes/ep9.jpg" at scale_to_1080p
with dissolve
play sound "audio/Transition.mp3"
pause 3.0
scene black
with dissolve
scene expression "images/backgrounds/Hill.jpg"   at scale_to_1080p
with fade
play music "audio/S&D.mp3" fadein 2.0
#Hill
"Селена збила дихання й тепер була змушена ковтати повітря ротом. Шаол біг поруч. Він умів дихати майже безшумно й ніколи не показував, що втомився. Селена бачила це по краплинках поту на його лобі та темних плямах, що розпливалися по білій сорочці."
"Вони бігли до вершини пагорба, прихованої ранковим туманом. У Селени підкошувалися ноги, а живіт підкочував до горла. Вона голосно видихнула, привертаючи увагу Шаола, потім зупинилася й обхопила стовбур дерева."
"Дихання ротом не допомагало. Почалися знайомі позиви до блювоти, і її вивернуло просто біля дерева. Селена ненавиділа теплі сльози, що хльостали з очей. Але зараз вона навіть не могла їх змахнути. Шлунок витрусив не все, і вона знову нахилилася, тримаючись за стовбур. Шаол стояв неподалік і просто дивився."
"Селена вперлася лобом у стовбур, намагаючись заспокоїти дихання й позбутисяприсмаку в роті. Минуло всього три дні після першого випробування й десять — з моменту її приїзду в Рафтхол, а вона досі не повернула колишню силу. Чотири дні пролетять швидко, а там — друга перевірка, і знову хтось покине лави претендентів."
"Вправи тривали своїм чередом, однак Селена почала прокидатися ще раніше й до приходу Шаола встигала змокнути від своїх занять. Вона не дозволить собі поступитися ні Кейну, ні Ренальту, ні комусь іншому."
sh "Повністю очистилася?"
"Селена підняла голову, збираючись нагородити його сердитим поглядом. Не вийшло: голова запаморочилася, а невдовзі з’явилися знайомі позиви. Третя хвиля."
sh "Казав я тобі: не можна їсти перед бігом. Могла б потерпіти до повернення."
c "Тобі приносить задоволення знущатися з мене?"
sh "По-моєму, це ти знущаєшся з себе, вивертаючи нутрощі навиворіт."
c "Тобі пощастило, капітане. Наступного разу це може статися так несподівано, що мене виверне просто тобі під ноги."
sh "Ти спочатку мене наздожени. Чи ти думаєш, я покірно стоятиму поруч і чекатиму, коли ти обіллєш мене цією кашею?"
"Селені відчайдушно захотілося збити посмішку з капітанського обличчя, але щойно вона зробила крок, відчула слабкість у колінах. Довелося вкотре обхопити дерев’яний стовбур. Краєм ока Селена помітила, що Шаол пильно роздивляється її спину. Нижня сорочка задралася, і частина спини була голою."
c "Тобі ніяк подобається витріщатися на мої шрами?"
sh "Коли вони в тебе з’явилися?"
"Селена розуміла: мова про три огидні шрами, що тягнуться вздовж спини."
c "А як на твою думку, коли вони могли з’явитися?"
"Він не відповів. Селена підняла голову, роздивляючись дерева. Налетівший вітер хитнув їх, і два листочки зірвалися вниз."
c "Цими шрамами мене нагородили в перший же день мого ендов’єрського життя."
sh "А що ти зробила, щоб їх заробити?"
sh "Заробити? Їх не заробляють. Удари батогом роздають дарма й у будь-якій кількості. Скотину б’ють, коли вона вперта, а рабів — просто тому, що в наглядача запор, або тому, що вчора він програв у кості місячне жалування."
"Шаол спробував щось сказати, але Селена махнула рукою."
c "Якщо запитав, то слухай… Я ледь встигла опинитися всередині поселення, як мене потягли кудись і прив’язали між двома стовпами для порки. Двадцять один удар батогами. Для остраху."
"Селена не бачила ні капітана, ні попелясто-сірого неба над Рафтхолом. Точніше, небо вона бачила, але не це, а темно-синє, майже чорне небо Ендов’єра. У вухах засвистів вітер, і до нього додалися зітхання та стогони рабів."
c "Це сталося раніше, ніж я встигла познайомитися хоч із кимось із в’язнів."
sh "Зажди, тебе що ж, ледь привезли в Ендов’єр і одразу потягли до стовпів?"
"Селена зам’ялася."
c "Ну, не одразу. Один слинявий наглядач поліз мене лапати. Я хоч і в кайданах була, але показала йому, що я не дівка з таверни… Усю ніч я стискала зуби, щоб не стогнати. Рани почали запалюватися. По суті, мене кинули помирати: або від запалення, або від втрати крові. Я це розуміла."
sh "І тобі ніхто не допоміг?"
c "Тільки вранці. Ці пси здивувалися, що я ще жива. Нас вишикували, щоб відвести на сніданок. Поки стояли в ланцюжку, якась жінка непомітно сунула мені бляшанку з маззю. Я навіть подякувати їй не встигла. Того ж дня наглядачі убили її."
"Селена стиснула кулаки, відчуваючи, як сльози печуть їй очі."
c "Коли я вирішила втекти, я спочатку зайшла в ту частину шахти, де товпилися ці четверо, і розрахувалася з ними за мою рятівницю… Вони не вірили, що помруть. Я їх переконала."
sh "В Ендов’єрі не так уже й багато жінок, невже більше ніхто…"
"Він замовк, ніби не знав або боявся вимовити потрібне слово."
c "Ти хочеш запитати, невже ніхто не намагався завалити мене, як ту нещасну? Коли я, ледь з’явившись, зламала ніс їхньому дружкові, вони дещо зрозуміли."
c "А після невдалого втечі наглядачі не наважувалися наближатися до мене. Одного, який намагався ставитися до мене майже по-людськи, швидко прибрали. Начальство боялося мого впливу. А раптом я зумію обдурити вартових і знову спробую втекти?"
"Вітер накидав їй волосся на все ще мокрий лоб. Капітанові не було потреби знати про її здогадки. Селені не раз здавалося, що Аробінн якимось чином підкупив стражників, і ті потім більше кричали на неї, ніж били."
c "Кожен виживає, як уміє."
"Селену здивувало, з яким співчуттям дивився на неї капітан, мовчки киваючи її словам. Не особливо розмірковуючи про причини, Селена повернулася й побігла вгору схилом, до вершини пагорба, де промені сонця розганяли туман."
#Training room (empty)
scene expression "images/backgrounds/Training room (empty).jpg"   at scale_to_1080p
with fade
"Наступного дня Брулло зібрав претендентів у коло й чомусь почав розповідати про те, чим одні види зброї відрізняються від інших. Усе це Селена засвоїла ще в дитинстві й відтоді добре пам’ятала. Тим більше що Аробінн був значно вражаючим оповідачем, ніж Брулло."
"‘Цікаво, чи можна навчитися спати стоячи й прокидатися в потрібний час?’ — позіхаючи, думала Селена."
"Несподівано її увагу привернула тінь, що промайнула неподалік від скляних дверей, які вели в сад. Може, собака забігла? Селена повернулася й побачила, як один із претендентів — розжалуваний солдат — збив із ніг вартового, і той звалився на підлогу."
"Падаючи, вартовій сильно вдарився головою об мармурові плити й завмер. Селена не наважилася ворухнутися. Решта претендентів також заціпеніли. Бунтівник, розраховуючи на несподіваність, кинувся до скляних дверей, збираючись розчахнути їх і сховатися в саду."
"Але Шаол та його гвардійці виявилися швидшими. Втікач навіть не встиг вискочити в сад. Стріла застрягла в нього в горлі, коли він розчахував двері."
"У залі запанувала пронизлива тиша. Одні гвардійці оточили претендентів, тримаючи зброю напоготові. Інші, включно з Шаолом, кинулися туди, де майже поруч лежали бездиханний стражник і вбитий претендент. На галереї поскрипували луки. Караульні, що перебували там, тримали під прицілом мало не кожного претендента."
"Селена завмерла. За пару кроків завмер Нокс. Зараз це було найправильнішим. Один хибний рух — і який-небудь переляканий солдатик всадить тобі стрілу в горлянку. Навіть Кейн намагався дихати безшумно."
"Селена бачила, як Шаол схилився над пораненим вартовим, намагаючись зрозуміти, чи живий той. Ніхто не наважувався доторкнутися до вбитого втікача, рука якого й зараз ще тягнулася до скляних дверей. Селена пам’ятала його ім’я — Савен, але не знала, за що його вигнали з армії."
no "Боги небесні. Вони ж його… убили. (пошепки)"
"Селена хотіла сказати йому, щоб заткнувся, але боялася ворухнутися. Решта претендентів обережно перешіптувалися, і тільки. Зробити хоча б крок не наважувався ніхто."
no "Я знав, що вартові завжди насторожі й втеча звідси неможлива, але… Мій благодійник обіцяв мені: навіть якщо я програю змагання, я не повернуся до в’язниці. А йому можна вірити, моєму благодійникові."
"Селена зрозуміла: мова злодія звернена не стільки до неї, скільки до самого себе. Промовивши ще кілька безладних фраз, Нокс замовк. А їй не відірвати погляду від убитого Савена."
"Що змусило колишнього солдата так ризикувати? І чому саме зараз? До другого випробування залишалося ще три дні. Мабуть, Савен і сам не розумів, що штовхнуло його до дверей."
"Дурна несподіваність — ось як це називається. Хіба в той день, коли Селена намагалася втекти з Ендов’єра, вона думала про свободу? Вона що, готувала втечу? Ні, усе сталося несподівано. Убивши наглядача, вона зрозуміла, що перейшла якусь межу. Усі її подальші дії були суцільною імпровізацією. Вона рвалася до стіни, але не вірила, що втеча вдасться."
"Крізь скляні двері світило сонце, перетворюючи бризки крові на подобу вітража."
"Можливо, Савен тверезо оцінив свої шанси й зрозумів: йому не виграти змагання й не стати королівським захисником. Навіть така смерть бачилася йому кращим виходом, ніж повернення в ті місця, звідки його привезли сюди. Якби він справді хотів утекти, він би напевно дочекався темряви й знайшов би інше місце, де менше вартових."
"Ні, Савен просто хотів довести собі, що здатен на це. Хто-хто, а Селена дуже добре розуміла його відчайдушний вчинок. Її ж теж зупинили зовсім поруч зі стіною."
"І раптом вона зрозуміла, що рухало Савеном зараз і нею тоді. Вони обидва хотіли довести собі й навколишньому світові, що були й залишаються людьми. Адарланський король міг відібрати в них свободу, кинути на каторгу, знущатися, принижувати, вигадувати найдурніші змагання."
"Вони не були невинними жертвами, але, навіть будучи злочинцями, вони залишалися людьми. Савен не захотів бути пішаком у королівській грі й обрав смерть."
"Закляклі пальці Савена вказували на недосяжний горизонт. Селена мовчки прочитала молитву за його душу й побажала йому удачі в іншому світі."
#
"У той самий час"
"Дорін Хавільяр сидів на троні й відчайдушно боровся зі сном. Музика й гул розмов діяли заспокійливо, і спадковий принц то й діло розтирав важкі повіки. І навіщо мати вимагала його присутності на придворних асамблеях? Добре, що раз на тиждень, але й ці кілька годин були для нього мукою. І все ж краще сидіти на троні, ніж розглядати труп Глазопожирателя."
"Шаолу довелося займатися цим кілька днів поспіль. Дякувати капітанові, а то б спадковому принцу довелося самому розбиратися, що до чого. Тільки даремно Шаол стільки морочиться. Швидше за все, Глазопожиратель натрапив на п’яних гвардійців. Сказав їм щось образливе або посміявся. Зрозуміла річ: ніхто з цих бравих хлопців із повинною не з’явиться."
"А сьогодні — нова історія. Один із претендентів раптом вирішив утекти. Природно, варта зупинила його назавжди. Дорін подумки уявив собі картину втечі, і його пересмикнуло. Яке щастя, що знову Шаолу, а не йому доводиться копирсатися в усій цій каші, починаючи з тяжко пораненого гвардійця й закінчуючи радником, що виставив убитого претендента."
"І про що тільки думав його батько, влаштовуючи своє дурне змагання? Дорін глянув на матір. Їхні трони стояли поруч. Королеві нічого не повідомили про події. Вона б прийшла в жах. А тут було від чого прийти в жах. Георгіна все ще залишалася красивою, хоча на обличчі додалося зморшок і не всі їх можна було сховати під пудрою, а в каштановому волоссі з’явилися сріблясті пасма."
"Сьогодні королева вбралася в пишну, з довгим шлейфом, сукню з зеленого оксамиту, накинувши поверх кілька золотавих повітряних шалей. Обличчя Георгіни ховала вуаль. Схоже, королеві хотілося відгородитися від придворного світу, спорудивши щось на кшталт шатра."
"А в залі, як завжди, снували придворні: одні рухалися степенно, інші — нишком, перебігаючи від однієї групки до іншої. Усе як завжди: порожні розмови, суперництво, флірт, плітки. Оркестр, розташований у кутку, ліниво грав менует. Деякі придворні танцювали, решта воліли сидіти, і навколо них ганяли слуги, пурхаючи з срібними підносами й кришталевими келихами."
"Дорін відчував себе живою лялькою. Ще вранці мати надіслала йому наряд, і він слухняно вдягнув блакитно-зелений оксамитовий камзол із дурнуватими пишними білими рукавами. На щастя, панталони виявилися світло-сірими. А от замшеві черевики каштанового кольору виглядали занадто новими, і це дещо зачіпало чоловічу гордість принца."
G "Доріне, хлопчику мій, ти зовсім засинаєш."
"Він стрепенувся й відповів вибачливою усмішкою."
G "Учора я отримала листа від Холліна. Він передає тобі найкращі побажання й пише, що любить свого старшого брата."
pr "А про щось цікавіше він пише?"
G "Тільки про те, що школа йому ненависна, він спить і бачить, як повернеться додому."
pr "Це в нього в кожному листі."
"Королева зітхнула."
G "Якби твій батько не забороняв, я б давно повернула нашого малюка в Рафтхол."
pr "Школа йому на користь. Там є хоч якісь віжки."
"З Холліном — як і з батьком: чим далі вони від замка, тим краще."
G "Ти, коли ріс, не завдавав мені стільки клопоту. Не сварився зі слугами, не дерзив учителям. Бідолашний Холлін. Обіцяй мені, що, коли я помру, ти будеш про нього дбати."
pr "Помреш? Мамо, та тобі тільки…"
G "Я пам’ятаю, скільки мені років. І тому ти мусиш одружитися. Якнайшвидше."
pr "Одружитися? Навіщо мені одружуватися?"
G "Не забувай, ти — спадковий принц. Тобі вже дев’ятнадцять років. Невже ти хочеш стати королем, у якого не буде спадкоємців? Згоден поступитися троном Холліну?"
"Дорін мовчав."
G "Іноді мені здається, що тобі й королем-то не хочеться бути. Навколо тебе стільки прекрасних дівчат із хороших родин. Невже ти не можеш обрати собі гідну дружину? Звісно, краще було б одружитися з принцесою."
pr "Ти сама знаєш: принцес не залишилося."
G "Окрім принцеси Нехемії. Не заперечуй мені. Я ж не примушую тебе на ній одружуватися. Дивно, що твій батько дозволив їй зберегти цей титул. Але дівчина вона гордовита й свавільна. Я надіслала їй розкішну сукню, а вона відмовляється її вдягати. Чи чувано таке?"
pr "Мабуть, у принцеси є на те свої причини. Я з нею трохи поговорив. Знаєш, вона не здалася мені гордовитою. Жвава, безпосередня дівчина. Не те що здешні кривляки."
G "Раз ти її хвалиш, чому б тобі на ній не одружитися?"
"Засміялася королева, не давши синові відповісти. Дорін мляво усміхнувся. Він досі не розумів, чому батько раптом погодився, щоб дочка короля Ейлуе вирушила до адарланського двору вивчати мову й звичаї Адарлана. Судячи з відгуків посланців, Нехемія була не найкращим вибором."
"До принца доходили чутки про її допомогу ейлуейським повстанцям. Крім того, Нехемія наполегливо домагалася скасування каторжного поселення в Калакуллі. Побувавши в Ендов’єрі й побачивши, що соляні копальні зробили з Селеною Сардотін, Дорін не докоряв принцесі за прагнення допомогти співвітчизникам."
"Однак навіть коротка розмова з Нехемією залишила в нього відчуття, що в неї є й якісь інші, таємні мотиви приїзду в Рафтхол."
G "Як шкода, що на пані Кальтену вже має види герцог Перантгон. Така чудова дівчина й така вихована. Може, у неї є сестра."
"Дорін склав руки на грудях, намагаючись не показувати свого огиди. Кальтена перебувала в дальньому кінці зали й звідти пожирала очима принца. Від довгого сидіння в Доріна затерпіла спина, і він почав звиватися на троні."
G "А що ти скажеш про Елаїзу? Вона така мила, а часом буває дуже грайливою."
"‘Це, матусю, я й без тебе знаю’."
pr "Елаза наганяє на мене нудьгу."
"— Доріне, ти міркуєш, ніби тобі десять років. Тільки не кажи, що збираєшся одружуватися з любові. Любов хороша в романах. Міцного й щасливого шлюбу з любові не дочекаєшся."
"До чого ж йому все це набридло! Щоразу одні й ті самі розмови з матір’ю під мерехтіння чемно усміхнених чоловічих і жіночих облич. Нудьга, нудьга на кожному кроці."
"Принц думав, що поїздка в Ендов’єр розворушить його й він рахуватиме дні до повернення додому. За ці місяці нічого в замку не змінилося. Ті самі придворні дами, які й досі дивляться на нього благальними очима. Ті самі смазливі служнички, що зухвало підморгує йому."
"Ті самі радники, що вручають свої довжелезні закони й статути з принижувальними проханнями «викроїти хвилинку» й прочитати їхню писанину… І батько, одержимий завоюванням нових і нових земель. Король не заспокоїться, поки над кожним континентом не майорітиме прапор Адарлана."
"Навіть ці змагання за титул королівського захисника перетворилися на тяганину. Доріну й так було ясно, що під кінець залишаться тільки Селена й Кейн. Усі інші претенденти його анітрохи не цікавили."
G "Щойно ти був готовий заснути, а тепер хмуришся. Хлопчику мій, ти чимось засмучений? Є якісь звістки від Рузанди? Бідний мій малюк — вона розбила твоє серце!"
"Дорін не знав, куди втекти від материнських причитань і трагічних жестів."
G "Але ж це сталося більше року тому…"
"Принц мовчав. Він не хотів думати ні про Рузанду, ні про того мужлана, якого вона віддала перевагу спадковому принцу й заради якого втекла з замка."
"Оркестр загравав іншу мелодію, і бажаючих танцювати стало більше. Придворні закружляли, виділяючи замислуваті па. Серед танцюристів було достатньо ровесників Доріна, але йому здавалося, що він дивиться на них звідкись здалеку. Ні, принц не відчував себе ні старшим, ні мудрішим. Просто він відчував…"
"Він відчував, ніби всередині нього живе зовсім інша людина, якій остогидли й придворні забави, й відверте небажання його ровесників хоч щось знати про світ за стінами замка. Той, інший, не мав жодного діла до титулу спадкового принца."
"Підлітком Дорін дуже любив бали й галасливі компанії, але поступово почав розуміти, що живе в двох світах. І ж бо ніхто цього не помічав. Так, він не такий, як інші. Але він же спадковий принц… Якби не Шаол, Доріану було б дуже самотньо."
"Королева клацнула білими пальцями, підкликаючи фрейліну, і сказала синові:"
G"Я знаю: батько залишив тобі безліч доручень. Але я сподіваюся, що в тебе все ж знайдеться час подумати й про мене. І тоді ти уважно вивчиш ось це."
"Прилетіла фрейліна зробила глибокий реверанс і подала принцу складений аркуш щільного пергаменту, скріплений яскраво-червоною материнською печаткою. Дорін одразу зламав печатку, і в нього звело живіт від довгої низки імен дівчат із знатних родин, що досягли шлюбного віку."
pr "Що це?"
"Королева тріумфально усміхнулася."
G "Список тих, кому ти міг би запропонувати руку й серце. Кожна з них гідна руки спадкового принца. І кожна, як мені казали, здатна народити міцних і здорових спадкоємців."
"Дорін поспіхом запхав список у кишеню камзола. Нудьга, супроводжувана незрозумілим неспокоєм, анітрохи не зменшилася."
pr "Я подумаю."
"Кинув він матері й, не давши їй розкрити рота, зійшов із трону. Принца одразу оточила зграйка юних придворних дам. Одна пропонувала йому потанцювати, друга питала про його здоров’я, третя цікавилася, чи має він намір відвідати бал-маскарад, що відбудеться через місяць, у ніч Самуїнна."
"Їхні щебетливі голоси зливалися в один. Хто ці тріщалки? Доріан не міг згадати імені жодної з них."
"Геть, швидше геть звідси! Доріну стало задушно. Якщо він зараз же не піде, то задихнеться. Його губи промовляли завчені слова прощання, а ноги несли його геть. Приготований матір’ю список наречених здавався йому головешкою, що загрожувала пропалити камзол і дістатися до тіла."
"Засунувши руки в кишені, Дорін блукав коридорами замка. Псарні спорожніли. Частину гончаків король забрав із собою, а решту гвардійці пустили по сліду, все ще сподіваючись знайти вбивць Глазопожирателя. Принц хотів було зайти на псарню й поглянути на одну з вагітних сук."
"Але що толку дивитися на її роздутий живіт і гадати, яким буде виводок? Раніше, ніж цуценята народяться, цього ніхто не скаже. Він сподівався на чистоту виводка, хоча мамаша була схильна тікати з псарні. Доріан пишався цією гончою — найшвидшою з усіх, однак ніяке дресирування так і не змогло подолати її буйну тягу до свободи."
"Дорін не знав, куди й навіщо йде. У русі йому було легше. Дурний камзол! Принц розстебнув верхній ґудзик і тут почув дзвін мечів. Він сам не помітив, як підійшов до зали, де змагалися претенденти. Але чому вони досі займаються? Невже Брулло змусив?"
"Дорін зупинився біля дверей і раптом помітив Селену. Точніше, спочатку він помітив колихаючі хвилі її золотавого волосся. Меч здавався продовженням її руки. Селена вела поєдинок одразу з трьома вартовим, спритно маневруючи між ними."
"Зліва хтось кілька разів сплеснув у долоні, і поєдинок припинився. Селена й вартові важко дихали. Майбутня королівська захисниця усміхалася. По лобі й щоках текли цівки поту, а сині очі весело блищали. Зараз вона була просто красунею, але…"
"На мить принц забув про Селену. До учасників змагання повільно йшла принцеса Нехемія. Замість звичної білої сукні на ній була темна блуза й просторі штани. У руці принцеса тримала красиву різьблену палицю."
"Нехемія схвально поплескала Селену по плечу й щось сказала. Селена засміялася. Дорін глянув по боках. Де Шаол? Де Брулло? Чому одна з найнебезпечніших адарланських убивць перебуває тут разом з ейлуейською принцесою. І чому в неї в руці меч? Їм що, мало невдалої втечі?"
"Дорін увійшов до зали. Він із усмішкою вклонився принцесі. Нехемія відповіла ледь помітним кивком. Нічого дивного. Дорін узяв Селену за руку. Долоня пахла потом і металом, проте принц поцілував її."
pr "Добридень, пані Ліліана."
c "Добридень, ваша високосте."
"Селена спробувала висвободитися, але принц міцно стискав її мозолисту долоню."
pr "Дозвольте вас на пару слів."
"Не дочекавшись її згоди, він відвів Селену на кілька кроків."
pr "Де Шаол?"
"Cуворо запитав Дорін. Селена стала в свою улюблену позу — склавши руки."
c "Це ви так розмовляєте зі своєю захисницею?"
"Але відчувалося, що принцу не до жартів."
pr "Де капітан?"
c "Я не знаю. Якби мені довелося битися об заклад, я б поставила на те, що він зараз розглядає понівечений труп Глазопожирателя або віддає розпорядження про таємне поховання тіла Савена. І потім, Брулло після занять сказав, що я можу залишатися тут і вправлятися, скільки забажаю. Завтра у нас — друге випробування. Сподіваюся, ви пам’ятаєте."
"Це Дорін пам’ятав."
pr "А чому тут перебуває принцеса Нехемія?"
c "Вона посилала по мене. Фаліпа їй розповіла, де я, і принцеса побажала сюди прийти. Її-то вам нема чого боятися."
"Селена насмішкувато дивилася на нього, покусуючи нижню губу."
pr "По-моєму, ти ніколи не вирізнялася балакучістю."
c "Ви ж не удостоювали мене розмовами. Та й капітан не був схильний до бесід."
pr"А коли мені було удостоювати тебе розмовами?"
c "Нехай ваша високість пригадає такий дріб’язок, як наша спільна подорож із Ендов’єра. І потім, я вже два тижні перебуваю у вашому замку."
pr "Але ж я надіслав тобі книжки."
c "І не потрудилися запитати, чи прочитала я їх."
"Зухвала дівчисько! Вона що, забула, з ким говорить?"
pr "Зажди, один раз я з тобою говорив. Невдовзі після нашого приїзду."
"Селена знизала плечима й відвернулася, збираючись відійти. Розгніваний і трохи заінтригований такою поведінкою, Дорін схопив її за руку. Бірюзові очі Селени спалахнули. Вона подивилася на свою полонену долоню, потім перевела погляд на обличчя Доріна."
c "Ви мене не боїтеся? Чи ви так само вміло б’єтеся, як капітан Естфол?"
"Принц ступив ближче й ще міцніше стиснув Селені зап’ястя."
pr "Ще краще. (пошепки на вухо)"
"Вона заморгала й почервоніла."
c "Знаєте що..."
"Пробурмотіла вона, але момент був втраченийЦей поєдинок принц виграв."
c "Ніколи б не подумала, ваша високосте. Прийму до відома."
"Дорін церемонно вклонився."
pr "Роблю те, що в моїх силах. Ти можеш вправлятися тут хоч до ночі, а от принцесу я з тобою не залишу."
c "Це чому ж? З якої стати мені вбивати єдину жінку, у якої є мізки? Я по горло сита придворними дурепами."
"Мабуть, подумки вона додала: «І дурнями». Може, і їх із Шаолом ця шалена дівчисько вважає такими?"
c "Чого ви боїтеся, принце? Ви забули про її охоронців? Та вони змелють мене раніше, ніж я підніму руку на їхню господиню."
pr "Це порушує етикет. Вона приїхала вивчати наші традиції, а не змагатися."
c "Вона — принцеса й може робити все, що забажає."
pr "А ти, як я бачу, вирішила навчити її мистецтву поєдинку."
c "Ви просто мене побоюєтеся."
pr "Я проведу принцесу до її покоїв."
c "Чорт вам у поміч, ваша високосте!"
"Дорін поправив волосся й підійшов до принцеси. Нехемія стояла, уперши руки в боки. Принц подав знак її охоронцям наблизитися."
pr"Ваша високосте. Мені дуже шкода, але я змушений провести вас до ваших покоїв."
"Принцеса всім своїм виглядом показувала, що не розуміє його слів. І тоді Селена заговорила з нею ейлуейською мовою. Ледь дослухавши її, принцеса вдарила палицею об мармурову підлогу й почала щось швидко говорити Доріну."
"Її мова нагадувала шипіння роздратованої змії. Принц із гріхом пополам ще розумів повільну ейлуейську мову, але з цього фиркання не зрозумів ні слова. Селена послугово переклала йому слова Нехемії."
c "Принцеса каже, що вам краще повернутися до ваших танців і м’яких подушок, а ми тут знайдемо чим зайнятися."
"Дорін тримався з останніх сил, зберігаючи серйозне обличчя."
pr "Поясни принцесі, що їй за статусом не належить брати участь у таких змаганнях."
"Селена промовила кілька фраз. Нехемія махнула рукою й відійшла на дюжину кроків до стійки зі зброєю."
pr "Що ти їй сказала?"
"— Я сказала, що ви з радістю погодилися бути її першим партнером по навчальному поєдинку. Ваша високосте, не впирайтеся. Не розчаруйте принцесу."
pr"Я не буду з нею змагатися."
c "А зі мною?"
pr "Можливо. У твоїх покоях. Сьогодні ввечері."
c "Я чекатиму."
"Усміхнулася Селена, кокетливо намотуючи пасмо на палець. Принцеса стояла, швидко й уміло крутячи своєю різьбленою палицею. Прийомів проти цієї зброї ейлуейців Дорін не знав. Йому раптом здалося, що витончена Нехемія не тільки виб’є меч із його руки, а з такою ж легкістю виб’є з нього дух."
"Дорін підійшов до стійки зі зброєю й узяв два дерев’яні мечі."
pr "А може, для початку скористаємося цим?"
"Принцеса не вперлася. Свою грізну палицю вона віддала охоронцеві й узяла в Доріана дерев’яний меч для навчальних поєдинків. Селені не вдасться виставити його дурнем!"
pr "Ставайте там."
"Сказав він принцесі, а сам зайняв оборонну позицію."

#Епізод 10

"Селена дивилася, як спадковий принц Адарлана показує ейлуейській принцесі основи бою на мечах, і посміхалася. Принцу не можна було відмовити в чарівності. Тільки вона мала відтінок зверхності. Втім, інший спадковий принц, засліплений блиском свого титулу, поводився б набагато гірше. Найбільше Селену бентежило те, з якою легкістю Доріан змусив її почервоніти. Він був настільки гарний собою, що вона не могла думати ні про що, крім його шарму. І чому він досі не одружений?"
"Принцеса Нехемія зробила випад і вдарила Доріана мечем по руці. Селена прикусила губу, щоб не розреготатися. Принц зараз був схожий на хлопчиська, якому не пощастило в бійці. Він скривився, потер подряпину на зап’ясті, але зумів сховати образу поглибше й усміхнувся. Принцеса злорадно посміхалася."
"‘Чортова чарівність! І на кого ти тільки народився таким красенем!’"
"Селена притулилася до стіни. Це було рідкісне видовище. Найяскравіше за всі дні її життя в замку."
"Розвагу перервало несподіване появи Шаола. Капітан боляче схопив Селену за руку."
"— Що все це означає? — запитав він, розвертаючи Селену обличчям до себе."
"— Що саме?"
"— Чим вони з Доріаном займаються?"
"— А ти не бачиш? У них навчальний поєдинок."
"— Чому в них дійшло до навчального поєдинку? — не відставав капітан."
"— Тому що принц викликався показати принцесі, як треба битися на мечах."
"Шаол відштовхнув Селену й підійшов до високородних супротивників. Бій припинився. Шаол відвів Доріана в куток. Звідти долинули уривки поспішних сердитих фраз. Потім капітан знову підійшов до Селени й сказав:"
"— Караульні відведуть тебе до твоїх покоїв."
"— Що? — Селена згадала їхню недавню, зовсім дружню розмову на балконі й здригнулася. — Завтра випробування, і мені ще треба вправлятися."
"— По-моєму, ти сьогодні достатньо вправлялася. Ти знаєш, котра зараз година? Ваші заняття в Брулло закінчилися пару годин тому. Тобі треба як слід відпочити, інакше завтра ти будеш ні на що не придатна. І не приставай до мене з розпитуваннями. Я нічого не знаю про особливості завтрашнього випробування."
"— Ну що за безглуздя! — спалахнула Селена."
"Шаол боляче ущипнув її за руку, змусивши замовкнути. Нехемія насторожено глянула в їхній бік, але Селена махнула їй, пропонуючи продовжувати урок зі спадковим принцом."
"— Ти зовсім з’їхав з глузду, товстошкіре чудовисько? Я просто стояла й дивилася. Я не знаю й не хочу знати, які підозри бродять у твоїй голові."
"— А ти наївна простачка, яка не розуміє, чому ми не дозволяємо вам із принцесою розважатися поєдинками?"
"— Розумію. Ти мене боїшся, ось і весь сказ."
"— Ти надто високої думки про себе."
"— Капітане, я поки що ще не з’їхала з глузду. Думаєш, я мрію повернутися в Ендов’єр? — сердито запитала Селена. — Чи ти думаєш, що я не уявляю всіх наслідків втечі? Я не хочу бути дичиною й усе життя петляти, заплутуючи сліди. Чи ти думаєш, я не розумію, чому мене вивертає, коли ми з тобою бігаємо щоранку? Так тому, що моє тіло ще не оговталося після соляних копалень. Мені треба не тільки їсти й спати. Мені треба набирати сили й відновлювати втрачені навички. Тобі б мене підтримати, а ти…"
"— Нехай я не знаю, як у злочинців народжуються їхні замисли, зате я знаю інше: злочинці завжди думають про втечу."
"Селені хотілося порубати його на шматки, але замість цього вона почала молотити руками повітря."
"— До цього моменту я почувалася винною. Нехай зовсім трішки, але винною. Ти мене позбавив цього почуття. Я ненавиджу сидіти в клітці! Навіть у розкішній клітці з кількох кімнат, де від нудьги можна з’їхати з глузду. Ненавиджу караульних і всю цю придворну маячню. Ненавиджу тебе, коли ти велиш мені не виділятися з натовпу. Брулло відкрито вихваляє Кейна. Це можна. Кейну можна показувати, на що він здатен, а мені не можна, так? Я маю сидіти в куточку й не привертати до себе уваги. Ненавиджу ваші нескінченні «не можна»! І найбільше я ненавиджу тебе!"
"Капітан притупнув ногою."
"— Усі слова вивергла?"
"У його погляді не було й натяку на доброту. Ідучи, Селена стискала кулаки, мріючи вп’ястися капітанові в горлянку."
"Кальтена сиділа в кріслі біля каміна. Звідти їй було зручно спостерігати за герцогом Перангоном. Герцог стояв біля тронного подіуму й бесідував із королевою. Як шкода, що Доріан пішов годину тому й їй не вдалося перекинутися з ним хоча б кількома словами. Кальтена досадливо кусала губи. Вона майже все ранку провела в приготуваннях, вибираючи вбрання й зачіску. А як гарно їй уклали волосся! Синьо-чорні локони обрамляли її обличчя із золотавою шкірою. Звичайно, шкіра Кальтени не була золотавою від природи, але те, чого не існувало в природі, з лишком компенсували всілякі пудри, помади, рум’яна та інші засоби з арсеналу краси. Нехай туге шнурування корсета на її жовто-рожевій сукні загрожувало зламати їй ребра, а нитки перлів і діамантів стискали шию, Кальтена стійко переносила ці тяготи й змушувала себе невимушено усміхатися. Хоча Доріан і пішов, зате в залі несподівано з’явився Перангон. Це був по-справжньому подарунок долі, бо герцог рідко відвідував придворні асамблеї."
"Час нагадати про себе. Кальтена церемонно підвелася з крісла. Дивно, що герцог її не помітив. Ймовірно, він кудись поспішав, бо попрощався з королевою й пішов до дверей. Кальтені не залишалося нічого іншого, як опинитися на його шляху. Очі Перангона одразу стали голодними. Кальтена стиснулася всередині, переконуючи себе, що всі чоловіки однакові."
"— Вітаю вас, пані Кальтена, — промовив герцог, відвівши їй низький уклін."
"— Добридень, ваша світлосте, — усміхнулася вона, намагаючись якомога глибше сховати своє огиду до герцога."
"— Сподіваюся, ви перебуваєте в доброму здоров’ї, — сказав Перангон, пропонуючи їй руку."
"Кальтена знову усміхнулася й прийняла його руку. Герцог мав внушительний животик, однак руки залишалися сильними."
"— Дякую, ваша світлосте. Ну як можна не бути в доброму здоров’ї, перебуваючи в такому дивовижному місці? А як ви? Мені здається, я цілу вічність вас не бачила. Ваша поява тут — на рідкість приємний сюрприз."
"Перангон обдарував її завченою усмішкою."
"— І я сумував за вашим товариством, пані Кальтена."
"Вона постаралася не скривитися від дотику м’ясистих волохатих пальців герцога до її дорогоцінної шкіри й навіть нахилила до нього голову."
"— Сподіваюся, що й її величність теж перебуває в доброму здоров’ї. Ваша бесіда з нею була приємною?"
"Займатися подібними розпитуваннями було небезпечно, особливо враховуючи, що її перебування в замку повністю залежало від милості герцога. Кальтена познайомилася з ним минулої весни й вважала це рідкісною удачею. Добитися від нього запрошення до двору особливих зусиль не склало. Кальтена знала, що герцог любить прогулюватися наодинці, і просто потрапила йому на шляху, попередньо відчепивши від себе пильну компаньйонку, приставлену до неї батьком. Однак Кальтена приїхала в замок не тільки заради насолоди придворним життям. Її не влаштовувала роль багатої провінційної нареченої, яку батько збирався видати заміж із вигодою для себе. Їй набридли провінційні сварки й місцеві дурні, готові виконувати будь-яку її забаганку."
"— Хвала небесам, королева на здоров’я не скаржиться, — сказав Перангон, супроводжуючи Кальтену до її покоїв."
"Вона йшла, придумуючи благовидні приводи, щоб розлучитися з герцогом біля дверей. У животі противно свербіло, ніби вона з’їла щось несвіже. Герцог не приховував, що хоче її. Правда, він не дозволяв собі загребти її своїми ручищами й завалити на постіль, але звик завжди отримувати бажане. Тим більше що вона сама йому натякнула, що віддячить за запрошення до столиці. Герцог одразу зрозумів натяк і тепер чекав нагоди нагадати Кальтені про дану обіцянку. Минулого разу вона відмовилася, пославшись на напад мігрені. Що ж придумати цього разу?"
"— Але в її величності є інші турботи. Мати не може не хвилюватися за сина-нареченого."
"Кальтена змусила себе спокійно вислухати це. Насамперед — спокій. Ну й ввічливе цікавість, ніби одруження принца стосується її остільки-поскільки."
"— Тож незабаром нас чекає радісна звістка про заручини його високості?"
"Це питання теж було з категорії небезпечних."
"— Я щиро на це сподіваюся, — пробурмотів герцог, однак його обличчя під копицею рудого волосся потемніло, а на щоці проступив зубчастий шрам. — Її величність склала внушний список претенденток на роль нареченої принца. Усі вони — з достойних родин. Королеву влаштувала б будь-яка з них."
"Герцог осікся, згадавши, з ким веде розмову. Кальтена затріпотіла віями, зображуючи повну незацікавленість."
"— Вибачте мою цікавість, — замуркотіла вона. — Я ні в якому разі не смію втручатися в справи королівської родини."
"Кальтена змусила себе погладити його пальці, від чого її серце закалатало ще сильніше. Що ж це виходить? Доріану вручено список наречених, схвалених королевою? Хто входить до того списку? І як їй… Ні, про це вона подумає потім. Зараз треба перш за все з’ясувати, хто стоїть між нею й короною, про яку Кальтена мріяла й яка їй часто снилася."
"— Тут нема за що вибачатися, — сказав герцог, і в нього заблищали очі. — Ходімо до вас. Розкажете, чим займалися всі ці дні."
"— Нічого примітного, якщо не рахувати знайомства з дивовижно цікавою молодою особою, — з удаваною байдужістю відповіла Кальтена."
"Вони йшли світлим коридором скляної частини замка."
"— Що за особа? — насторожився герцог."
"— Нова подруга Доріана. Він мені її представив як пані Ліліану."
"Герцог помітно напружився."
"— Ви з нею бачилися?"
"— Так. Вона дуже ввічливо мене зустріла."
"Брехати Кальтена вміла гладко й складно."
"— І давно принц вас із нею познайомив?"
"— Сьогодні, — продовжила брехати Кальтена. — Потім він був змушений нас залишити, а пані Ліліана зізналася мені, що Доріан до неї не байдужий. Я щиро бажаю, щоб вона значилася в списку королеви."
"Звичайно, Кальтена сподівалася ненароком щось вивідати про свою суперницю. Але почуте змусило її серце забитися втретє, тепер уже від радості."
"— Пані Ліліана? Ні, вона в списку королеви не значиться."
"— Бідолашка. Уявляю, як це розіб’є їй серце, — защебетала Кальтена, бачачи, що шия й обличчя Перангона помітно почервоніли, а сам він сердито задихав. — Ще раз кажу: не мені совати ніс у подібні справи, але менш як годину тому Доріан сказав…"
"— Що він сказав? — загримів герцог."
"Його гнів був спрямований не на Кальтену, а, звичайно, на так звану пані Ліліану. Як вчасно ця апетитна дурненька повідомила йому настільки цінні відомості."
"— Доріан зізнався, що дуже до неї прив’язаний. Можна сказати, він у неї закоханий."
"— Бути того не може!"
"— Накажете вважати його високість брехуном? — Кальтена зобразила благородне обурення. — Як усе це трагічно! Принц мусить розуміти: його батьки не погодяться на їхній шлюб."
"— Це не трагічно. Глупо це, ось що!"
"Вони зупинилися навпроти дверей, що вели до кімнат Кальтени. Гнів зробив герцога відвертішим, ніж слід було."
"— Це дурна, безрозсудна й неможлива затія."
"— Неможлива? Чому?"
"— Коли-небудь я поясню."
"Знизу, із саду, долинув переривчастий бій годинника. Перангон повернувся на їхній звук і сказав:"
"— Мене чекають на засіданні ради."
"Потім він нахилився до вуха Кальтени, обдаючи її гарячим і вологим диханням, і шепнув:"
"— Можливо, я навідаюся до вас вечірком?"
"Перш ніж піти, Перангон провів рукою по її сідницях. Кальтена провела його поглядом і, коли він зник за поворотом, бридливо здригнула плечима. Вона зовсім не жадала сьогодні ввечері приймати в себе цього хтивого пузана. Але якщо з його допомогою вона стане ближчою до Доріана…"
"Кальтені ще належало з’ясувати, хто її суперниці, але спочатку треба докласти зусиль і відірвати кігтики Ліліани від принца. Входить ця зарозуміла дівка в список чи ні, а загрозу вона становить. І якщо герцог теж ненавидить Ліліану, краще не сваритися з таким могутнім союзником. Він-то вже зуміє віддерти цю п’явку від Доріана."
"Ідучи на обід до Великої зали, Доріан і Шаол майже не розмовляли. Принцесу Нехемію благополучно повернули до її покоїв, де їй нічого не загрожувало. Обидва погодилися, що Селена повелася дурно, штовхнувши принца на поєдинок із Нехемією. Але й Шаолу не можна було залишати її без нагляду, тим більше що труп претендента нікуди б не втік."
"— Ви, здається, подружилися з цією Селеною, — холодним тоном зауважив принцу Шаол."
"— А ми ревнуємо? — усміхнувся Доріан."
"— Мене більше турбує ваша безпека. Вона вміє бути привабливою. Вона здатна вразити вас своїм розумом. Але при цьому вона не перестає бути асасином."
"— Те саме я чув від батька."
"— Ви це почуєте від будь-якої здорової на розум людини. Хоч вона й погодилася бути вашою захисницею, тримайтеся від неї подалі."
"— Нічого мені не наказувати!"
"— Це не наказ. Можете вважати мої слова наполегливою дружньою порадою."
"— Скажи, ну навіщо їй мене вбивати? Вона ж чудово знає, чим це закінчиться. Думаєш, їй не хочеться жити? Ще як хочеться. І їй подобаються знаки уваги з нашого боку. Якщо Селена досі нікого не вбила й не спробувала втекти, з якої стати вона наважиться на таку дурість зараз? Їй є що втрачати. — Доріан поплескав капітана по плечу. — Ти хвилюєшся більше, ніж треба."
"— А в мене посада така: хвилюватися за безпеку королівської родини."
"— Тоді до двадцяти п’яти років ти посивієш, і Селена точно тебе не полюбить."
"— Доріане, що за маячню ви кажете?"
"— По-моєму, вона вирішила трохи змінити спрямованість свого, скажімо так, асасинства. Навіщо ламати тобі шию, якщо можна розбити твоє серце? І тоді тобі мимоволі доведеться кинути її до в’язниці чи навіть убити."
"— Даремно, Доріане. Такі, як Селена, не в моєму смаку."
"Не бажаючи далі злити друга, Доріан змінив тему."
"— Я тут намагався зрозуміти, хто ж міг убити цього Глазопожирателя. І навіщо?"
"Золотисто-карі очі Шаола стали майже чорними."
"— Я пару днів розглядав його останки. Дуже точне слово."
"У капітана побіліли щоки."
"— Хтось вирвав у нього всі нутрощі й навіть… мізки. Залишилася понівечена шкіра. Я послав до короля гонця з донесенням, але сам не збираюся припиняти розслідування."
"— А я думаю, Глазопожиратель натрапив на п’яних гвардійців. Забіяк серед наших вистачає. Уже не знаю, чим він їх розлютив, але вони вирішили обійтися з ним так само, як він обходився зі своїми жертвами."
"Повторюючи свою версію, Доріан і сам почав у ній сумніватися. Він бачив сварки й бійки п’яних гвардійців. Бувало, навіть брав у них участь. Але він не пам’ятав, щоб гвардійці забили когось насмерть та ще й розполосували труп, витягнувши звідти все нутро. Десь у глибині заворушився страх."
"— Думаю, мій батько тільки зрадів загибелі Глазопожирателя."
"— Я сподіваюся."
"А страх не минав. Бажаючи прогнати його, Доріан усміхнувся й обійняв капітана за плечі."
"— Ти в нас допитливий. Обов’язково докопаєшся. Можливо, навіть завтра, — додав він, входячи разом із Шаолом до Великої зали."

#Епізод 11

"Селена зі зітханням грюкнула книгою. Як огидно все закінчилося! Вона встала й вийшла зі спальні, не знаючи, чим зайнятися. Мабуть, Шаол по-своєму правий, і не треба було влаштовувати поєдинок Нехемії зі спадковим принцем. Селені хотілося вибачитися перед капітаном, але те, як він поводився з нею… Вона міряла кімнату кроками. Звичайно, у капітана королівської гвардії є справи поважніші, ніж стерегти найвідомішу злочинницю Адарлана. Так, вона все розуміє. Їй зовсім не подобається бути жорстокою, але… капітан заслужив таке поводження."
"Селена злилася на свою поведінку в залі. Поводилася як дурна. Навіщо почала пояснювати капітанові, чому її вивертає щоранку. Наговорила купу різкостей. А він їй повірив? Чи, може, зненавидів після таких слів? Селена глянула на розпухлі й почервонілі пальці. Дотренувалася. Коли вона встигла перетворитися з найнебезпечнішої в’язниці Ендов’єра на таке жалюгідне створіння?"
"Звичайно, їй би зараз не себе жаліти, а подумати про завтрашнє випробування. І про вбитого Глазопожирателя. Селена, як могла, зігнула й розхитала всі дверні петлі, і тепер усі двері відчинялися зі скрипом. Якщо хтось до неї й проникне, вона почує заздалегідь. Їй удалося вкрасти в роззяви-портних кілька голок і сховати в шматку мила. З голок, якщо їх з’єднати, вийде маленька піка. Краще, ніж зовсім нічого, особливо якщо вбивця полює на претендентів. Селена різко смикнула руками, допомагаючи мозку позбутися тривожних думок. Вона попрямувала до кімнати для ігор і музикування. Звичайно, у карти сама з собою не пограєш, та й ганяти більярдні кулі радості мало."
"Її погляд упав на клавікорди. Селена любила музику. Їй подобалася влада звуків, здатних руйнувати й зцілювати, робити досяжним недосяжне й наповнювати героїзмом буденність."
"Обережно, ніби клавікорди були сплячою людиною, якої вона боялася розбудити, Селена підійшла до громіздкого інструменту. Висунула дерев’яну лавку. Та противно заскрипіла по підлозі, і Селена скривилася. Потім вона підняла важку кришку, сіла, поставила ноги на педалі й легенько натиснула обидві. Інструмент був достатньо старим; його клавіші кольору слонової кістки вже торкнулася жовтизна, а чорні клавіші нагадували дірки між зубами."
"Колись вона добре грала. Можливо, навіть дуже добре. Під час кожної їхньої зустрічі Аробінн завжди змушував її грати."
"Цікаво, він уже знає, що її вивезли з соляних копалень у Рафтхол? Якщо так, чи спробує він її звільнити? Селені досі було страшно допускати думки про можливого зрадника. Тоді навколо було стільки хиткого й неясного. Через два тижні після загибелі Саема вона втратила свободу й частинку себе самої."
"Саем. Як би він поставився до її полону? Якби Саем був живий, він би визволив її з королівської в’язниці раніше, ніж королеві доповіли б про затримання небезпечної злочинниці. Але Саем, як і вона, став жертвою зради. Думка про те, що Саема більше немає, часом била її навідмаш, перекриваючи дихання."
"Селена обережно торкнулася басової клавіші, але звук вийшов різким, смиканим, повним гніву й болю. Тоді так само обережно вона спробувала наіграти на високих нотах простеньку мелодію. З кутів відгукнулося відлуння, принісши з собою уривки спогадів. У кімнаті було настільки тихо, що музика здавалася недоречною."
"Потім вона заграла іншу мелодію, майже повністю складену з півтонів. Це був її давній етюд на швидкість пальців, який так і називався: «Чорні клавіші». Селена згадала, як доводила ним Аробінна, поки той не гаркнув: «Ти можеш зіграти щось інше?» Етюд вона пам’ятала, а от колишньої швидкості пальців не було. У двох місцях вона збилася, з досади вдавила педаль і зняла руки з клавіш."
"Але музика не відпускала, і тоді Селена заграла зовсім інше, де вже не було безтурботної веселості «Чорних клавіш». Перші акорди були скутими, але Селена продовжувала грати, і руки рухалися все впевненіше. Сумна, навіть скорботна мелодія, але її звуки робили з душею Селени те саме, що з тілом — гаряча вода й мило. Дивно, що її пальці не розучилися перебігати між білими й чорними клавішами, що після місяців темряви й рабства музика все ще жила й дихала в ній. І десь серед високих і низьких, швидких і протяжних звуків був Саем. Селена грала твір за твором, довіряючи музиці незбагненне, відкриваючи старі рани. Вона грала, і звуки були її порятунком і прощенням."
"Доріан завмер у дверях, боячись ворухнутися. Селена сиділа до нього спиною й навіть не підозрювала про його появу. Вона продовжувала грати. Принц не знав, коли ж вона його помітить. Мабуть, коли змовкне останній акорд. Але Селена грала так захоплено, що музикування могло затягнутися до ночі. Проти цього Доріан не заперечував. Він був готовий слухати її годинами. Прямуючи сюди, він просто хотів виконати дану обіцянку й, чесно кажучи, приголомшити цим Селену. Але замість небезпечної вбивці, поглинутої замислами втечі (Доріану здавалося, що вона продовжує мріяти про це), він побачив дівчину, яка довіряє свої секрети струнам клавікордів."
"При всьому чутті асасина Селена виявила присутність Доріана лише тоді, коли він сів поруч із нею на лавку."
pr "Ти прекрасно гра…"
"Її пальці запнулися й проїхалися по клавішах, змусивши інструмент страждати від гучних дисонансних нот. Селена скочила й кинулася до стійки з більярдними киями. І тільки тоді вона побачила, хто насмілився увірватися до її покоїв. Доріан міг заприсягтися, що її очі мокрі від сліз."
"— Що ви тут робите? — хрипко запитала вона."
"Принц подумки всміхнувся. Схоже, будь-якого іншого непроханого гостя чекало б частування більярдним києм."
pr "— Я прийшов один, без Шаола, — усміхнувшись, повідомив принц. — Тож можеш не хвилюватися. І звичайно, прошу вибачити за перерване музикування."
"На його подив, щоки Селени почервоніли. Занадто вже людська емоція для найвідомішої вбивці Адарлана, про холоднокровність якої ходили легенди. Його прихід приголомшив Селену, але це чомусь не порадувало Доріана."
"— Ти так чудово грала, що я не одразу наважився тебе потурбувати."
"— Дякую за комплімент, — сухо відгукнулася Селена."
"Вона попрямувала до стільця. Принц заступив їй шлях. Чутки зображували Адарланського асасина мало не велеткою. А тут — юна дівчина середнього зросту, але з дуже привабливою фігурою. Принц із задоволенням відзначив, що за цей час у Селени з’явилися властиві жінці округлості."
"— Що ви тут робите? — без жодної ввічливості повторила запитання Селена."
"Доріан зухвало усміхнувся."
"— Ми ж домовилися зустрітися ввечері в тебе. Невже забула?"
"— Я думала, ви жартуєте."
"— Я спадковий принц Адарлана, — нагадав Доріан, опускаючись на стілець біля каміна. — Жартувати мене відучили ще в дитинстві."
"— А вам дозволено тут перебувати?"
"— Що? Дозволено? Мені? Це ж мій замок, і в ньому я можу робити все, що мені заманеться."
"— Але ви не забули, хто я?"
"Навіть якби вона зараз схопила кий і всаджувала йому в груди, Доріан усе одно б не злякався."
"— Судячи з твоєї гри, ти вмієш не тільки швидко й холоднокровно вбивати."
"— Як це розуміти?"
"— А так, — відповів принц, намагаючись не загубитися в її дивних, притягальних очах. — З тебе зробили вбивцю. Асасину душа не потрібна. Душа тільки заважає вбивати. Але, судячи з твоєї музики, душу в тебе відібрати не змогли. І ти не просто безжальна виконавиця замовлень на вбивства."
"— Звичайно, у мене є душа. Вона є в усіх."
"Щоки Селени залишалися червоними. Невже його несподівана поява так на неї подіяла? Принц придушив усмішку."
"— Забув запитати: як тобі сподобалися ті книги?"
"— Дуже цікаві, — тихо відповіла вона. — Я отримала велике задоволення."
"— Радий чути."
"Їхні очі зустрілися. Селена відійшла подалі від його стільця."
"‘Можна подумати, що асасин тут не вона, а я!’ — подумки всміхнувся принц."
"— А як твої справи в залі? Готуєшся? Ніхто з претендентів тебе не ображає?"
"— Мої справи йдуть чудово, — відповіла Селена, але кутики її рота опустилися. — Точніше, йшли. Після сьогоднішньої події сумніваюся, щоб комусь захотілося ускладнювати собі життя."
"Доріан миттєво зрозумів: вона говорила про вбитого втікача. Точніше, про того, хто лише спробував стати втікачем."
"— Це Шаол наказав убити Савена? — запитала Селена, покусуючи нижню губу."
"— Ні. Це був наказ мого батька — негайно стріляти по кожному з вас, хто спробує втекти. Сумніваюся, що Шаол взагалі віддав би такий наказ, — додав принц, сам не знаючи, навіщо це робить."
"Його слова трохи її заспокоїли. Страшна нерухомість її погляду почала зникати. Селена мовчала. Тоді принц з удаваною недбалістю запитав:"
"— А як тобі Шаол як партнер по змаганнях?"
"Запитання було цілком невинне. Селена невизначено знизала плечима. Цей жест міг означати що завгодно."
"— Мене влаштовує, — сказала вона. — Думаю, Шаол мене трохи ненавидить, але в його становищі це не дивно."
"— А чому ти думаєш, ніби він тебе ненавидить? — запитав Доріан."
"Дивно, але внутрішньо він погоджувався з її словами."
"— Тому що я — асасин, а він — капітан королівської гвардії й мусить принижуватися, возячись із претенденткою на титул захисника його величності."
"— А ти хотіла б, щоб усе було навпаки?"
"Доріан мляво усміхнувся. Запитання вийшло не таким уже й невинним."
"Селена наблизилася на пару кроків, і в принца закалатало серце."
"— Кому хочеться бути предметом ненависті? Втім, я краще віддам перевагу бути ненавидженою, ніж невидимою, — промовила вона слова, що склалися в дивний каламбур. — Але особливої різниці немає."
"— Тобі самотньо? — запитав Доріан і майже одразу пошкодував про своє запитання."
"— Самотньо? — перепитала Селена."
"Тільки тепер вона наважилася сісти, і то на стілець, що був подалі від принца. Доріан боровся з бажанням підійти ближче й доторкнутися до її волосся. Невже вони справді такі шовковисті, як здається?"
"— Ні, ваша високосте. Мені не самотньо. Я цілком умію себе займати, особливо якщо в мене достатньо книг."
"Доріан дивився на полум’я в каміні, намагаючись не думати про жахливе місце під назвою Ендов’єр. Він уявив, яке пронизливе самотність відчувала Селена там, де не було не тільки книг, а й багато чого іншого, без чого людське життя опускається до рівня скотського існування."
"— І все ж я сумніваюся, щоб тобі постійно вистачало товариства самої себе."
"— Ви хочете це виправити? — засміялася вона. — Мене анітрохи не приваблює стати однією з ваших коханок."
"— А що в цьому поганого?"
"— Мені достатньо слави асасина. А прославитися тим, що якийсь час ділила ложе зі спадковим принцем, — це не моє."
"Принц виразно кашлянув, але Селена продовжила:"
"— Вам потрібні пояснення, чому я не прагну до вас у постіль, чи достатньо сказати, що мої почуття не продаються за коштовності й дрібнички?"
"— І вона ще буде міркувати про моральність! — не витримав Доріан. — А людей ти вбивала за гроші чи з любові до ремесла?"
"Погляд Селени став жорстким."
"— Не смію затримувати вас, ваша високосте, — сказала вона, вказуючи на двері."
"— Ти мене… проганяєш?"
"Доріан не знав, сміятися йому чи злитися."
"— Накажете покликати Шаола? Вряд чи він зрадить, побачивши спадкового принца наодинці з асасином."
"Селена тріумфально склала руки на грудях. Вона знала, що в цьому поєдинку перемога дісталася їй. Їй навіть подобалося дивитися на приголомшеного Доріана, якому не було що сказати."
"— Дивно в нас із тобою виходить. Ти звинуватила мене в розпусті, і це в порядку речей. Але щойно я сказав правду про особливості твого ремесла — і ти готова мене вигнати."
"Ось воно, справжнє розвага, про яке він давно мріяв! Їхня сутичка коштувала сотень придворних асамблей і карнавалів."
"— Прогнати мене ти не можеш — замок належить мені. Замість того, щоб спопеляти мене очима, краще розкажи про своє життя. Де ти так чудово навчилася грати на клавікордах? І що за твір ти грала останній? У ньому було стільки смутку, ніби ти думала про свого таємного коханого, — сказав Доріан і підморгнув."
"— Мене вчили грати, як учать будь-яку дитину. Спочатку я ненавиділа клавікорди. Мріяла розрубати їх сокирою. Потім щось стало виходити."
"Селена встала й, підійшовши до дверей, зітхнула:"
"— Ви праві, я думала про нього."
"— Щось до вечора в тебе колючки виросли, — усміхнувся принц і теж встав."
"Він зупинився неподалік від Селени."
"— Удень ти була балакучішою, — зауважив він."
"— А я, ваша високосте, — не диковина, на яку ви можете витріщатися! — раптом кинула йому Селена, підходячи ближче. — І не придворна дурненька, що зачарувала вас на карнавалі. Мабуть, вам багато чого набридло в здешньому житті. Але я не предмет для розваг і задоволення вашої пристрасті. Упевнена, це була головна причина, чому ви вирушили в Ендов’єр. А титул захисниці — так, для зовнішнього прикриття."
"— Що? — тільки й міг вимовити приголомшений Доріан."
"Селена плюхнулася в крісло."
"— Невже ви всерйоз думаєте, що я не здогадуюся, навіщо ви сюди прийшли? Поговорити про роман «Корона героя»? Вам цього мало. Вам самому хочеться пригод, про які там написано."
"— Мені й без тебе пригод вистачає, — пробурмотів Доріан."
"— Не лукавте, ваша високосте. Не намагайтеся переконати мене, що моя присутність у замку — звичайна подія, що тьмяніє на тлі придворного життя. Ви з дитинства по горло ситі цим життям. У вашому замку всі страждають від нудьги. Тому ваш батько й влаштував ці змагання. Я вже й так перебуваю у владі короля. Але ставати ще й вашою блазнею я не збираюся."
"Принц раптом відчув, що червоніє. Хто й коли дозволяв собі так його відчитувати? Батьки. Учителі, коли він був хлопчиськом. Але потім — ніхто. Ні радники, ні придворні й тим більше якась самовпевнена дівчисько."
"— Ти забула, з ким розмовляєш?"
"— Мій дорогий принце, — спокійно відповіла Селена, роздивляючись свої нігті, — ми тут одні. До зовнішніх дверей далеко. Нас ніхто не чує, і я можу говорити все, що хочу."
"Селена думала, що розлючений принц зараз накинеться на неї з кулаками чи вихопить меч. Але Доріан раптом почав голосно, безутримно реготати. У Селени спалахнули щоки, від чого її очі стали ще яскравішими. Відчайдушна дівчисько! Чи розуміла вона, як би він міг із нею вчинити, якби вона не була асасином? А чи розумів він, який гнів обрушать на нього батько й Шаол, якщо він забуде всяку обережність і дозволить пристрасті керувати собою?"
"— Я йду. Але я повернуся. І скоро."
"— Не сумніваюся, — сухо відповіла Селена."
"— Спокійної тобі ночі, Селена Сардотін."
"Доріан обвів очима кімнату й знову зухвало усміхнувся:"
"— Але перш ніж я піду, скажи: цей твій таємний коханий… він же не з замка?"
"Не можна, їй не можна було заїкатися про це. Очі Селени миттєво згасли."
"— Спокійної ночі, — крижаним тоном промовила вона."
"— Я не хотів тебе образити, — винувато сказав принц."
"Селена мовчки махнула рукою, дивлячись не на нього, а на вогонь. Щоб не погіршувати ситуацію, принц тихо підійшов до дверей і взявся за ручку. Двері заскрипіли."
"— Його звали Саем, — глухо, ніби здалеку, пролунав голос Селени."
"Вона все ще дивилася на гру полум’я."
"‘Його звали Саем’."
"— Що з ним сталося? — усе-таки запитав принц."
"— Він помер, — повернувшись до нього, з сумною усмішкою відповіла Селена."
"— Коли?"
"Доріан забув усю її різкість. Чорт забирай, якби він тільки знав, він би говорив про що завгодно, тільки не про це…"
"— Тринадцять місяців тому, — видавила з себе Селена."
"Душевний біль, що відбився на її обличчі, був миттєвим, але Доріан уловив цю мить, і в нього все стиснулося всередині."
"— Мені дуже шкода, — прошепотів він, розуміючи всю дурість цих порожніх слів."
"Вона знизала плечима, показуючи, що його співчуття нічого не змінює й не може змінити того, що сталося."
"— Мені теж… шкода, — сказала Селена, повертаючись до вогню."
"Тепер кожне слово ставало зайвим. І кожна хвилина перебування принца тут — теж."
"— Удачі тобі в завтрашньому випробуванні."
"Селена не відповіла. Доріан вийшов, тихо зачинивши двері."
"Її душу-роздираюча музика продовжувала звучати в ньому всередині, коли він повернувся до себе й підпалив материнський список потенційних наречених. Ця музика супроводжувала його за читанням у ліжку й змовкла лише тоді, коли він заснув."
"Селена втиснулася в кам’яну стіну замка. Ноги тремтіли, але почорнілими від смоли пальцями й такими ж чорними ступнями вона намагалася зачепитися за будь-яку виїмку й тріщину між кам’яними брилами. Брулло щось кричав їй і ще дев’ятнадцятьом претендентам, що дерлися вгору по стіні, але вітер відносив його слова, і тут, на висоті сімдесяти футів, їх не було чути. Один претендент взагалі не з’явився на випробування, і навіть його караульні не знали, куди він пропав. Може, йому й справді вдалося втекти. Краще вже ризикнути, ніж вляпатися в це дурне випробування. Скрегочучи зубами, Селена трохи підтягнула тулуб і лівою ногою намацала розколину."
"До мети цих божевільних лазінь залишалося ще двадцять футів у висоту й тридцять у довжину. Там, байдужий до тягот претендентів, майорів золотавий прапор. На словах випробування звучало просто: піднятися на висоту дев’яноста футів і забрати полотнище. Той, хто зуміє спуститися з прапором униз, отримає від Брулло схвальне поплескування по спині. Але це не звільняло решту від побачення з місцем, де знаходився прапор. Претендента, що опинився останнім, чекало повернення в пекло, з якого його на час визволили."
"Дивно, що ніхто з претендентів поки що не зірвався зі стіни. Можливо, їм допомагали балкони, карнизи вікон, ґрати й сітки, за які можна було вхопитися. Селена здолала ще кілька футів. У неї гули й саднили пальці. У таких справах краще не дивитися вниз. Аробінн годинами змушував її стояти на карнизі вежі, привчаючи не боятися висоти. Обливаючись потом, Селена досягла чергового віконного козирка й підтягнулася на руках. Козирок виявився достатньо широким, і це дозволяло їй трохи перепочити, а заодно глянути на своїх суперників."
"Звичайно, Кейн знову був попереду. Він обрав найлегшу для підйому ділянку стіни. Могила й Верин лізли слідом за ним. Нижче неї був Нокс. Майже врівень із ним ліз юний асасин Пелор. Решта, схоже, товпилися купою, заважаючи один одному. Кожному Брулло дав можливість обрати один допоміжний засіб: мотузку, шипи, особливі чоботи. Звичайно ж, Кейн віддав перевагу мотузці."
"Селена обрала жерстяну баночку зі смолою й не шкодувала про свій вибір. Зараз, коли вона закінчила привал і обережно підвелася на повний зріст, її просмолені руки й ноги слухняно прилипли до кам’яної стіни. Баночка висіла в неї на поясі. Перед тим як продовжити підйом, Селена додатково просмолила долоні. Унизу хтось скрикнув, але вона придушила цікавість. Вона знала, що обрала важчу ділянку, зате тут не було суперників. На легкій ділянці претенденти буквально відштовхували один одного."
"Ще кілька футів. Руки Селени, ніби щупальця, присмокталися до каменю. Пролунав новий крик, уже не сердитий, а відчайдушний. Потім вона почула глухий стук. Запанувала тиша, але тиша тривала лічені секунди. Тепер закричали глядачі. Хтось із претендентів зірвався й розбився на смерть. Глянувши вниз, Селена побачила тіло безжального вбивці на прізвисько Коса. До цих змагань він кілька років провів на каторзі Калакулли, куди його засудили за всі злодіяння. Селена здригнулася. Знову жертва, тепер уже жертва випробувань. Чи розуміли ті виряжені старі, що жертв сьогодні може бути більше? Чи їм байдуже? Заплатять програш і забудуть."
"Селена обхопила водостічну трубу й почала дертися по ній. На Кейна зловісно скалилася кам’яна горгулья, але колишнього солдата це не налякало. Він накинув на шию чудовиську мотузкову петлю й перелетів через ділянку гладкої стіни, опустившись на карниз. До прапора йому залишалося всього п’ятнадцять футів. На Селену це подіяло гнітюче, але вона змусила себе думати тільки про підйом і продовжила дертися по водостічній трубі."
"Претенденти, що лізли за Кейном, готувалися повторити його трюк. Звідти лунали сердиті крики. Селена знову відволіклася й побачила, що Могила влаштував затор. Мабуть, він не вмів кидати мотузку. Його петля не бажала затягуватися на шиї горгульї. Тоді Верин його обійшов, змусивши посторонитися, й легко «окільцював» статую своєю мотузкою. Нокс, що опинився позаду Могили, збирався зробити те саме, але Могила став кричати на нього, і злодій примирливо підняв руки. Усміхаючись, Селена дісталася до залізної скоби, що кріпила водостічну трубу. Ще трохи — і буде досягнуто рівень прапора. А там — тридцять футів по гладкій стіні."
"Перепочивши хвилинку, Селена полізла далі. П’ятнадцятьма футами нижче один із претендентів — колишній найманець — чіплявся за роги горгульї, збираючись закріпити мотузку на її шиї. Схоже, він знайшов шлях швидший — через зграю кам’яних чудовиськ. Далі йому треба було дістатися до уступу, що був у вісімнадцяти футах, і потім уже перебиратися до іншої зграї горгулій, де сперечалися Нокс і Могила. Найманець їй нічим не заважав. На водостічну трубу він не зазіхав, і Селена спокійно, дюйм за дюймом, продовжувала лізти вгору. Холодний вітер тріпав їй волосся."
"І тут вона почула крик Нокса. Селена глянула вниз і побачила, що Могила штовхнув злодія з їхнього спільного п’ятачка на шиї горгульї. Нокс повис на мотузці, обв’язаній навколо тулуба. Невдовзі він зіткнувся зі стіною, і мотузка туго натягнулася. Селена завмерла, бачачи, як Нокс відчайдушно шукає найменші вибоїни й щілини, щоб закріпитися на стіні."
"Але Могилі було мало просто спихнути суперника. Він нахилився, роблячи вигляд, що поправляє чобіт, і Селена побачила блиснувший на сонці ніж. Як він зумів сховати зброю й не попастися? В інший час Селена захопилася б його спритністю, але зараз їй було не до захоплення. Вона крикнула, попереджаючи Нокса. Вітер відніс її крик, і злодій нічого не почув. А Могила вже різав мотузкову петлю на шиї горгульї. Ніхто з претендентів, що були поруч, і не подумав втрутитися. Пелор зупинився, шукаючи можливість обійти Могилу. Усі розуміли: якщо Нокс упаде й загине, одним суперником стане менше, а якщо вони втрутяться, то ризикують завалити випробування. Селена знала: її це теж не стосується. Треба лізти далі. Однак якась сила прикувала її до місця."
"У тому місці, де опинився Нокс, йому було ні за що вхопитися. Ні карниза, ні горгульї. Гола стіна. Щойно Могила переріже мотузку, Нокс полетить униз."
"Мотузка була сплетена з дюжини жил, і ті, одна за одною, розчленовувалися під лезом ножа. Відчувши дивні ривки, Нокс задер голову й тепер із німого жаху стежив за асасином. Падіння вниз означало вірну смерть. Могилі залишалося перерізати ще три чи чотири жили, і він позбудеться суперника."
"Скрип мотузки перетворився на жалісний стогін. І тоді Селена заслизнула по водостічній трубі вниз."
"Метал труби здер їй шкіру на руках і ногах, але вона не відчувала болю. Найманець ледь встиг притиснутися до стіни, і Селена шумно опустилася на голову горгульї, вхопившись за її роги. Бачачи, що шия чудовиська вже обвита мотузкою найманця, Селена схопила інший кінець і обв’язала навколо себе. Мотузка була достатньо довгою й міцною. Поруч із горгульєю, на яку опустилася Селена, було ще чотири кам’яні чудовиська. Це давало простір для розбігу."
c "— Тільки торкнися мотузки, і я тобі кишки випущу, — пригрозила найманцеві Селена й приготувалася до ризикованого маневру."
"Вона почула відчайдушний крик Нокса, де злилися страх і лють. Мотузка, на якій гойдався злодій, з гучним тріском обірвалася. Селена перемахнула через спини горгулій і кинулася вниз."

#Епізод 12

"Вітер врізався в неї, обдаючи холодними струменями, але Селена цього не помічала. Уся її увага була прикута до падаючого Нокса. А він падав надто швидко й перебував надто далеко від її простягнутих рук."
"Зеваки внизу щось кричали. Сонячне світло танцювало на скляній поверхні замка, заважаючи дивитися. Але Нокс був уже зовсім поруч. Приголомшений, з широко розплющеними сірими очима. Він розмахував руками, ніби вірив, що вони перетворяться на крила."
"Селена впала на нього й ударилася так, що в неї перехопило дихання. Але тепер її руки міцно тримали Нокса за пояс. Удвох вони каменем неслися вниз, до стрімко наближаючої землі."
"Нокс ухопився за мотузку, однак Селені від цього легше не стало. Туго натягнута мотузка скрипіла, загрожуючи обірватися. Селена буквально вп’ялася в тулуб Нокса. Утримати його, тільки не розтиснути руки й утримати. Разом вони були живим маятником, і він, гойднувшись в один бік, тепер неминуче відхилявся в інший — до стіни. Селена ледь встигла повернути голову. Удар від зіткнення зі стіною припав на її плече й бік. Але зараз Селена думала тільки про свої руки, не дозволяючи їм розтискатися. І вона, і Нокс важко дихали. Обидва спітніли. Мотузка виявилася міцною й утримувала їх у тридцяти футах над землею."
"— Ліліано, — прошепотів Нокс, утикаючись обличчям у її волосся. — Боги небесні…"
"Знизу їх почали підбадьорювати криками, у яких потонули тихі слова Нокса. У Селени відчайдушно тремтіли руки, а всі думки були тільки про те, щоб утримати врятованого злодія. Їй здавалося, що всередині все нутрощі ходять ходуном. Вона дуже добре знала, чим це закінчується."
"Але те, що сталося, не звільняло Селену й Нокса від випробування. Їм обом тепер знову належало піднятися до місця, де знаходився прапор, а потім спуститися вниз. Решта претендентів, тимчасово забувши про випробування, стежили за порятунком Нокса. І тільки один, що перебував вище за всіх, продовжував лізти до прапора."
"Селена бачила, як Кейн схопив прапор і заревів, радіючи своїй перемозі. Він гордо розмахував прапором, явно насолоджуючись привітальними криками. Від злості й досади Селена стиснула зуби."
"Обери вона легку ділянку, перемога дісталася б їй. Вона б зуміла дістатися до прапора вдвічі швидше за Кейна. Але ж Шаол велів їй триматися в середині й не дуже показувати свої здібності. І потім, її підйом був набагато вражаючим і говорив про її навички. А Кейну особливих навичок не потрібно було. Так, як він, на стіну забрався б будь-який новачок, не навчений лазіння. Можливо, Селена й перемогла б у цьому випробуванні, але тоді вона точно не врятувала б Нокса."
"А що тепер? Чи вистачить їй часу? Нокс нехай забирається по мотузці, а вона полізе, як лізла: намазавши смолою руки й ноги. Немає нічого ганебнішого за друге місце. Селена думала про це, дивлячись, як Верин, Могила, Пелор і Ренальт долали останні фути, торкалися місця, де був прапор, і починали спуск."
"— Гей, Ліліано й Ноксе! Поспішайте! — крикнув їм Брулло."
"Селена похмуро глянула на головного зброяра й приготувалася до нового лазіння по стіні. Шкіра на пальцях і ступнях у багатьох місцях була здерта до крові. Коли Селена намацала виїмки й ступила туди, ноги відгукнулися пекучим болем. Обережно, дуже обережно Селена полізла вгору."
"— Вибач. Я завадив тобі, — видихнув Нокс, гойдаючись на мотузці й теж шукаючи, куди б поставити ноги."
"— Усе гаразд, — заспокоїла його Селена."
"Але самій їй було на рідкість кепсько. Після недавнього напруження вона ніяк не могла вгамувати тремтіння в усьому тілі. Клякнучи на вітрі, Селена полізла вгору. Як добиратиметься туди Нокс, її вже не хвилювало. Дурна, яка ж вона дурна, що вляпалася в це порятунок! І про що вона тоді думала?"
"— Вітаю, — сказав Шаол, відпиваючи ковток води. — Вісімнадцяте місце — зовсім непогано. У всякому разі, Нокса ти обскакала."
"Селена не відповіла. Вона мовчки водила напівз’їденою морквою по тарілці, добираючи рештки підливи. Відмити поранені руки й ноги від в’ївся смоли виявилося не так-то просто. Служницям довелося двічі наповнювати діжку гарячою водою. Селена витратила цілий шматок мила, і все одно на долонях залишалися чорні плями. Потім Фаліпа ще пів години мазала й перев’язувала їй рани. Тремтіння припинилося, але у вухах усе ще стояв передсмертний крик Косі й глухий стук його удару об землю. До того часу, коли вона закінчила випробування, тіло вже забрали. Загибель Косі врятувала Нокса від вибуття. Щодо Могили — Брулло його навіть не дорікнув. У цій грі брудні прийоми вважалися в порядку речей. А ніж, пронесений Могилою, — це теж у порядку речей?"
"— Ти дієш так, як ми й домовлялися, — продовжував Шаол. — Хоча твоє доблесне порятунок цього злодійчука навряд чи заслуговує схвалення."
"— Я ж усе одно програла, — буркнула Селена."
"Коли вона спустилася, Доріан привітав її й подякував за порятунок життя Нокса. Сам Нокс міцно обійняв її й довго бурмотів подяки. Тільки Шаол зустрів її похмурим поглядом. Вона порушила правила гри. Злодійці, що промишляє крадіжкою коштовностей, нема чого ризикувати собою, рятуючи чуже життя."
"У карих очах Шаола відбивалося післяобіднє сонце."
"— А хіба тебе не вчили програвати красиво й гідно?"
"— Ні, — похмуро відповіла Селена. — Аробінн казав так: друге місце — це чудовий титул для першого невдахи."
"— Аробінн Хемел? — перепитав Шаол, опускаючи склянку. — Ватажок асасинів?"
"Селена повернулася до вікна. А житло Аробінна знаходилося не так уже й далеко від замка. Дивно, що тільки зараз вона подумала про це."
"— А хіба ти не знав, що він був моїм учителем?"
"— Я забув, у кого ти… вчилася."
"Судячи з того, що Шаол чув про цю людину, Аробінн просто висік би Селену за те, що вона полізла рятувати якогось Нокса, ризикуючи своєю безпекою й місцем у змаганнях."
"— Він що, всі роки сам тебе навчав?"
"— Спочатку сам. А потім запрошував для мене вчителів з усієї Ерілеї. Мене вчили битися «вчителі рисових полів». Так їх у нас називали, бо вони родом з південного континенту, де росте рис. Мене вчили найкращі знавці отрут із джунглів Бугадана… Потім я вже сама їздила до вчителів. Аробінн навіть посилав мене до Мовчазних асасинів із Червоної пустелі. Він не рахувався з витратами й платив стільки, скільки просили."
"Селена підчепила нігтем нитку на рукаві халата."
"— Я вважала, що так і має бути. Я тоді взагалі нічого не розуміла в грошах. А ледь мені виповнилося чотирнадцять, Аробінн розповів, у яку суму йому обійшлося моє навчання, і додав, що чекає від мене відшкодування витрат."
"— Тож спочатку він тебе вчив, а потім змусив за все платити?"
"Селена знизала плечима, однак приховати спалах злості, викликаний запитанням Шаола, не змогла."
"— Така доля всіх сиріт, яких хтось чомусь навчає. Хіба з куртизанками поводяться інакше? Вони потрапляють у «заклади любові» зовсім дівчатками, а потім дізнаються, скільки грошей витрачено на їхнє харчування, навчання, одяг і так далі. І стають рабинями закладу, поки не розрахуються сповна."
"— Але це ж гидко! — мало не плюнув капітан."
"Він був сердитий, однак не на неї. Рідкісний випадок."
"— І ти виплатила Аробінну всі гроші?"
"Селена усміхнулася. Усмішка її була холодною, ледь торкнулася губ, але не досягла очей."
"— Уяви собі. Я виплатила йому все до останнього мідяка. А він потім за три години спустив мої гроші. Там було понад пів мільйона золотих монет."
"Шаол навіть підвівся, а Селена затовкала це спогад поглибше, де воно не викликало болю."
"— До речі, ти досі не вибачився, — сказала вона, змінюючи тему."
"— Не вибачився? За що?"
"— За вчорашні гидоти. Ти забув, як поводився в залі, та ще в присутності принцеси Нехемії?"
"Як Селена й думала, капітан проковтнув наживку."
"— Я не стану вибачатися за правдиві слова, — заявив він, сердито мружачись."
"— Ти поводився зі мною, ніби я не просто злочинниця, а ще й божевільна. І це ти називаєш правдою?"
"— Тобі нагадати твої слова? Ти заявила мені, що ненавидиш мене сильніше, ніж кого-небудь."
"— Так воно й було, — сказала Селена й раптом усміхнулася."
"Капітан теж усміхнувся. Він кинув у неї скибкою хліба, яку Селена спритно спіймала однією рукою й одразу кинула в нього. Капітан ліниво простягнув руку й спіймав літаючий хліб."
"— Ідіот, — сказала Селена, усміхаючись у весь рот."
"— Божевільна злодійка, — повернув їй комплімент Шаол."
"— Я всерйоз тебе ненавиджу!"
"— Це за що ж? До речі, не я зайняв вісімнадцяте місце."
"Селена роздула ніздрі. Капітанові довелося нахилитися, інакше кинута нею яблуко влучило б йому прямо в голову."
"Під вечір Фаліпа пошепки повідомила Селені страшну новину. Виявилося, що претендент, який не з’явився на випробування, зовсім не намагався втекти. Його знайшли на одній зі службових сходів. Тіло було сильно понівечене й розчленоване."
"Похмура атмосфера, викликана цим убивством, зберігалася протягом наступних двох тижнів. Два випробування пройшли своїм чередом і якось майже непомітно. Перше було на кмітливість, друге — на вміння йти по сліду. Селена пройшла обидва, не привертаючи до себе уваги й нікого не рятуючи. Хоча ні перед випробуваннями, ні під час них ніхто з претендентів не був убитий і не загинув, Селена постійно трималася насторожі. Шаол намагався переконати її, що два роздертих трупи — це просто нещасні випадки, причини яких обов’язково будуть розкриті."
"Однією з небагатьох радощів були успіхи Селени в бігу. Вона ставала все витриваліша й тепер могла бігти довше й швидше, зберігаючи рівне дихання. А ще вона навчилася майже не звертати уваги на глузування Кейна, які він регулярно відпускав з того чи іншого приводу. У всякому разі, у неї вже не виникало колишнього бажання вбити його будь-якою підвернувшоюся зброєю чи навіть голими руками. Спадковий принц більше не заглядав до неї. Селена бачила його лише під час випробувань. Там Доріан усміхався їй, а в Селени чомусь червоніли щоки й починало щипати в носі."
"Втім, їй було не до думок про принца. Її всерйоз турбувало найближче майбутнє. До завершальних поєдинків залишалося всього дев’ять тижнів, а претендентів на заповітні чотири місця було більше, ніж вона думала. Той же Нокс буквально дихав їй у потилицю. Кейн рухався так упевнено, що ніхто не сумнівався: одним із учасників обов’язково буде він. А троє інших?"
"Дорогою в Рафтхол Селена була твердо впевнена: вона неодмінно виграє ці дурні змагання. Зараз… зараз їй дуже хотілося повернути собі колишню впевненість."
"Селена приголомшено дивилася собі під ноги. Вона добре пам’ятала ці гострі сірі камінці. Пам’ятала, як вони кришилися під ступнями й як пахли після дощу. А ще вона пам’ятала, що, коли її збивали з ніг, вони боляче дряпали шкіру. Уся місцевість складалася з цих сірих каменів і камінців. Вони заповнювали цілі милі простору. З них складалися гори — кам’яні ікла, що пронизували хмарне небо. Жалюгідне лахміття, ветхе й брудне, не захищало від налітавшого вітру. Селена не могла без нудоти доторкатися до своїх лахміття. Що сталося? Де вона?"
"Вона повернулася, і брязкіт кайданів зі зловісною ясністю нагадав їй де. У соляних копальнях Ендов’єра."
"Провалила випробування, повернули на каторгу. Звідси не втечеш. Їй дали скуштувати свободи. Вона майже повірила, що свобода — це назавжди. А тепер…"
"Удару батога вона не чула. Спину обпекло нестерпним болем. Селена закричала й повалилася на землю. Сірі камінці вп’ялися їй у коліна."
"— Чого розляглася? Піднімайся! — прогарчав надсмотрщик."
"Сльози роз’їдали їй очі. Хитаючись, Селена встала й одразу побачила руку надсмотрщика з занесеним батогом. Тепер із нею розрахуються за все. Вони заб’ють її просто тут. У дворі, біля воріт."
"Батіг прорвав їй тіло до кісток. Перед очима закружляв вогняний шар. Потім і Селена закружилася разом із ним і понеслася до чорного прямокутника загальної могили, що ще не встигла наповнитися тілами."
"Першим, що вона відчула, розплющивши очі, був гострий запах власного поту."
"— Ти як? — запитав хтось поруч, і вона здригнулася всім тілом."
"Куди вона потрапила?"
"— Це був сон, — сказав Шаол."
"Селена очманіло дивилася на нього, потім завертіла головою по боках. Рафтхол. Вона все ще в Рафтхолі. У скляному замку. Ні, у кам’яному. У тому, що внизу."
"Спину покривав густий, липкий піт. Зовсім як кров. У Селени крутилася голова, до горла підступала нудота. Щось дивне творилося з відчуттям власного тіла: Селена одночасно відчувала себе піщинкою й величезною брилою. Вікна в її спальні були щільно зачинені, але звідкись тягнуло протягам, що ніс із собою аромат троянд."
"— Селено, заспокойся. Це був лише сон, — повторив капітан королівської гвардії. — Ти так кричала. Я подумав, що тебе уві сні вбивали, — усміхаючись лише губами, додав він."
"Селена обмацала спину. Тільки старі шрами — три великих і кілька дрібних. І більше нічого."
"— Мене били батогом, — сказала вона й різко смикнула головою, проганяючи страшні спогади. — А ти що тут робиш так рано? Ще навіть не світало."
"Вона сіла на ліжку, склавши руки, і, здається, трохи почервоніла. З чого б це?"
"— Сьогодні свято. Самуїнн, — сказав Шаол. — Я скасовую наші заняття. Я зайшов дізнатися, чи не хочеш ти піти на службу."
"Невже змагання витіснили з її пам’яті всі інші події?"
"— Як ти сказав? Сьогодні… Самуїнн? Чому ж нам заздалегідь не повідомили? Мабуть, сьогодні в замку буде бал?"
"— Бал, звичайно, буде, але тебе туди не запросили."
"— Звичайно. Мене запрошувати небезпечно. А раптом я в якоїсь придворної дами вкраду намисто прямо з шиї? Чи браслетик з ручки. А ти, капітане, як будеш відзначати Самуїнн? Викликати духів чи танцювати біля вогнища?"
"— Придумала теж! — відмахнувся капітан. — Я в дурнуватих обрядах не беру участі."
"— Поміркуй свою хоробрість, Шаоле, — усміхнулася Селена й намалювала в повітрі якийсь знак. — У цей день боги й душі померлих перебувають зовсім близько від нас. Не боїшся, що вони почують твої образливі слова?"
"— Люди тримаються за дурнуватий звичай — святкувати настання зими, — скривився Шаол. — Шукають у вогнищах якийсь вищий сенс. Нічого ці вогнища не дають, крім попелу."
"— Це приношення богам, щоб уберегти їх."
"— Від кого? Що це тоді за боги? Попіл удобрює землю, більше нічого."
"— Це ти так кажеш, — заперечила йому Селена й встала."
"Її нічну сорочку можна було вичавлювати. А ще краще — не думаючи, викинути. Навряд чи це введе в розхід королівську казну."
"Селена попрямувала до умивальної. Капітан пішов слідом."
"— Ось уже не думав, що ти віриш у різні забобони. І як це тільки поєднувалося з твоїм ремеслом?"
"Вона обернулася, нагородивши його сердитим поглядом. Їй хотілося гарненько помитися, а не вести порожню розмову. Вона увійшла до умивальної. Капітан не відставав."
"— Ми тепер і митися будемо разом? — запитала вона."
"Шаол збентежився й шумно грюкнув дверима з іншого боку."
"Коли Селена, розбризкуючи краплі води з волосся, увійшла до їдальні, капітан чекав її там."
"— А де ти снідав до того, як мене сюди привезли? — запитала вона."
"Уж якщо сьогодні свято, їй дозволено снідати самій і взагалі розпоряджатися своїм часом, як забажає."
"— Ти спочатку відповіси на моє запитання, — сказав Шаол."
"— На яке ще запитання?"
"Селена вмостилася навпроти капітана й наповнила тарілку кашею. Каша була цілком їстівною, однак вимагала відчутної добавки цукру й гарячих вершків."
"— Ти підеш до храму?"
"— Чому це мені дозволяють піти до храму, а на свято не кличуть? — запитала Селена, зачерпуючи повну ложку каші."
"— Право молитися зберігається за всіма."
"— А право ходити на свята?"
"— Свято, — усміхнувся капітан. — Суцільне обжерливість, пияцтво й розпуста. Кожен рік — одне й те саме."
"— Зрозуміло. Королівська влада піклується про мою моральність, — підбила підсумок Селена."
"Ну скільки ложок цукру треба всипати в цю кашу, поки вона стане солодкою?"
"— Тож ти підеш до храму? Якщо підеш, тоді їж швидше."
"— Не піду, — з повним ротом відповіла Селена."
"— Дивно. При твоїй-то забобонності — і розгнівати богів, не пішовши на службу. Мені здавалося, асасини мусять особливо шанувати день мертвих."
"Селена вирячила очі й надула щоки, зображуючи з себе недоумкувату. При цьому вона не забувала жувати."
"— У мене свої стосунки з богами. Може, я встигну задобрити їх парою жертв."
"Шаол підвівся, звично взявшись за ефес меча."
"— Постарайся обійтися без дурниць. Так, і ось ще що: ти особливо не вбирайся. Брулло мені сказав, що денних занять він не скасовує. Завтра у вас випробування."
"— Знову? Попереднє було всього три дні тому, — простогнала Селена."
"Минулого разу вони кидали спис на скаку, і її здерті пальці ще не загоїлися."
"Капітан пішов, не сказавши більше ні слова. У покоях Селени стало тихо. Тільки в її вухах усе ще лунали глухі удари ендов’єрського батога."
"Радіючи довгоочікуваному кінцю служби, Доріан Хавільяр поспішно покинув храм і вирушив блукати замком. Релігія ніколи не надихала його. Після кількох годин сидіння на жорсткій лаві й бурмотіння нескінченних молитов йому відчайдушно хотілося подихати свіжим повітрям і побути наодинці."
"У принца заніло лівий скроню. Стиснувши зуби, Доріан почав на ходу розтирати хворе місце. На шляху йому трапилася зграйка придворних дам. Побачивши принца, вони поспішно присідали в реверансі, а потім так само поспішно, з дурнуватим хихиканням, закрилися віялами. Доріан пройшов повз, обмежившись стриманою кивком. Навіть на таких службах королева не забувала показувати синові потенційних наречених, шепотом пропонуючи звернути на них увагу. Доріану коштувало немалих сил не вибухнути й не піти зі служби раніше часу."
"Вирішивши обійти живу огорожу, він свернув ліворуч і ледь не зіткнувся з жінкою в блакитно-зеленій оксамитовій сукні. Такого кольору буває вода в гірських озерах. Мабуть, у кравців цей відтінок якось називається, але Доріан подібних тонкощів не знав. Оксамит, звичайно, красивий, із переливами, що нагадують дорогоцінний камінь, а от фасон… був у моді років сто тому."
"З сукні погляд принца перемістився на обличчя жінки."
"— Добридень, пані Ліліано, — з учтивою усмішкою привітався принц, додавши до усмішки легкий уклін. — Радий бачити й вас, принцесо Нехеміє. Ну а з капітаном ми сьогодні вже зустрічалися."
"Він чомусь не міг відірвати очей від сукні Селени. Струменячі хвилі оксамиту тепер були схожі на води ріки."
"— Який у вас святковий наряд, — обережно сказав принц."
"Селена опустила очі."
"— Коли пані Ліліана вбиралася, її служниці були в храмі, — пояснив капітан. — Їй довелося вдягнути те, що потрапило під руку."
"Це було схоже на правду. Нинішні модні сукні мали корсет, зашнурувати який без сторонньої допомоги не вдавалося жодній жінці. Селена напевно заплуталася б не тільки зі шнурівкою, а й із численними потайними застібками й гачками."
"— Ваша високосте, прошу мене великодушно вибачити, — почервонівши й ледь стримуючи гнів, відповіла Селена. — Мені щиро шкода, що мій наряд не відповідає вашому смаку."
"— Ні, що ви, — пробурмотів Доріан, дивлячись на її ноги."
"Селена була в яскраво-червоних туфлях. Їхній колір нагадував колір лопнувших ягід на кущах, коли їх торкнеться мороз."
"— Ви чудово виглядаєте. Просто ваша сукня… вона трохи не з нашої епохи."
"Селена виразно подивилася на нього."
"‘На тебе не догодити!’ — говорив її погляд."
"Збентежений принц повернувся до Нехемії."
"— Як поживаєте, принцесо? — запитав він, намагаючись ретельно вимовляти ейлуейські слова."
"Відчувалося, коряве вимова ріже їй слух, але правила пристойності змушували Нехемію схвально кивати."
"— Добре поживаю, ваша високосте, — відповіла вона на такому ж ламаному адарланському."
"Тільки зараз Доріан помітив у тіні живої огорожі двох охоронців Нехемії. Як завжди, уважно спостерігаючих і готових до будь-яких несподіванок. У принца застукало в скронях."
"Уже кілька тижнів герцог Перангон намагався переконати радників у необхідності послати в Ейлуе додаткові війська. Це, на думку герцога, дозволить назавжди покінчити з бунтівниками й відбере в ейлуейців будь-яке бажання бунтувати. Не далі як учора Перангон виступив із новою пропозицією: окрім відправки адарланських легіонів, недвозначно заявити, що Нехемія перебуває в Рафтхолі на становищі заручниці. Це — доводив Перангон — охолодить запал бунтівників і змусить їх здатися. Доріан ще міг зрозуміти, коли адарланці брали заручників у межах Ейлуе. Але зробити заручницею спадкову принцесу? Він кілька годин підряд закликав королівську раду не вчиняти такої помилки, чреватої появою в Ейлуе лише нових бунтівників. На жаль, доводи принца переконали зовсім небагатьох. Більшості радників задум Перангона здавався сміливим і своєчасним. Усе, що вдалося Доріану, — це переконати королівську раду не приймати остаточного рішення до повернення короля. За решту тижнів принц сподівався перетягнути на свій бік частину прихильників герцога."
"Доріан відчував незручність і намагався не дивитися Нехемії в очі. Будь він ким завгодно, тільки не спадковим принцем, він би неодмінно її попередив. Але якщо Нехемія поїде раніше встановленого терміну, герцог одразу зрозуміє, хто її попередив, і про все доповість королеві. Стосунки з батьком і так були огидними; не вистачало тільки, щоб на принца лягло тавро співчуваючого бунтівникам."
"— Ви будете на вечірньому святкуванні? — запитав він принцесу, намагаючись надати обличчю учтиво-байдужий вираз."
"— А ви, Ліліано? — у свою чергу запитала Нехемія."
"Усмішка Селени не віщувала нічого доброго; у всякому разі, для Доріана."
"— На жаль, цей вечір зайнятий у мене іншими справами. Так адже, ваша високосте?"
"У кожному її слові відчувалася роздратованість."
"Шаол ввічливо кашлянув і з підкресленою цікавістю став розглядати ягоди на колючих кущах. Доріан залишився без підтримки."
"— Найжахливіше, коли хочеться бути в двох місцях одразу, — заученим тоном придворного почав принц. — Але справи пані Ліліани вимагають її присутності. Мені теж дуже шкода, однак я поважаю її вибір."
"Якби погляд Селени міг перетворитися на кинджал, валявся б зараз Доріан із перерізаним горлом. Однак принц не поступався. Ну не міг, не міг він привести її на свято, де буде стільки цікавих очей. Посиплються запитання, здогадки, припущення. Поповзуть чутки. І потім, при такому скупченні гостей Селені буде легко загубитися. Спробуй простежити за нею!"
"— Тож ви не підете? — засмучено запитала Нехемія."
"— Ні. Сподіваюся, ви повеселитеся за нас обох. — Помовчавши, Селена додала ейлуейською: — Його високість уміє розважати жінок."
"Цього разу принц зрозумів кожне слово. Нехемія засміялася, і Доріану стало трохи легше. Ейлуейка з Селеною становили чудову пару. Нехай боги допоможуть їм."
"— А тепер, ваша високосте, нас чекають важливі справи, — сказала йому Селена, беручи принцесу під руку."
"Ні, дозволяти їм подружитися… це може мати непередбачувані наслідки."
"— Приємного вам дня, ваша високосте."
"Селена зробила реверанс, блиснувши переливами червоних і блакитних самоцвітів на поясі. Потім нагородила принца їдкою усмішкою й повела Нехемію в сад."
"— Дякую тобі за допомогу, — процідив крізь зуби Доріан."
"Капітан дружньо поплескав його по плечу."
"— Це вони ще смирні. Бачили б ви їх, коли вони обидві в ударі."
"Він поспішив слідом за жінками."
"Доріану хотілося кричати на все горло й рвати на собі волосся. Він пам’ятав свій візит до Селени й досі перебирав у пам’яті подробиці їхньої розмови. Але за ці тижні його час і увага були повністю зайняті засіданнями королівської ради й придворною рутиною. Якби не сьогоднішнє свято, він би неодмінно відвідав Селену. Він зовсім не хотів розгнівати її, сказавши, що сукня вийшла з моди. Вирвалося саме собою. І що вона так розлютилася через це свято? Подумаєш, не запросили…"
"Принц ще раз подумки перелічив собі причини, що не дозволяли допустити Селену на свято. Але на душі все одно було муторно. Він повернувся й поплентався в бік псарні."
"Селена вела пальцем по акуратно підстрижених кущах і усміхалася сама собі. Після слів принца сукня їй анітрохи не розлюбилася. І вигляд у ній був по-справжньому святковий."
"— Ні, ваша високосте, я не солдат, — повільно втовкмачував Нехемії Шаол. — Я капітан королівської варти. Ми охороняємо безпеку й спокій королівської родини."
"— Це одне й те саме, — сказала принцеса."
"Вона все ще говорила з сильним акцентом, але капітан зрозумів і прикусив губу. Селена ледь стримувала злорадну посмішку."
"За минулі два тижні вони з Нехемією бачилися достатньо часто. Правда, зустрічі були короткими: за обідом чи на прогулянці. Нехемія розповідала про своє дитинство, ділилася спостереженнями з життя й повідомляла, який придворний сьогодні її розлютив. А злили Нехемію мало не всі, з ким вона стикалася."
"— Мене не вчили битися на війні, — крізь зуби заперечив Шаол."
"— Ви вбиваєте за наказами вашого короля."
"‘Вашого короля’. Нехемія хоч і погано володіла адарланською мовою, але розуміла силу двох цих слів. ‘Вашого короля’ — не її. Селена постійно чула гнівні тиради Нехемії щодо адарланського короля, однак зараз вони були в саду, де слова ейлуейки могли підслухати чужі вуха. Треба її зупинити, поки не увійшла в раж."
"— Шаоле, з принцесою марно сперечатися, — сказала Селена, підштовхуючи його ліктем. — По-моєму, ти даремно поступився свій титул Пітеру. Цікаво, титул можна повернути? Тобі одразу стало б легше жити."
"— Ти зуміла запам’ятати ім’я мого брата?"
"Селена знизала плечима, не розуміючи, чому це так порадувало капітана."
"— Ти назвав мені його ім’я. Я запам’ятала. Що тут особливого?"
"Капітан сьогодні виглядав просто чарівно. Навіть волосся в нього красиво звисало на лоб, поєднуючись із золотавою шкірою обличчя."
"— Думаю, ти славно повеселишся сьогодні. Особливо без мене, — з похмурою посмішкою сказала Селена."
"— Невже тебе це так засмутило? — щиро здивувався Шаол."
"— Анітрохи, — збрехала Селена, перекидаючи локони через плече. — А якщо чесно, сама не знаю. По-моєму, всі люблять свята."
"— Хочеш, я принесу тобі звідти якусь дрібничку?"
"— Дрібничку не треба. Краще принеси смажену баранячу ногу."
"Капітан вдихнув прохолодне, бадьоре повітря."
"— Сумніваюся, що сьогодні буде щось особливе. Бал як бал, бенкет як бенкет. Швидше за все, бараняча нога виявиться сухою й жорсткою."
"— А взагалі-то, друже мій, ти мусиш або взяти мене з собою, або скласти мені компанію."
"— Друже?"
"Селена почервоніла."
"— Мабуть, правильніше буде назвати тебе «похмурим супроводжуючим». Чи «впертим знайомцем», якщо тобі так більше подобається."
"На її подив, капітан усміхався."
"Принцеса раптом схопила Селену за руку."
"— Навчи мене вашої мови, — ейлуейською сказала вона, переходячи на «ти». — Навчи краще її розуміти. Я ж досі толком не можу ні читати, ні писати по-вашому. Мене зовсім замучили нудні, тупі старі, яких мені дали в учителі."
"— Я? — здивувалася Селена."
"Їй було ніяково, що принцеса не може брати участь у загальних розмовах. А було б здорово, якби Нехемія навчилася вільно говорити адарланською. Але як переконати Шаола? Він і так насторожено ставився до їхніх зустрічей і ніколи не дозволяв їм залишатися наодинці. Сидіти на їхніх уроках капітан нізащо не погодиться."
"— Бачиш, самій говорити адарланською й учити адарланській інших — різні речі. Сумніваюся, що в мене вийде, — сказала Селена."
"— Вийде, — не прийняла заперечень принцеса. — Ти будеш мене вчити. Після… ваших із ним справ, — уточнила вона, злегка кивнувши в бік капітана. — По годині щодня, перед вечерею."
"Судячи з обличчя принцеси, її прохання було рівнозначне наказу. Селена набрала повні груди повітря й повернулася до Шаола. Капітан запитально поглядав на неї."
"— Принцеса бажає, щоб я щодня, перед вечерею, займалася з нею адарланською мовою."
"— Боюся, це неможливо, — відрізав капітан."
"Селена переклала. Від погляду Нехемії, яким вона зараз дивилася на Шаола, багатьох прошибав піт. Капітан виявився стійкішим."
"— Чому неможливо? — запитала принцеса. — Селена розумніша за багатьох ваших, що в замку."
"Шаол зрозумів загальний сенс її строкатої ейлуейської фрази."
"— Не думаю, що таке…"
"— Я — спадкова принцеса Ейлуе. Чи цього мало? — нещадно коверкаючи адарланські слова, запитала Нехемія."
"— Ваша високосте, — почав було Шаол, але Селена схопила його за руку, кивнувши на дивне видовище."
"Вони перебували неподалік від Часової вежі. Навіть у яскраві сонячні дні чорна вежа виглядала похмурою й загрозливою. Однак дивним видовищем була не вона, а стоявший на колінах Кейн. Нахилившись до землі, він уважно щось роздивлявся."
"Почувши кроки, Кейн повернув голову. Потім, як завжди, оскалив зуби в широкій усмішці й встав. Його руки були перепачкані землею. Не чекаючи, коли всі троє наблизяться до нього, Кейн кивнув Шаолу й швидко пішов у бік вежі."
"— Двоноге чудовисько, — видихнула Селена, дивлячись йому вслід."
"— Хто це? — ейлуейською запитала Нехемія."
"— Колишній солдат королівської армії, — відповіла Селена. — Тепер служить герцогу Перангону."
"Нехемія теж поглянула в бік швидко віддаляючогося Кейна, і її темні очі перетворилися на щілини."
"— Не знаю чому, але мені хочеться з розмаху вдарити його по обличчю."
"— Рада, що хтось розділяє моє бажання, — засміялася Селена."
"Шаол мовчки рушив далі. Селена з Нехемією пішли слідом. Шлях їх лежав через відкриту веранду, на якій стояла Часова вежа. Селена придивилася до місця, де щойно копирсався Кейн. Те, що вона побачила, погано в’язалося з обликом і повадками Кейна. Виявилося, цей здоровань розчищав знак, подряпаний на плитці. Тепер знак був видний за кілька кроків."
"— Як по-вашому, що це за знак? — запитала вона принцесу. — І з чого Кейну знадобилося його очищати від землі й сміття?"
"— Це «знак долі», — сказала Нехемія."
"Ледь уміла говорити адарланською принцеса знала такі слова! Селена насупила лоба. У самому знаку не було нічого незвичайного чи страшного: трикутник усередині кола."
"— Ви розумієте сенс цих знаків? — запитала Селена."
"‘Знак долі’. Як дивно."
"— Ні, сенсу я не розумію, — поспішно відповіла принцеса. — Це залишки давньої, давно зниклої релігії."
"— Якої релігії? — тільки й встигла запитати Селена, як помітила другий знак. — Дивись, а ось і ще один."
"Другий знак являв собою коло, з центру якого починалася вертикальна лінія. Вийшовши за межі кола, вона роздвоювалася."
"— Краще їх не чіпати, — різко заявила Нехемія. — І забули їх не просто так. Була причина."
"Селені залишалося лише здивовано моргати."
"— Про що ви говорите? — запитав Шаол."
"Селена коротко передала йому суть їхньої розмови. Вислухавши її, капітан випнув нижню губу й не вимовив ні слова."
"Відійшовши на кілька кроків, вона побачила третій знак: сильно сплющений ромб із роздвоєними лініями по боках. Його верхня й нижня частини були витягнуті майже в пряму лінію. Знак володів дивною симетрією. Хто наказав подряпати ці знаки на плитках? Король, коли будували Часову вежу? Чи плитки з’явилися тут набагато раніше вежі?"
"Нехемія безвідривно дивилася на лоб Селени."
"— Щось не так? — не витримала Селена. — Я запаскудилася землею?"
"— Ні, — майже пошепки відповіла принцеса, продовжуючи розглядати її. Обличчя самої Нехемії стало настільки лютим, що Селена, яка бачила десятки злих облич, злегка відсахнулася. — І ти нічого не знаєш про «знаки долі»?"
"— Нічого, — під жахливий бій годинника відповіла Селена. — Інакше б не запитувала."
"— Ти щось приховуєш, — сказала Нехемія, але в її тоні не було докору. — Ти зовсім не така, якою здаєтьсяшся, Ліліано. У тобі є інший пласт, і він значніший за зовнішній."
"— Ви робите мені великий комплімент. Доти я вважала себе звичайною придворною. Може, трішки розумнішою за інших жінок."
"Селена намагалася говорити невимушено, мріючи, щоб Нехемія припинила пильно розглядати її."
"— Пам’ятаєте, у нашу першу зустріч ви сказали, що я говорю ейлуейською, як простолюдинка. Тож навчіть мене говорити, як говорять у вас при дворі."
"— Навчу, якщо ти навчиш мене вашої смішної мови, — пообіцяла принцеса."
"Настороженість у погляді Нехемії послабилася, але зовсім не зникла. Що ж такого побачила принцеса, якщо навіть змінилася в обличчі?"
"— Давайте укладемо договір, — натягнуто усміхаючись, запропонувала Селена. — Тільки йому не кажіть. Десь із трьох чи чотирьох годин я зазвичай буваю вільна. Тож за годину до вечері ми цілком можемо зустрічатися й займатися мовами."
"— Тоді завтра я прийду до тебе о п’ятій, — сказала Нехемія."
"Принцеса усміхнулася й пішла далі. Її чорні очі дивно блищали. Селена вважала за благо більше не розпитувати Нехемію й мовчки пішла слідом за нею."

#Епізод 13

"Селена, не роздягаючись, лежала на постелі, роздивляючись підлогу, залиту місячним світлом. Світло проникало в усі пилові щілини між кам’яними плитками, роблячи простір спальні блакитно-сріблястим, а час — завмерлим. Селені здавалося, ніби вона застигла в одному з таких миттєвостей."
"Ніч не викликала в неї страху, хоча така темрява подобалася їй набагато менше денного світла. Інколи, підстерігаючи жертву чи повертаючись після вбивства, Селена піднімала голову до неба. Зоряні роси захоплювали її й водночас змушували відчути себе маленькою, нікчемною комашкою."
"Почувши бій тих самих жахливих годинників у саду, Селена насупила брови. Північ. Завтра чергове випробування. Зараз їй уже треба було б спати, але сон не йшов. Може, почитати? Їй не хотілося вставати й запалювати свічку. Піти й щось зіграти на клавікордах? Краще не варто, а то раптом ще хтось з’явиться послухати її гру. Але ще дурніше отак лежати й уявляти собі бурхливу, наповнену людськими голосами бальну залу. За весь день вона так і не переодягнула свою зеленкувато-блакитну сукню, що відстала від моди на століття чи більше. Їй було лінь переодягатися."
"Селена дивилася туди, де місячне світло перетікав з підлоги на стіну, завішену старовинною шпалерою. Відчувалося, її не дуже берегли. Дивнішим був зображений сюжет: ліс, що йшов далеко-далеко, химерні гілки дерев, з яких визирали різні лісові звірі. Внизу, ближче до підлоги, знаходилася постать жінки. Інших людей там не було."
"Завдяки розмірам шпалери ця жінка була виткана в повний зріст. У неї були сріблясті, ніби сиві, волосся, але зовсім юне й дуже гарне обличчя. Здавалося, місячне світло грає складками її хвилястої білої сукні."
"Ні, не здавалося! Шпалера справді злегка тремтіла. Селена повернулася до вікна. Воно було щільно зачинене. Селена згадала, що сили протягів не вистачало, щоб змусити важке полотнище колихатися."
"Що ж тоді вона зараз бачить? Гру свого перезбудженого розуму?"
"У шкіру Селени ніби вп’ялися десятки крихітних голочок. Дівчина встала, запалила свічку й обережно підійшла до стіни. Шпалера перестала колихатися. Селена відвернула край полотнища. Під ним, як і всюди, була кам’яна стіна. Селена поставила свічку на столик, підвернула нижній край шпалери й поклала його на комод. Потім знову взяла свічку й почала уважно роздивлятися стіну. Вона побачила вертикальну борозну й на відстані трьох футів — ще одну. Бороздки починалися від підлоги й закінчувалися трохи вище її голови, де вони…"
"Так це ж двері!"
"Селена плечем уперлася в кам’яну плиту. Та злегка піддалася, і в Селени закалатало серце. Глотнувши повітря, вона знову натиснула на камінь. Двері жалісно заскрипіли. Селена натиснула сильніше, і двері відчинилися."
"Попереду темнів коридор. Звідти тягнуло вітром. У Селени похолола спина, але зовсім не від вітру. І чому тепер вітер дме в бік коридору? Адже щойно він дув у зворотний бік, розгойдуючи портьєру."
"Селена окинула поглядом спальню, зім’яту постіль із розкиданими по ковдрі книгами й ступила в коридор."
"Його стіни теж були складені з каменю й вкриті густим шаром пилу. Зробивши кілька кроків, Селена повернулася до кімнати. Уж якщо вона збирається досліджувати коридор, не з однією ж свічкою туди йти. Ех, їй би зараз не завадив найпоганенький кинджал чи ніж. Звичайно, краще б меч. І однієї свічки буде мало. Тут потрібен факел, у крайньому разі — запас свічок. Вона вміла пробиратися й у кромішній темряві, але була не настільки дурна, щоб довіряти темряві в королівському замку."
"Тремтячи від збудження, Селена обійшла кімнати, міркуючи, що може їй знадобитися. У кошику для рукоділля Фаліпа дуже доречно залишила два мотки пряжі. Селена взяла їх, а ще три шматки крейди й один зі своїх саморобних ножів. У кишені плаща вона запхала три нові свічки, а плащ щільно підперезала."
"Вона зупинилася на порозі. Темрява в коридорі була справді кромішною, але Селену чомусь тягнуло зануритися туди. Вітер знову дув усередину."
"Селена передбачливо приставила до відчинених дверей важкий стілець, щоб ті раптом не грюкнули й не замкнули її в пастці коридору. На спинці стільця Селена п’ятьма вузлами надійно закріпила кінець одного з мотків пряжі. А подумавши, розгорнула шпалеру, замаскувавши й двері, й стілець. Мало що."
"Коридор був холодним, але сухим. По стінах і стелі тягнулася пилова павутина. Пройшовши кілька кроків, Селена побачила сходи, що йшли в темряву. Слабенького вогника свічки вистачало лише, щоб побачити п’ять-шість найближчих сходинок. Селена напружилася всім тілом, готова при найменшому шелесті стрімголов кинутися назад до кімнати. Але навколо панувала мертва тиша, яку зустрінеш лише в покинутих і забутих людьми місцях."
"Тримаючи свічку над головою, Селена повільно почала спускатися. Поли плаща волочилися по сходинках, затягуючи за собою пил. Селена не знала, скільки часу провела тут. Вона вдивлялася в стіни, сподіваючись побачити якісь написи чи знаки. Нічого. А може, вона потрапила всього лише на стару сходову клітку? Колись тут ходили слуги, потім перестали. У замку повно таких покинутих місць. Мабуть, сходи й коридори, як сукні, теж «виходять з моди». Ось адже вигадала собі пригоду! Закінчиться ця сходова клітка в якійсь пиловій, заваленій мотлохом коморі з наглухо зачиненими дверима."
"Але сходи привели Селену не в комору, а до трьох масивних порталів, розташованих по один бік. Куди ж вона все-таки потрапила? Важко уявити, щоб у багатолюдному замку про це місце зовсім забули. Однак густий шар пилу на підлозі доводив, що так воно й є. Скільки десятиліть тому тут востаннє ступала чиясь нога?"
"Три портали. Ворота. Не надто веселий вибір. У казках двоє з них неодмінно вели до вірної смерті. Селена оглянула стіни, знову намагаючись побачити хоч якісь попередження. Нічого."
"Моток пряжі перетворився на крихітний клубочок. Селена обережно поставила свічку на підлогу, дістала другий моток і прив’язала до залишків першого. У кімнаті, здається, десь ще була пряжа. Даремно полінювалася пошукати, зате в неї залишилося три невикористані шматки крейди."
"Селена обрала середній портал, але лише тому, що той був до неї найближчим. А сходи тим часом продовжувалися, йдучи вниз. Куди, в які підземелля? Селені здавалося, що вона вже й так під землею."
"Вона увійшла в портал. Від основного коридору відходило безліч відгалужень, але Селена йшла прямо, орієнтуючись на зростаючу вогкість. По стінах сочилася вода, а пил і павутину замінила пліснява. Ставало все холодніше. Полум’я свічки незадоволено шипіло в сирому повітрі. Червоні оксамитові туфлі осклизли й наскрізь промокли. Селена вже збиралася повернути назад, але звук, що доносився з темряви, змусив її йти далі."
"Це був звук повільно текучої води. У тунелі ставало світліше. Тепер шлях їй освітлювала не тільки загрозлива погаснути свічка, а рівне, блакитнувате світло, що лилося назустріч. Місячне світло."
"У Селени закінчився другий моток, і вона кинула нитку на мокру й брудну підлогу. Усі відгалуження теж закінчилися. Селена знала, де вона. Точніше, здогадувалася, але все ще боялася повірити в правдивість своєї здогадки. Вона прискорила крок і з радістю б побігла, але не в такому взутті. Серце оглушливо стукало, і Селена думала, що в неї зараз лопнуть барабанні перетинки. Вона пішла далі й пару разів ледь не впала. Попереду показалася склепінчаста арка, а далі, далі…"
"Селена вийшла до широкого каналу, що вбирав у себе всі стоки й нечистоти замка. Пахло тут… ні, тут не пахло. Тут відчайдушно смерділо."
"Вона стояла, роздивляючись відчинені ворота й вузьку площадку за ними. Усе, що вивергав із себе замок, канал уносив в Авери, а може, й прямо в море. Тут не було ні вартових, ні засувів. Тільки залізна решітка, що перегороджувала смердючу ріку."
"Біля берегів погойдувалися на бурих хвилях по чотири човники. На протилежній стіні виднілося кілька дверей — дерев’яних і залізних. Можливо, якась із них була кінцем потайного ходу, що дозволяв королеві непомітно покинути замок. Селена придивилася до наполовину згнилих човнів. Швидше за все, чинний нині король навряд чи знав про існування цього ходу."
"Селена підійшла до решітки й просунула голову крізь іржаві прути. Нічний повітря було холодним, але не таким, коли промерзаєш до кісток. Зовні над зловонним потоком схилилися чорні стовбури дерев. Мабуть, Селена потрапила в ту частину замка, що звернена до моря…"
"Але може, з зовнішнього боку все ж є вартові? Під ногами валявся великий камінь. Обвалився зі стелі. Селена підібрала камінь, розмахнулася й кинула у воду за межами воріт. Якби там були вартові, вона почула б брязкіт обладунків і зброї та сердиті голоси. Але вона не чула нічого, крім шуму води. На іншому кінці решітки виднів підйомний механізм. Важко сказати, коли востаннє тиснули на його важкий важіль, щоб підняти решітку й пропустити човни."
"Селена знайшла виїмку в стіні й поставила туди свічку. Вона зняла плащ і витягла все, що було в кишенях. Ухопившись руками за прути, Селена обережно почала перебиратися на інший бік."
"Їй доводилося мати справу з підйомними механізмами. Мабуть, цей ненамного складніший. Залишалося лише натиснути на важіль. Селена відчувала себе звіром, якому забули зачинити клітку. Її трясло від хвилювання. Що вона робить у цьому палаці? Навіщо вона — найкращий асасин Адарлана — витрачає час на якісь ідіотські змагання? Навіщо намагається довести, що вона найкраща? Ось вам доказ!"
"Схоже, сьогодні вартові капітана Естфола перепили нарівні з усіма. Селена могла б зараз обрати човен понадійніше й зникнути в ночі. Але для цього треба повернутися за плащем. Плащ їй не завадить. Ці дурні думали, що перетворили її на дресировану звірятку!"
"Нога ледь не зісковзнула з осклизлого нижнього прута решітки. Селена вчепилася в неї, боляче вдарившись коліном. Бурмочучи прокляття, вона заплющила очі, щоб заспокоїтися. Внизу — всього лише вода. Нехай дуже брудна, але вода. Це тобі не Ендов’єр."
"Дочекавшись, коли серце перестане калатати, Селена знайшла іншу опору для ноги. Місяць навіть заважав їй зараз своїм нестерпно яскравим світлом. Крізь нього ледь розрізнялися зірки."
"Вона зібралася з думками. Звичайно, їй нічого не варто зараз утекти з замка, але це буде найдурніший із усіх її дурних вчинків. Король не заспокоїться, поки не знайде її. Шаола з ганьбою виженуть із королівської гвардії, а принцеса Нехемія залишиться одна серед лицемірних ворогів."
"Селена гордо закинула голову. Ні, вона не втече від них, наче жалюгідний злодійчук. Вона пройде ці дурні випробування й гідно здобуде собі свободу. І потім, чому б не відновити сили на безкоштовних харчах? Чому б не розширити свої навички, вправляючись у залі? Втечі стрімголов не здійснюються. Треба запастися всім необхідним, на що підуть тижні. Куди їй поспішати?"
"Селена повернулася туди, де залишила плащ. Вона переможе. А коли вона переможе… якщо коли-небудь їй знадобиться втекти з королівського рабства… тепер у неї є свій потайний хід."
"І потім, не можна переоцінювати свої сили. Повертаючись назад, Селена відчувала, що втомилася. У неї гули ноги, а їй ще належав підйом нагору."
"Важко дихаючи, вона вибралася з порталу й зупинилася, оглядаючи два інші. Куди ведуть вони? Їй раптом стало байдуже. Нещодавнє цікавість згасла. Однак вітер знову подув, і тепер — у бік правого порталу. Селена ступила туди й остовпіла. Полум’я свічки нахилилося вперед, вказуючи в темряву. Але навіть серед загальної темряви одна ділянка виглядала значно чорнішою за решту. У шелесті вітру чулися голоси, що зверталися до неї давно забутими мовами. Селена вискочила звідти й попрямувала до лівого порталу. Йти за шепочучими голосами завжди небезпечно, а в ніч Самуїнна — ще небезпечніше."
"У тунелі лівого порталу вітер раптом став теплим. Через кілька кроків Селена побачила гвинтові сходи, що вели нагору. Забувши про гудячі ноги, вона почала підніматися. З кожною сходинкою шепочучі голоси слабшали, поки не затихли зовсім. Тепер Селена чула тільки свої втомлені кроки."
"Сходи вивели її не в лабіринт переходів, а в коридор. Здавалося, він безкінечний. Селена йшла й йшла. Їй хотілося розтягнутися на підлозі й відпочити. Цього робити було не можна. Вона вже збиралася повернути назад і пройти виснажливий шлях до своєї кімнати, як раптом почула музику."
"Сумнівів не могло бути: музика доносилася з Великої зали. Невдовзі на стінах і підлозі з’явилося слабке золотаве світло. Мабуть, воно лилося з якоїсь дверей."
"Завернувши за ріг, Селена потрапила на невеликі сходи. Ті вивели її в вузький, низький коридор, рухатися по якому можна було тільки пригнувшись. Селена вперто йшла вперед. Але вона помилилася: і світло, і звуки проникали не з-за дверей, а з-за бронзової вентиляційної решітки."
"Селена заплющила очі. Вона перебувала майже під стелею й дивилася на бенкетуючих у Великій залі."
"Тільки для вентиляції призначався цей вузький і тісний коридор? Важко повірити, щоб тут не ховалися шпигуни, стежачи за тими, за ким було велено. Але зараз Селена була тут одна. А внизу понад сотня учасників святкування їли, пили, співали й танцювали. Невдовзі вона помітила Шаола. Той сидів поруч із якимось старим. Вони бесідували й… сміялися."
"Старий був до неї спиною. Можливо, він і не сміявся. Але Селена чітко бачила реготливого капітана. У неї почервоніли щоки, що вона одразу пояснила собі нестачею повітря. Селена поставила свічку на підлогу й оглянула дальній кінець величезної зали. Там теж були бронзові решітки, але за ними, здається, не ховалися нічиї цікаві очі або ховалися занадто вміло. Селена перевела погляд на танцюючих. Серед них вона помітила… кількох претендентів, своїх завтрашніх суперників. Їх приодягли, але погане вміння танцювати не сховати жодним вбранням. Нокс, з яким вона тепер вправлялася щодня, рухався краще за решту. Однак Селена все одно не заздрила дамам, які наважилися з ним танцювати."
"Що ж це виходить? Іншим претендентам дозволили піти на святкування, а їй — ні? Селена притулилася до просвіту між прутами решітки, щоб краще роздивитися своїх суперників. Відбувалося сприймалося нею як ляпас. Сюди покликали всіх… окрім неї. Ось вони, розсілися за столами. А Пелор насмілився сидіти біля Шаола! І капітан терпить присутність цього недомірка! Як вони посміли не покликати її? Тяжкість у грудях почала слабшати лише тоді, коли Селена переконалася, що на балу немає й Кейна. Видно, теж вважали небезпечним пускати його сюди."
"Трохи заспокоївшись, Селена стала спостерігати за спадковим принцем. Доріан кружляв із якоюсь світловолосою дурненькою, а та заливалася сміхом. Селені хотілося зненавидіти принца за таке поводження з нею, його захисницею! Але їй було не відірвати від нього очей. Ні, Селена не хотіла говорити з ним. Вона навіть не хотіла зараз опинитися на місці дурненької блондинки. Їй хотілося тільки дивитися й захоплюватися витонченістю рухів і добротою в його очах. Такий самий погляд був у нього тоді, від чого вона, сама того не бажаючи, раптом розповіла йому про Саема. Нехай він із роду Хавільярів, і все-таки… і все-таки їй відчайдушно захотілося його поцілувати."
"Танець закінчився. Спадковий принц галантно поцілував блондинці руку. Селена насупила брови й навіть відвернулася. Все. Тупик. У повному сенсі слова, оскільки вузький коридор, що більше нагадував лаз, біля бронзової решітки впирався в стіну."
"Обходячи танцюючих, Шаол попрямував до дверей Великої зали. Треба терміново повертатися! Якщо капітан надумає увійти до неї й побачить, що її ніде немає? А він неодмінно увійде, бо обіцяв принести їй з балу якусь дрібничку."
"Селена втомилася, дуже втомилася. У неї боліло все тіло, не кажучи вже про ноги. Але втрачати пильність було не можна, інакше завтра замість змагання вона опиниться… Селена встала, взяла свічку й рушила в зворотний шлях, на ходу змотуючи пряжу в клубок. Дорога була легкою — весь час униз. Селена майже бігла по гвинтових сходах, перестрибуючи через дві сходинки."
"Вона вибралася з порталу. Тепер нагору — в пил і темряву. Головне — встигнути. Встигнути раніше капітана. Дуже добре, якщо по дорозі до її покоїв хтось затримає його й відволіче. Зараз у замку повно п’яних, і когось неодмінно потягне «виливати душу». Але ні, краще на це не сподіватися."
"Коли Селена повернулася до спальні, вона ледь трималася на ногах. Їй би зараз треба було зняти з себе промоклу сукню, помитися й переодягнутися. Але на це не було ні часу, ні сил. Селена поспішно зачинила двері в стіні, розгорнула шпалеру й поставила на місце стілець, а потім плюхнулася на ліжко."
"Спадковий принц теж втомився. Він навіть не міг відповісти на запитання, що змусило його йти сюди, до покоїв небезпечної злочинниці Селени Сардотієн. І коли? О третій годині ночі! Голова крутилася від випитого вина й танців. Доріан розумів: варто йому присісти, і він миттєво засне. Найрозумніше було б зараз негайно йти до себе, але замість цього принц обережно прочинив двері спальні Селени й зазирнув усередину."
"Принца здивувало, що Селена так і не зняла цю дивну сукню. Але зараз, на тлі червоної ковдри, вона виглядала не такою вже й старомодною. Селені вона навіть пасувала. Золотаве волосся майбутньої королівської захисниці розметалося по червоних складках. Доріана порадувало, що від колишньої блідості не залишилося й сліду. Навіть уві сні щоки Селени залишалися рум’яними."
"Поруч із нею лежала розкрита книга. Швидше за все, Селена зачиталася й непомітно для себе заснула. Доріан не наважувався ступити всередину, боячись, що вона прокинеться. Асасини сплять чутко. Але ж не прокинулася ж вона від скрипу відчиняючихся дверей. Ні, Селена не була, не могла бути прирожденою вбивцею. Усьому виною — життєві обставини. Доріан вдивлявся в риси її обличчя, не знаходячи в них нічого хижого й кровожерливого."
"Нехай і небагато, але він встиг вивчити її характер і чомусь відчував, що Селена не завдасть йому шкоди."
"Доріан згадав усі батьківські застереження, усі попередження Шаола. І все-таки після його першого вторгнення сюди й їхньої розмови, що цілком складалася з колкостей, він відчув незрозуміле полегшення. Мабуть, Селена — теж, якщо вона раптом розповіла йому про якогось Саема. Сама розповіла. А тепер він з’явився сюди вдруге, глибокої ночі. Запитується — навіщо. Селена не знала тонкощів придворного флірту, і манеру її розмови навряд чи можна було назвати ввічливою. Минулого разу вона без жодних іносказань заявила, що роль чергової його коханки — не для неї. Тоді навіщо він топчеться на порозі її спальні?"
"Ззаду почулися обережні кроки. Обернувшись, Доріан побачив Шаола. Капітан мовчки схопив його за руку, витягнув у коридор і зупинився біля вхідних дверей."
"— Що ви тут робите? — сердитим шепотом запитав капітан."
"— А що тут робиш ти? — запитав принц."
"Запитання було більш ніж доречним. Чи не Шаол без кінця попереджав його про небезпеки близького знайомства з Селеною? А сам? Навіщо капітанові королівської гвардії знадобилося серед ночі з’являтися тут?"
"— Чорт би вас забрав, Доріане! Вона ж не та дурненька, з якою ви танцювали на балу. Вона — асасин. Вона здатна вбивати голими руками. Сподіваюся, це ваш перший візит сюди?"
"Відповіддю йому була дурнувато-усміхнена посмішка спадкового принца."
"— Не треба мені жодних ваших пояснень. Забирайтеся звідси, і якомога швидше. Такого безрозсудства я від вас не чекав."
"Шаол схопив принца за комір камзола. Розлючений Доріан замахнувся кулаком, але капітан виявився спритнішим. Не давши принцу отямитися, Шаол безцеремонно виштовхав його в коридор і замкнув двері на засув."
"Цієї ночі спадковому принцу спалося на рідкість погано."
"Шаол ковтав ротом повітря. Чи мав він право так поводитися зі спадковим принцем Адарлана? Доріан цілком резонно поставив йому запитання: а що він, Шаол Естфол, робить у покоях Селени? Капітан не розумів і не хотів розуміти причини гніву, що спалахнув у ньому, коли він застав тут Доріана. Це не було ревнощами; почуття, що охопило Шаола, перебувало за межами ревнощів, і це почуття перетворювало друга його дитинства на зовсім незнайому людину. Так, Селена встигла вбити чимало чоловіків, але ще не віддалася жодному. Достатньо було поспостерігати, як вона тримала себе з чоловіками. Чи знав про це Доріан? Можливо, знав, і це лише розпалювало його інтерес."
"Шаол прочинив двері трохи ширше й скривився, почувши гучний скрип."
"Судячи з усього, Селена знову зачиталася й заснула, не встигнувши роздягнутися. Навіть у цій старомодній сукні вона була просто прекрасна, але чарівність не робила її менш небезпечною. У ній і зараз проступали риси досвідченої й безжальної вбивці. Це читалося по її сильній щелепі, по вигину брів, по нерухомості пози. Селена була живим мечем, власноруч викуваним і заточеним Ватажком асасинів для своїх цілей. Мабуть, ось так сплять гірський лев чи дракон — під час сну ознаки їхньої сили нікуди не зникають."
"Шаол струснув головою й зробив крок. Селена прокинулася."
"— Послухай, до ранку ще далеко, — сонно пробурмотіла вона, повертаючись на інший бік."
"— Я приніс тобі подарунок."
"Шаол розумів, що каже якусь маячню. Йому захотілося стрімголов вибігти з її покоїв."
"— Подарунок? — здивувалася Селена."
"Вона повернулася й уставилася на капітана, моргаючи сонними очима."
"— Нічого особливого. Це роздавали на святі. Дай мені руку."
"Капітан сказав лише частину правди. Подарунки роздавали не всім підряд, а лише знатним дамам. Просто йому вдалося запустити руку в кошик і вкрасти це колечко. Більшість придворних дам із презирством ставилися до таких подарунків і або кидали кільця назад у кошик, або віддавали улюбленим служницям."
"— І що ж ти приніс? — позіхаючи, запитала Селена, але руку простягнула."
"— Ось, — з гордістю хлопчиська оголосив капітан, викладаючи кільце на її долоню."
"Селена сонно усміхнулася, але кільце взяла й одразу наділа."
"— Яке миленьке, — сказала вона."
"Насправді срібне кільце було зовсім простим. Його єдиною прикрасою служив аметист розміром із ніготь. Круглий камінчик із рівною поверхнею. Зараз він поглядав на Селену, ніби пурпурове око."
"— Дякую, — сонно промовила вона."
"— Ти так і спиш у цій сукні, — сказав капітан, відчуваючи, як червоніє."
"— Заснула. Коли ти підеш, я переодягнуся. Мені треба… відпочити."
"Капітан знав: переодягатися вона не буде. Через мить Селена вже спала. Рука з кільцем була притиснута до грудей біля серця. Капітан щось пробурмотів, потім зірвав із дивана накидку й укрив нею Селену. Йому раптом захотілося зняти з її пальця це кільце. Бажання було незрозумілим і відверто дурним. Потираючи палаючі щоки й шию, він тихо покинув покої Селени, думаючи про те, як завтра він пояснюватиме все це Доріану."
"Уві сні Селена знову йшла потайним коридором, куди вела знайдена нею двері. Але тепер у неї не було ні свічки, ні клубка. Спустившись до трьох порталів, вона обрала правий. З двох інших тягнуло холодом і вогкістю, а цей приваблював теплом і незвичним для порталу запахом. Звідти пахло не пилом і не пліснявою, а трояндами. Коридор, куди потрапила Селена, не був прямим. Він петляв праворуч і ліворуч і привів її до вузьких сходів. Сама не розуміючи чому, Селена не наважувалася доторкатися до кам’яних стін. Вона спускалася, обережно ставлячи ногу на чергову сходинку. Гвинтові сходи вивели її на майданчики, де теж були портали й двері. Але Селена, слідуючи за ароматом троянд, продовжувала спуск. Здавалося б, рух униз сходами не вимагав особливих зусиль, і все одно ноги в Селени встигли втомитися. Нарешті сходи привели її до старої дерев’яної дверей."
"Ймовірно, двері зсередини замикалися, бо мали бронзовий дверний молоток у вигляді черепа. Його порожні очниці дивилися на Селену. Їй почудилося, ніби череп усміхається. Селена зупинилася. Череп, нехай навіть і на дверях, не віщував нічого доброго. А раптом зараз звідкись потягне холодним вітром і вогкістю, і морок наповниться невідомо чиїми стогонами й криками? Але повітря залишалося теплим і все ще пахло трояндами. Набравшись хоробрості, Селена взялася за ручку. Двері безшумно відчинилися."
"Селена чекала побачити за дверима пилове, давно покинуте темне приміщення. В одному вона мала рацію. Тут давно ніхто не з’являвся. Але світла цілком вистачало. Він лився з невеликого отвору в стелі — сріблясто-блакитнувате місячне світло. Місяць освітлював статую прекрасної лежачої жінки. Придивившись, Селена побачила, що це не просто статуя, а надгробок. Кам’яна плита слугувала кришкою саркофага. Склеп! Ось, виявляється, куди привели її довгі гвинтові сходи."
"Стелю склепу прикрашали ліпні дерева. Їхні гілки схилялися над мармуровою жінкою. Поруч із її саркофагом стояв інший, і в ньому був похований чоловік. Але чому обличчя жінки буквально купалося в місячному світлі, а його обличчя ховали сутінки?"
"Статуї робив талановитий скульптор, бо навіть у мармурі обличчя чоловіка зберігало чарівність. Широке чоло, прямий, волевой ніс, коротка борідка клином. Чоловік стояв, тримаючи в руках меч і спираючись грудьми на його ефес. У Селени перехопило дихання, коли вона помітила на голові чоловіка корону."
"Корона була й у жінки. Легка, витончена, прикрашена єдиним синім самоцвітом. Її довге волосся вилося по плечах і спадало на кришку. Селені раптом здалося, що волосся це зовсім не з мармуру, а справжнє, людське. Обличчя статуї манило до себе, і Селена тремтячою рукою погладила мармурову щоку жінки."
"Щока виявилася твердою й холодною, якими й бувають у статуй."
"— Королевою якої епохи ви були? — вголос запитала Селена."
"Замість статуї їй відповіло відлуння з кутів склепу. Селена здригнулася, але не відійшла. Обличчя статуї її не відпускало. Вона обережно провела по мармуровому лобі, потім торкнулася напіввідкритих губ. І тут її рука намацала якийсь знак. Він майже зливався з рештою поверхні. Місячне світло заважало його роздивитися. Тоді Селена прикрила знак рукою. Сплюснутий ромб із двома розгалуженнями й вертикальною лінією, що виходила із середини…"
"‘Знак долі’. Майже такий самий вона бачила в саду, біля Часової вежі. Селені раптом стало зябко. Вона відступила від саркофага, розуміючи, що потрапила в заборонене місце."
"Селена ледь не спіткнулася, зачепившись ногою за якийсь горбик. Це змусило її придивитися до підлоги… Вона застигла з роззявленим ротом. Горбиків тут було безліч. Підлога зображувала зоряне небо. Селена глянула на стелю й помітила не тільки дерева, а кущі, траву й квіти. Там, нагорі, була земля. Але чому землю й небо поміняли місцями? А на стінах що?"
"Селена затулила собі рот, щоб не скрикнути. Уся поверхня стін була в «знаках долі». Вони тягнулися лініями, складали квадрати й завитки. У всьому була надприродна послідовність і гармонія. З маленьких знаків складалися знаки покрупніше, а вони, у свою чергу, утворювали ще більші знаки, щоб у кінцевому підсумку злитися в один гігантський «знак долі», сенс якого лежав далеко за межами людського розуміння."
"З того місця, де зараз перебувала Селена, їй був видний напис біля ніг мармурової королеви. Нахилившись, Селена прочитала кам’яні літери."
"«Розлом часів». Ще одна загадка. Мабуть, у давні часи ці слова щось означали. А може, й нічого. Скільки надгробків прикрашено пишною словесною безглуздістю. Чи все ж…"
"Статуя королеви не відпускала її. У мармуровому обличчі було щось заспокійливе й дуже знайоме; щось, що перегукувалося з ароматом троянд."
"Як же вона раніше цього не помітила? У мармурової жінки були вигнуті, гострокінцеві вуха! Вуха безсмертного народу фей. Династія Хавільярів правила вже тисячу років, і за час їхнього правління жодна з жінок народу фей не виходила заміж. Єдине виключення становила… Здається, вона була феєю лише наполовину. Але якщо здогадка вірна, значить, це…"
"Селена відступила вбік і шумно вдарилася спиною об стіну, піднявши білу хмару пилу."
"Це був склеп Гавіна — першого короля Адарлана. А поруч із його гробницею — гробниця Еліани, дочки Бранона, спадкової принцеси Террасена, дружини Гавіна й першої королеви Адарлана."
"Селена чула, як шалено калатає її серце. Тікати, швидше тікати звідси! Але її ноги приросли до зоряної підлоги. Вона не мала права сюди заходити. Їй, заплямованій кров’ю безлічі жертв, не можна з’являтися в священних місцях. Таке не залишається безкарним. Світ мертвих жорстоко помститься їй за святотатство."
"Припустимо, вона забрела сюди випадково. Але чому гробниці, які мали б шануватися як великі святині, перебувають у такому запустінні? Чому в день поминання мертвих ніхто не прийшов сюди, не очистив склеп від пилу й не усипав гробниці квітами? Чому люди забули про Еліану Галатінію-Хавільяр?"
"Заспокоївшись, Селена продовжила огляд склепу й біля дальньої стіни виявила купи дорогоцінних каменів і зброї. Поруч із золотими обладунками лежав меч. Селена впізнала його, хоча ніколи не бачила й тільки чула легенди про нього. Це був легендарний меч Гавіна. З ним король пройшов усі війни, що потрясали тоді континент. Цим мечем Гавін убив Еравана, Повелителя темряви. Навіть зараз, через сотні років, на лезі меча не було й найменших слідів іржі. І нехай меч утратив свої колишні магічні властивості, але сила, що викувала його, продовжувала жити."
"— Дамаріс, — прошепотіла Селена ім’я меча."
"— А ти, виявляється, знаєш вашу історію, — пролунав дзвінкий жіночий голос."
"Селена з криком метнулася геть, але зачепилася за спис і звалилася в скриню, наполовину заповнену золотими монетами й коштовностями. Жінка засміялася. Ярость додала Селені сміливості. Вона запустила руку поглибше, сподіваючись знайти в скрині якщо не кинджал, то хоча б важкий підсвічник. Але варто їй було побачити ту, кому належав голос, і Селена в жаху застигла."
"Поруч із нею стояла… Еліана Хавільяр. Не оживлена мармурова статуя, а жива… чи майже жива. Ця Еліана була ще прекраснішою за свого мармурового двійника. Сріблясте волосся лунними нитками спадало на плечі. Її очі блищали двома синіми зірками, а шкіра вражала білизною. Вуха Еліани були не гострокінцевими, а злегка загостреними."
"— Хто ви? — прошепотіла Селена, розуміючи всю дурість свого запитання."
"— Ти й так знаєш, хто я, — відповіла Еліана Хавільяр."
"Селена лежала, скрючившись, і боялася ворухнутися. Щось кололо їй у спину, а ліва нога затекла, притиснута важкою шкатулкою."
"— Ви… привид?"
"— Не зовсім, — відповіла королева Еліана й простягнула їй руку, допомагаючи встати."
"Рука була холодною, але цілком відчутною."
"— Мене не можна назвати живою у вашому розумінні, але я не привид, прикутий до гробниці."
"Еліана спрямувала очі до стелі й насупила брови."
"— Я сильно ризикувала, здійснюючи цю подорож."
"— Ви ризикували? — перепитала Селена, відсуваючись від королеви."
"— Ні ти, ні я не можемо тут довго залишатися."
"Якимось куточком свідомості Селена розуміла, що спить і бачить більш ніж дивний сон."
"— Їх удалося відволікти… на час. Але…"
"Еліана Хавільяр глянула на гробницю свого чоловіка."
"У Селени стиснуло голову. Мабуть, Гавін когось відволікав. Але кого?"
"— Хто вам заважав з’явитися тут? — запитала Селена."
"— Вісім вартових. Ти знаєш, про кого я говорю."
"Селена приголомшено моргала, потім миттєво все зрозуміла."
"— Це горгульї з Часової вежі?"
"Королева кивнула:"
"— Вони стережуть портал між нашими світами. Нам удалося вирвати час, і я змогла прослизнути повз них…"
"Еліана схопила Селену за руку. Боляче, як раніше хапав Шаол."
"— Слухай мене й запам’ятовуй. Збігів і випадковостей не існує. Усе, що відбувається, має свою мету й сенс. Тобі було призначено потрапити в цей замок, так само як тобі було призначено стати асасином і навчитися ремеслу, завдяки якому ти вижила."
"Селена відчула, як до горла підступає нудота. Вона так довго запихала ці спогади на саме дно пам’яті, так сподівалася, що вони зникнуть у бездонних глибинах. Навіщо Еліана дістала їх звідти?"
"— У цьому замку мешкає чудовищне зло. Чудовищне й могутнє, здатне потрясати зірки. Відлуння його злодіянь відгукується в усіх світах. Тобі належить зупинити це зло. Забудь про свою дружбу, борги й клятви. Знищ це зло, поки ще не запізно. Інакше воно прорветься через портал, і тоді вже ніщо його не зупинить."
"Королева замовкла й прислухалася. Її обличчя посуворилося."
"— Часу майже не залишилося. Ти мусиш виграти змагання й стати королівською захисницею. У тебе є розуміння. Ерілея потребує такої королівської захисниці, як ти."
"— Але що я…"
"Рука королеви щось шукала в кишенях."
"— Тебе ні в якому разі не повинні тут застати. Якщо тебе впіймають — усе пропало."
"Еліана вклала Селені в долоню якусь металеву штучку."
"— Це вбереже тебе від небезпек."
"Потім вона силоміць потягла Селену до дверей і сказала:"
"— Ти, мабуть, думаєш, що це я тебе сюди покликала. Ні. Мене теж сюди притягнуло. Тебе спрямувала якась сила, про яку я нічого не знаю. Комусь треба, щоб ти дивилася й училася…"
"Зовні долинуло ричання."
"— Вони повертаються, — прошепотіла Еліана."
"— Я не розумію, про що ви говорите. Мабуть, ви мене з кимось сплутали. Я зовсім не така."
"Королева Еліана торкнулася плечей Селени й поцілувала її в лоба."
"— Мужність серця зустрічається дуже рідко, — з незрозумілим спокоєм промовила вона. — Нехай це мужність веде тебе."
"Ричання перетворилося на шалений рев, і від нього затремтіли стіни. Селена заціпеніла. Королева Еліана буквально виштовхала її зі склепу."
"— Біжи!"
"Страх погнав Селену вгору сходами. Знизу долинув крик, потім лютий гарчання. Забувши про втомлені ноги, Селена понеслася ще швидше. Вона вискочила з порталу й тепер бігла сходами, що вели до її спальні. Втративши жертву, горгульї вили в безсилій люті. Селена знала: вони далеко й бар’єра їм не перетнути. Але це сьогодні…"
"Вона влетіла до кімнати. Останнє, що вона бачила, була її постіль. Потім усе занурилося в темряву."
"Селена розплющила очі. Вона важко дихала. Її здивувало, що на ній усе ще надіта зелено-блакитна сукня. Головне, тут вона в безпеці. Ну чому її переслідують кошмарні сни? І чому вона дихає так, ніби щойно звідкись прибігла? І чому в її мозку дзвенять слова: «Знищ зло, що причаїлося в замку»? Здається, вона їх уже чула. Уві сні."
"Вона повернулася на бік, мріючи знову заснути й потрапити зовсім в інший сон. Але щось упиралося їй у долоню. Так це ж кільце, подароване Шаолом. Звичайно кільце. Тільки воно."
"Самообман не вдався. Кільце було в неї на пальці й ніяк не могло впасти звідти на долоню. А на долоні лежав круглий амулет розміром із монету, прикріплений до тоненького золотого ланцюжка. Зовнішнє коло було обвите золотою филигранню. Усередині розташовувалися, перехрещуючись по вертикалі, два однакових кола. У їхній спільний простір був вставлений синій дорогоцінний камінь, що робив серединну частину амулета схожою на око. Зовнішнє коло мало видимий діаметр — тонку вертикальну нитку, центральний відрізок якої ховався всередині «ока»."
"Деякий час Селена роздивлялася амулет. Потім щось змусило її повернути голову в бік шпалери… Селена ледь не скрикнула: двері за полотнищем були прочинені!"
"Скочивши з постелі, Селена кинулася до шпалери, але спіткнулася об шлейф сукні й боляче вдарилася плечем об стіну. Роздивлятися плече вона буде потім, а зараз, стискаючи зуби, вона відвернула полотнище й силою грюкнула двері. Не вистачало ще «гостей» знизу! Чи другого появи Еліани."
"Шумно дихаючи, Селена стояла, уважно роздивляючись шпалеру, притиснуту до стіни комодом. Тільки зараз вона впізнала в зображеній на шпалері жінці Еліану. Постать королеви знаходилася саме там, де двері. «Збігів і випадковостей не існує». Виткана Еліана була розпізнавальним знаком."
"Селені раптом стало зябко. Вона підкинула дров у камін, нарешті зняла свою сукню й переодяглася в нічну сорочку. Потім поправила постіль і забралася під ковдру, поклавши поруч саморобний ніж. Їй знову трапилося на очі кільце. «Це вбереже тебе від небезпек…»"
"Вона ще раз глянула на замасковані двері. Звідти не долинало жодного звуку, ніби й не було нічого. Не було? Тоді звідки ця штучка? На балу такі явно не роздавали. Селена наділа амулет на шию. Він був теплим і зовсім невагомим. Селена натягнула ковдру до самого підборіддя й міцно заплющила очі. Вона мріяла міцніше заснути й не потрапити в сон, де чиясь кігтиста лапа відірве їй голову. Але ж усе, що сталося з нею цієї ночі, не було ні сном, ні маренням…"
"Селена стиснула ланцюжок амулета й подумала, що стане королівською захисницею. Обов’язково стане, бо іншої дороги до свободи для неї немає. Але Еліані її місія бачилася ширшою. Давня королева стверджувала, що Ерілея потребує саме такої захисниці, що розуміє страждання й сподівання народу. Можливо, Еліана не знала, що в нинішнього короля — інші погляди на місію свого захисника: знаходити й знищувати ворогів корони. Шкода, вона не встигла розповісти давній королеві про це."
"Другим повелінням Еліани було знайти й знищити зло, що причаїлося в замку. Але як? Вона ж не капітан королівської гвардії."
"Селена скрутилася клубочком. Ну й дурна ж вона! Відчинити потайні двері в ніч Самуїнна! Ще невідомо, які біди вона накликала на себе своїм безрозсудним цікавістю."
"Однак сон не йшов. Селена розплющила очі й у червонуватих відблисках каміна знову почала роздивлятися шпалеру. «Тобі належить зупинити це зло…»"
"Селена спіймала себе на тому, що веде мислену діалог із королевою Еліаною. Допитується, чому все обрушилося на її плечі. Може, королева не знала, що Селену всюди супроводжують або Шаол, або вартові?"
"Але якщо в замку таїться невідоме зло, воно загрожує не одній Селені, а всім. Вона б не заперечувала, щоб темні сили «почистили» замок, знищивши Кейна, Перангона, короля й Кальтену. А якщо разом із ними постраждають Нехемія, Доріан, Шаол?"
"Селена шумно видихнула. Схоже, їй знову доведеться відвідати склеп і там пошукати підказки. Може, щось і знайдеться. А якщо ні… що ж, Еліана хоча б дізнається про її спробу."
"У спальні прошелестів вітерець. Запахло трояндами. Селена ще довго ворушилася, перш ніж забутися важким сном."

#Епізод 14 

"Двері до її спальні розчахнулися навстіж. Селена скочила з постелі, встигнувши схопити важкий підсвічник. Увірвавшийся Шаол цього навіть не помітив. Селена повернулася до ліжка."
"— Капітане, ти мені даси сьогодні виспатися? — пробурчала вона, натягуючи ковдру. — Чи ти намірився святкувати до ранку? Може, ти переплутав двері?"
"Шаол мовчки витягнув її з постелі, боляче смикнувши за лікоть, і тільки тоді заговорив:"
"— Де ти була цієї ночі?"
"Страх стиснув їй горло. Капітан ніяк не міг дізнатися про її прогулянки сходами й коридорами."
"— Як де? — усміхнулася Селена, хоча їй було не до усмішок. — Чи ти забув, як приходив сюди й приніс мені ось це?"
"Вона висмикнула руку й поворухнула пальцями, показуючи йому кільце з аметистом."
"— Я пробув у тебе лічені хвилини. Де ти була весь інший час?"
"— Дивне запитання. Спала."
"Селена не відступила під його пронизливим поглядом. Невже цей Шаол кілька годин тому приносив їй кільце? Зараз він більше нагадував лютих вартових. Капітан вдивлявся в її обличчя, руки. Усе інше ховала довгопола нічна сорочка. Заспокоївшись, Селена теж почала розглядати капітана. Його мундир був наполовину розстебнутий і зім’ятий, а коротко стриженому скуйовдженому волоссю не завадив би гребінець. Капітан явно кудись поспішав і заскочив до неї, що називається, на бігу."
"— Що взагалі відбувається? — з підкресленою байдужістю запитала Селена. — Ти не даєш мені виспатися, а в нас сьогодні, між іншим, чергове випробування."
"— Випробування не буде. Ще одного претендента вбили. Ксав’єра, злодія з Мелісанди."
"Селена підняла очі на капітана й знизала плечима."
"— Ти думаєш, це я його вбила?"
"— Сумніваюся. Його труп був наполовину обгризений."
"— Обгризений? — Селена скривилася й сіла на постіль, уткнувши підборіддя в коліна. — Погана новина. Може, це Кейн? Не здивуюся, якщо він харчується людським м’ясом."
"Насправді Селені було не до жартів. Страх скував їй усі нутрощі. Ось і ще один убитий. П’ята смерть від початку змагань, і тільки дві з них цілком пояснені. Савена застрелили під час спроби втечі, а Коса зірвався зі стіни. Але решта? Глазопожиратель, роздертий солдат, тепер ще й Ксав’єр. Слова Еліани про зло, що причаїлося в замку, отримали нове підтвердження. Таке вже не поясниш звірством п’яних гвардійців чи нападом скаженого собаки, невідомо як потрапившого до замка. Це ланцюг, і ніхто не знає, скільки ланок додасться до нього в найближчі дні й тижні."
"— Дивне в тебе почуття гумору, — похмуро зауважив капітан."
"Вона змусила себе усміхнутися."
"— Кейн — перший, кого я б почала підозрювати. Та ти краще за мене знаєш, які у вас сусіди живуть серед Білокликих гір."
"Шаол пригладий волосся."
"— Твоя неприязнь до Кейна — ще не привід його підозрювати. Нехай він і люта скотина, але герцог Перангон обрав його своїм претендентом."
"— Теж мені, доказ! — усміхнулася Селена. — А мене своєю претенденткою… своєю захисницею обрав спадковий принц! І мої звинувачення не потребують дозволу різних там перангонів."
"— Скажи мені без викручування: де ти була цієї ночі?"
"Селена випрямила спину й, дивлячись капітанові прямо в його золотисто-карі очі, сказала:"
"— Тут, у цій постелі. Мало моїх слів, запитай у вартових. Якщо король вирішить мене допитувати, я завжди можу йому сказати, що ти й його високість готові бути моїми поручителями."
"Капітан побачив подароване ним кільце й злегка почервонів."
"— У мене є ще одна новина. Ми з тобою сьогодні не вправляємося."
"Селена широко усміхнулася йому, потім удавано зітхнула й лягла, натягнувши ковдру до підборіддя."
"— Чудова новина, капітане. Тобі залишилося тільки покинути мою спальню. Я хоч висплюся. Думаю, п’яти годин мені вистачить."
"Брехня, але капітан на неї повівся. Селена кокетливо затріпотіла віями й заплющила очі, а тому не бачила сердитого капітанського погляду. Шаол тихо вийшов. Селена дочекалася, коли за ним зачинилися вхідні двері, і тільки тоді сіла на постелі."
"Ксав’єра не просто вбили. Хтось устиг попоїсти на його тілі."
"Уночі, в тому сні… Годі себе дурити — це був не сон. Вона перебувала в склепі й чула жахливі крики горгулій… Може, Ксав’єра роздерло одне з чудовиськ? Але ж вони мешкають глибоко в підземеллі. У коридорах замка їх би одразу помітили. Можливо навіть, що спочатку Ксав’єра вбили, а потім якась погань обгризла його труп. Дуже, дуже голодна погань."
"Селену пересмикнуло. Спати вона, звичайно, не збиралася. Вона дістала своє імпровізоване знаряддя. Не густо, але іншого в неї немає. Зате є кілька годин свободи, якою вона розпорядиться по-своєму. Селена перевірила запори на всіх дверях і вікнах. Замкнути вхідні двері на засув вона не могла — це одразу викликало б підозру. Обмежившись замкненими дверима спальні, Селена рушила вниз. До склепу."
"Селена обійшла весь простір склепу й сама була готова ричати від досади. Жодних зачіпок, жодних знаків, щоб ясніше зрозуміти слова Еліани. Жодних натяків на джерело таємничого зла. Зовсім нічого."
"Але зараз склеп освітлювали промені сонця, і грудочки пилу, підняті ногами Селени, кружляли, як сніжинки. Склеп знаходився глибоко під землею. Як же будівельникам удалося наповнювати його місячним і сонячним світлом? Селена підійшла до решітки, що закривала світловий колодязь, задерла голову, придивилася."
"Ось воно що! Стінки колодязя були викладені листовим золотом. Безліч листів, відполірованих до дзеркального блиску. Це вони ловили світло й передавали його вглиб."
"Селена зупинилася між саркофагами. Права рука стискала саморобний ніж. Щось змусило її глянути на підлогу. На ній не було ні слідів кігтистих лап горгулій, ні її власних слідів. І жодних ознак того, що вночі тут побувала сутність Еліани."
"Вона повернулася до мармурової Еліани. Синій самоцвіт у короні давньої королеви переливався, ловлячи неяскраве сонячне світло."
"— Чому все це ти розповіла саме мені? — вголос міркувала Селена, залишивши всяку поважність."
"Відлуння повторило її запитання, відбиваючись від стін, вкритих «знаками долі»."
"— Еліано, ти померла тисячу років тому. Чому ж доля Ерілеї досі не дає тобі спокою? — допитувалася Селена."
"Чому давня королева не побажала з’явитися Доріану, Шаолу чи тій самій Нехемії?"
"Селена доторкнулася до здернутого носа статуї й повідомила:"
"— А ми-то думали, ти насолоджуєшся життям у потойбічному світі, геть забувши про це."
"Селені хотілося перетворити свої слова на жарт, але жарту не вийшло."
"Пора йти звідси. Рано чи пізно до неї в спальню почнуть стукати й, не отримавши відповіді, зламають двері. А якщо розповісти, що перша королева Адарлана минулої ночі поклала на неї важливу й відповідальну місію, їй навряд чи повірять. Селена скривилася, уявивши допит у королівській раді. Велике щастя, якщо її не звинуватять у державній зраді й застосуванні магії. Але ця прогулянка в підземелля цілком може закінчитися поверненням до Ендов’єра."
"Ще раз уважно оглянувши склеп, Селена пішла. Вона сподівалася прихопити з собою хоча б маленький ніж із вчорашньої купи зброї, але ні зброї, ні скрині з коштовностями сьогодні не було. Дамаріс теж зник."
"І потім, Еліана Еліаною, а в Селени — своя голова на плечах. І поки що вона не вільна розпоряджатися собою й своїм часом, тому спочатку треба досягти першої мети — стати королівською захисницею. Ось тоді їй ніхто не завадить вистежувати зло, що таїться в замку. А якщо намагатися робити це зараз, вона суттєво зіпсує собі шанси на перемогу."
"Селена поспішно піднімалася гвинтовими сходами. Знайдений нею факел чадів, породжуючи потворні тіні."
"‘Не розпорошуватися’, — твердила собі Селена."
"Треба зосередитися на змаганнях, на випробуваннях, а думки про невідоме зло загнати подалі. Раніше вона це вміла. Ось коли вона стане королівською захисницею…"
"Якщо стане."
"Через годину Селена в супроводі вартових ішла коридорами замка до бібліотеки. Її голова була високо піднята. Вона усміхалася молодим чоловікам, що траплялися їй назустріч, і хмикала, бачачи, як придворні дами пожирають очима її рожеву з білою оздобою сукню. Сукня справді зачаровувала, і сама Селена була в ній чарівною. Коли вона вийшла в коридор, Ресс — один із вартових — не втримався від компліменту. Селена скористалася цим і вмовила хлопця провести її до бібліотеки."
"Назустріч їй трапився один із членів королівської ради. Той здивовано підняв брови й щось промовив. Селену вразила хвороблива блідість його обличчя. Етикет вимагав зупинитися, вклонитися й вислухати якусь учтиву маячню, відповівши такою ж маячнею. Але Селена обмежилася легким кивком і пішла далі. Вона наближалася до повороту, з невидимої частини якого долинали гучні чоловічі голоси."
"Ресс і другий вартовій ледь встигали за нею. Ні, Селена зовсім не збиралася тікати. Прискорити крок її змусив добре знайомий запах. Точніше, сморід розкладаючогося людського тіла. До нього домішувався запах крові."
"Побачивши останки Ксав’єра, Селена згадала слова капітана. Ні, «наполовину обгризений труп» — це ще м’яко сказано. Дуже м’яко, якщо подивитися, що насправді залишилося від худорлявої тіла мелісандського злодія."
"Напарник Ресса пошепки вилаявся, а Ресс торкнув Селену за плече, вимагаючи не зупинятися. Люди, що оточили понівечені останки, знову говорили про скаженого собаку чи навіть вовка. Селену вони навіть не помітили, зате їй вистачило швидкого погляду, щоб роздивитися всі подробиці жахливої розправи над Ксав’єром."
"Грудна клітка злодія була роздерта, але ні нутрощів, ні кишок Селена не побачила. Можливо, їх забрав той, хто натрапив на труп, або вони зникли ще раніше. З вузького обличчя Ксав’єра лахміттям звисала шкіра, і червоніли западини вирваних шматків м’яса. Здавалося, він і зараз верещав від жаху, тільки ніхто не чув його криків."
"Яка там собака! Який вовк! Убивство не було випадковим. Ті, що сперечалися, ніби не помічали дірки на маківці, звідки були висмоктані чи вичерпані мізки. На стіні темніли сліди крові: не плями й не бризки. Схоже, вбивці щось написали кров’ю своєї жертви, а потім стерли. Але частина напису залишилася. Селена ледь не скрикнула: «знаки долі»! Їх було три, витягнуті в вигнуту лінію. Швидше за все, лінія була продовженням кола, яке вбивця накреслив біля тіла."
"— Боги небесні, — пробурмотів напарник Ресса, коли вони відійшли від страшного місця."
"Тепер зрозуміло, чому Шаол увірвався до неї в такому вигляді! Невже він подумав, що це вона вбила Ксав’єра? Дурень. Якби вона надумала позбутися суперників, вона б зробила це швидко й чисто. Вона асасин, а не потрошителька. Полоснути по горлу, точно вдарити ножем у серце, підсипати отрути у вино. Асасини так себе не поводять. Але при чому тут «знаки долі»? Виходить, убивство було ритуальним?"
"Їм назустріч ішов Могила. Селена пам’ятала, як він тоді ледь не загубив Нокса, і намагалася триматися від нього подалі. Його очі — два чорні лісові омутки — зіткнулися з її очима. Рот Могили оскалився в усмішці, оголивши гнилі зуби. Селена кивком вказала на останки Ксав’єра."
"— Не пощастило хлопцю, — сказала вона, намагаючись зробити вигляд, що зовсім не засмучена тим, що сталося."
"Могила усміхнувся й сховав свої скрючені пальці в кишенях поношених брудних штанів. Невже той, хто його обрав, пошкодував грошей, щоб хоч якось одягнути свого обранця? Видно, цей придворний сам не вирізняється розумом, раз знайшов собі таку шваль."
"— Шкода бідолаху, — без тіні співчуття відгукнувся Могила й пішов далі."
"Селена сухо кивнула й до самої бібліотеки більше не промовила ні слова. Із двадцяти чотирьох претендентів залишилося шістнадцять. До дня передостанніх поєдинків їх залишиться четверо. Ставки зростали. Їй треба було б дякувати вищим силам, що вирішили обірвати життя Ксав’єра. Але Селені чомусь не хотілося шепотіти слова подяки."
"До темряви залишалося зовсім небагато. Селена дивилася на чорну Часову вежу. Та ставала все темнішою, ніби її поверхня вбирала в себе промені призахідного сонця. Горгульї на вершині вежі були нерухомі, як і належить бути кам’яним статуям. Ні найменшого руху. Жодна з істот навіть не ворухнула кігтистим пальцем. Еліана назвала їх вартових. Вартових чого? Ах так, переходу між світами. Еліана їх дуже боялася. Якщо горгульї й були тим самим злом, чому ж давня королева не сказала прямо? Селена дивилася на них, хоча інтуїтивно відчувала: їй краще триматися від цих істот — навіть кам’яних — подалі. Зараз не час накликати біду на свою голову, інакше не дожити до заключного поєдинку й не стати королівською захисницею."
"І все-таки чому Еліана обмежилася туманними фразами?"
"— Та що ти прилипла до цих потворних істот? — запитала стоявша поруч Нехемія."
"— Як ви думаєте, вони здатні рухатися? — запитала Селена, повертаючись до принцеси."
"— Сама подумай, Ліліано: ну як таке можливо? Вони ж кам’яні, — засміялася Нехемія."
"Її ейлуейський акцент дещо зменшився."
"— А ви робите успіхи! — вигукнула Селена. — Як ми плідотворно позаймалися! Один урок, і ви вже повсюди соромите мене адарланською."
"Успіхи Селени в ейлуейській були значно скромнішими. Нехемія зупиняла її на кожному кроці, терпляче пояснюючи, чим правильна ейлуейська відрізняється від простонародного говору."
"— Які вони противні, — сказала Нехемія, косячись у бік горгулій."
"— Боюся, «знаки долі» не допоможуть, — зітхнула Селена."
"Один із знаків знаходився біля її ніг. Усього їх було дванадцять, і вони оточували Часову вежу. Значення кожного з них і загальний сенс залишалися для Селени повною загадкою. Із дванадцяти знаків жоден не збігався й навіть не був схожий на ті, що вона виявила біля роздертих останків Ксав’єра. Швидше за все, кількість «знаків долі» обчислювалася десятками, якщо не сотнями."
"— Тож ви справді не вмієте їх читати чи не хочете мені сказати? — без обиняків запитала принцесу Селена."
"— Ні, — коротко відповіла Нехемія й пішла в бік живих огорож, що обрамляли двір. — І тобі не раджу намагатися розгадувати їхній сенс, — додала вона, обернувшись через плече. — Нічим добрим це не закінчиться."
"Селена щільніше закуталася в плащ і пішла слідом. Усе в природі вказувало на швидку зиму. Ще кілька днів — і з неба посипле сніг. Але до Ільмаса, святкування нового року, ще півтора місяця, а до останнього поєдинку — два. Селена насолоджувалася теплом плаща. Вона добре пам’ятала зиму в Ендов’єрі. Коли живеш, точніше, прозябаєш у тіні Руннських гір, зима перетворюється на щоденну тортуру. Це просто диво, що вона зуміла не обморозитися. Але другої зими в Ендов’єрі їй точно не пережити."
"— Тебе щось турбує? — запитала Нехемія."
"— Вам здалося, — усміхнувшись, відповіла Селена своєю простонародною ейлуейською. — Зиму я не люблю, тільки й усього."
"— А я жодного разу не бачила сніг, — зізналася Нехемія, дивлячись у темніюче небо. — Я так хочу побачити зиму. Мені вона здається чарівним часом."
"— Будемо сподіватися, чарівність не пропаде, коли вам доведеться ходити холодними коридорами, прокидатися в холодній спальні й цілими днями мріяти про сонце."
"Нехемію це розсмішило."
"— А давай поїдемо зі мною до Ейлуе, коли я повертатимуся, — запропонувала вона. — Там ти дізнаєшся, що таке випалююче літо. Думаю, тоді ти оціниш і холодні коридори, і дні без сонця."
"Принцеса помилялася. Селена вже провела одне випалююче літо в Червоній пустелі, але воліла про це мовчати."
"— Я б із радістю побувала в Ейлуе, — сказала вона."
"Нехемія променисто усміхнулася:"
"— Значить, ти побачиш мою батьківщину."
"Мабуть, таким тоном вона віддавала накази."
"Звичайно, Селена промовчала й про можливість такої поїздки. Задравши голову, вона дивилася на помаранчево-червону громаду скляного замка."
"— Цікаво, Шаол розгадав хоч щось у цьому вбивстві? — сказала вона, звертаючись не стільки до Нехемії, скільки до себе самої."
"— Телохранителі мені розповіли… цю людину вбили… дуже жорстоко."
"— Не те слово, — пробурмотіла Селена."
"Скляний замок грав переливами золотавого, червоного й синього кольорів. Як не дивно, ця помпезна громада інколи бувала красивою."
"— Ти що, бачила тіло? — пожвавилася Нехемія. — Моїх телохранителів і близько не підпустили."
"Селена повільно кивнула."
"— Може, й на краще, що не пустили. Навряд чи вам захотілося б дізнатися подробиці."
"— Я не боягузка. Розкажи мені, — попросила Нехемія."
"— Що ж, слухайте, — зітхнула Селена. — Там усе було в крові. Стіни. Підлога. Усе перепачкане кров’ю."
"— Перепачкане? — перепитала Нехемія й одразу понизила голос до шепоту. — Ти не переплутала слова? Може, ти хотіла сказати — «забризкане»?"
"— Ні, слова я не переплутала. Таке відчуття, що хтось навмисне розмазав кров цього бідолахи по стінах і підлозі. І ще. Там кров’ю були намальовані «знаки долі». А потім їх старанно затирали."
"Селена зябко здригнула плечима, але не від холоду, а від жахливої картини, що постала в неї перед очима."
"— І це ще не все, — сказала вона. — У вбитого хтось вирвав нутрощі… Нехеміє, вам погано? Даремно я все це розповіла."
"— Ні. Продовжуй. Кажеш, у нього вирвали нутрощі? І тільки?"
"Селена пом’ялась, але вирішила викласти все:"
"— Не тільки. У нього пробили дірку на маківці й витрусили мізки. І вся шкіра на обличчі була здерта й звисала лахміттям."
"Нехемія кивала, дивлячись на голий кущ попереду. Принцеса прикусила нижню губу, а її пальці то стискалися, стискаючи поли довгої білої сукні, то розтискалися. Холодний вітер тріпав численні тонкі косички принцеси, тихо побрязкуючи вплетеними туди золотими прикрасами."
"— Вибачте мене, — ще раз сказала Селена. — Даремно я все це…"
"Ззаду почулися кроки, і раніше ніж обернулася, Селена почула знайомий голос:"
"— Глянь-но, хто тут гуляє."
"Селена напружилася всім тілом. У тіні Часової вежі стояв Кейн. Поруч із ним був його васал — горластий кучерявий злодійчук Верин."
"— Що тобі треба? — різко запитала Селена."
"Загоріле обличчя Кейна розтягнулося в посмішці. Селені здалося, що він став вищим на зріст. А може, це був простий обман зору."
"— Вигравати з себе знатну даму — ще не означає нею бути, — сказав Кейн."
"Селена подивилася на принцесу. Примруживши очі, Нехемія розглядала Кейна. Її рот був напіввідкритий."
"Нагородивши дивною фразою Селену, Кейн переключився на Нехемію. Його губи розійшлися в новій посмішці, оголюючи два ряди рівних білих зубів."
"— І надіта корона не робить принцесою. Уже не робить."
"Селена ступила до нього й сказала:"
"— Закрий свій дурнуватий рот, інакше я сама тобі його закрию, але спочатку вибиваю всі твої гарні зубки."
"Кейн грубо зареготав. Верин теж. Але відійшов подалі. Селена розправила плечі. Невже їй доведеться сутичка з Кейном?"
"— А собачка принца, виявляється, вміє голосно гавкати, — давлячись від сміху, виговорив Кейн. — Та тільки чи є в неї ікла?"
"Нехемія поклала руку Селені на плече, але Селена прибрала її й підійшла ще ближче до Кейна. Тепер вона відчувала на своєму обличчі пару від його дихання. Вартові ніби кудись попряталися. Тільки біля самого замка виднілося кілька ліниво прогулюючихся гвардійців."
"— Чи є в мене ікла? Це ти дізнаєшся, коли вони вп’ються в твою шию."
"— А чому не зараз? — видихнув Кейн. — Починай. Удар мене. Врежи мені з усією люттю. Ти ж завжди злишся, коли змушуєш себе не влучати в очко мішені чи тягнеш час, щоб не забратися на стіну нарівні зі мною. Удар мене, Ліліано, — повторив він і додав зовсім тихо, щоб чула тільки вона: — Подивимося, чого ти навчилася за рік життя в Ендов’єрі."
"Її серце загрожувало вистрибнути назовні. Він знає! Знає, хто вона й чим займалася. Селена не наважувалася глянути на Нехемію й сподівалася, що принцеса ще не навчилася розуміти швидку адарланську мову. Верин усе ще тримався осторонь."
"— Думаєш, у тебе однієї благодійник готовий розбитися в корж, аби ти перемогла? Чи думаєш, що, окрім принца й капітана, більше ніхто про тебе не знає?"
"Селена стиснула праву руку в кулак. Два удари — і бездиханний Кейн валятиметься на землі. Веріна вона заспокоїть і одним ударом."
"— Ліліано, нам пора, — адарланською сказала принцеса, беручи її за руку. — Нас справи чекають. Ходімо."
"— Ось-ось, — підхопив Кейн. — Собаченьки завжди за кимось бігають."
"У Селени тремтіли руки. Якщо зараз вона не витримає й ударить його… якщо між ними почнеться сутичка й вартовим доведеться їх розтягувати, тоді прощавай навіть мізерна свобода, яка в неї є. Шаол заборонить їй бачитися з Нехемією, змусить сидіти в чотирьох стінах. І їхнім вправам із Ноксом теж прийде кінець. Ні, вона не дозволить собі зірватися. Вона вміє вичікувати."
"Селена розправила плечі, усміхнулася й найневимушенішим тоном, на який була зараз здатна, сказала:"
"— Поцілуй себе в задницю, Кейне."
"Кейн і Верин знову зареготали. Селена й Нехемія пішли. Увесь цей час принцеса міцно стискала її руку. Не від страху й не від гніву, а щоб показати Селені: «Я розумію, де ти побувала». Селена відповіла тим самим. Про неї так давно ніхто не турбувався, що вона не звикла до співчуття."
"Шаол і Доріан стояли в тіні галереї й дивилися, як унизу Селена лупить по ганчір’яній ляльці, відпрацьовуючи навички ударів. Дізнавшись, що сьогодні вона вирішила вправлятися понад покладений час, капітан покликав із собою принца. Нехай побачить, на що здатна його претендентка. Може, тоді зрозуміє, наскільки вона небезпечна для нього й взагалі для всіх."
"Лялька тільки з виду здавалася м’якою. Усередині вона була набита піском. Селена, щось бурмочучи собі під ніс, безупинно молотила по ній лівою, правою, лівою, лівою, правою. Удари сипалися безперервно, ніби зовнішніми діями вона намагалася погасити те, що вирувало в неї всередині."
"— А вона стає сильнішою, — тихо зауважив принц. — Ти добре постарався, займаючись із нею."
"Селена вдаряла по ляльці руками й ногами, потім пригиналася й відскакувала вбік, ухиляючись від уявних ударів свого нерухомого «противника». Вартові біля дверей безстрасно стежили за її рухами."
"— Як ти думаєш, у неї є шанс перемогти Кейна? — запитав принц."
"Блискавичний удар ногою припав прямо по голові ляльки, перекинувши її. Для живого супротивника наслідки були б набагато серйознішими."
"— Є, якщо поєдинок із ним вона поведе холоднокровно й не дозволить злості верховодити собою. Але вона… нестримна. І непередбачувана. Дивно, що її не навчили керувати почуттями. Особливо раптовим гнівом."
"Шаол говорив правду. Він знав причину спалахів цього гніву. Можливо, позначилися місяці, проведені в Ендов’єрі. А може, це властиво всім асасинам. Але якою б не була причина, тримати гнів у вузді Селена не вміла."
"— А це ще хто такий? — незадоволено запитав Доріан, коли в залі з’явився Нокс."
"Той підійшов до Селени. Вона припинила лупити ляльку, витерла піт із чола й почала розминати пальці, обмотані клаптями."
"— Це Нокс, — пояснив Шаол. — Злодій із Перранта. Обранець радника Жуваля."
"Нокс щось сказав Селені, і та засміялася. Засміявся й він."
"— Завела собі дружка? — з легким роздратуванням запитав принц, бачачи, як Селена показує Ноксу один із ударів. — Вона що, допомагає цьому злодійчукові?"
"— Щодня. Коли закінчуються загальні заняття, вони залишаються й вправляються вдвох."
"— І ти це дозволяєш?"
"— Якщо бажаєте припинити їхні заняття, я це зроблю, — приховуючи незадоволення, відповів капітан."
"— Ні, — похитав головою Доріан. — Нехай вправляється з ним. Решта претендентів або жорстокі, або просто двоногі скоти. Союзник їй не завадить."
"— Селена це теж розуміє."
"Доріан повернувся й мовчки вийшов у сутінки коридору. Невдовзі червоний плащ принца розчинився в темряві. Шаол лише зітхнув. Ревнощі. Звичайнісінькі людські ревнощі. Незважаючи на розум і виховання, Доріан, як і Селена, не вмів приховувати свої почуття. Капітан пошкодував, що покликав принца сюди. Зітхнувши ще раз, Шаол рушив наздоганяти його, сподіваючись, що принц не накоїть з гарячого якихось дурниць."
"Через кілька днів Селена оголосила, що їй треба до бібліотеки. Замість вартових із нею пішов Шаол. Зараз він сидів за сусіднім столом і читав якийсь роман. Селена йорзала на стільці, гортаючи ламкі пожовклі сторінки важкого фоліанта. Поки що вона натикалася лише на довжелезні порожні фрази. Але вона вперто гортала фоліант, сподіваючись знайти там зображення «знаків долі»: і тих, що оточували Часову вежу, і намальованих кров’ю біля роздертих останків Ксав’єра. Основних запитань було два: навіщо невідомий убивця позбавляв життя претендентів і як він це робив. Чим більше відомостей вона знайде, тим краще. Селену турбувала реальна загроза, а не те містичне, незрозуміле зло, згадане Еліаною."
"Прогортавши пару сотень сторінок, Селена майже нічого не знайшла. У неї заболіли очі. У бібліотеці було сутінково. Якби не шелест сторінок книги Шаола, тиша приспала б її."
"Селена не наважувалася розповісти капітанові, що Кейн проник у її таємницю й що всі злодійські вбивства якимось чином пов’язані зі «знаками долі». Не зараз. У стінах бібліотеки їй нема чого думати про змагання й суперників. Тут вона може насолоджуватися тишею й спокоєм."
"— Ти закінчила? — запитав капітан, грюкаючи романом."
"— Ні ще, — буркнула Селена, барабанячи пальцями по столу."
"— На що ти гробиш свій вільний час? — усміхнувся капітан. — Добре ще, про це ніхто не знає. Інакше ти загробиш і свою репутацію, а Нокс піде від тебе до Кейна."
"Задоволений жартом, Шаол знову розкрив книгу й відкинувся на спинку стільця."
"‘Ідіот’, — подумала Селена. — Знав би ти, навіщо я риюся в цьому старому мотлоху й що шукаю. Тобі б розхотілося їдко жартувати. Між іншим, я ще й для тебе стараюся. За трупи відповідати не мені, а тобі’."
"Селена нахилилася й почухала погано гоячу рану на нозі. Цю рану їй завдав Шаол, коли в них був поєдинок на дубинках. Згадавши про це, Селена сердито глянула в бік капітана. Той нічого не відчув, продовжуючи читати."
"Під час занять капітан був до неї безжальний. Чого він тільки не змушував її робити: ходити на руках, кувыркатися через голову, вислизати від прямого удару, відволікаючи противника вражаючими обманними рухами… Усе це було їй знайоме, але знову відчувати себе дівчинкою-ученицею Селені дуже не подобалося. Зате поведінка капітана стала трішки кращою. Садонувши їй дубинкою по нозі, він потім вибачився. Сказав, що збирався вдарити вдвічі слабше. Селена зізналася собі, що капітан їй чимось навіть подобається."
"Вона шумно грюкнула фоліантом, піднявши хмаринку пилу. Досить шукати там, де нічого немає."
"— Ти що? — стрепенувся Шаол."
"— Та нічого, — похмуро відповіла Селена."
"Що ж таке «знаки долі» й звідки вони взялися? І взагалі, чому вона досі ніколи про них не чула? Цими знаками були вкриті всі стіни склепу Еліани й Гавіна. Уламки давно забутої релігії? Але кому знадобилося зберігати ці уламки? І чому поруч із понівеченими трупами хтось намалював їх кров’ю жертви «знаки долі»? Повинен же існувати якийсь зв’язок."
"Відомості, які Селені вдалося добути з товстенних книг, були вельми суперечливими. Автор одного трактату стверджував, що «знаки долі» були алфавітом. Селена було вхопилася за його твердження, але ще через сотню сторінок учений муж зізнався: «знаки долі» не пов’язані з граматикою жодної давньої мови."
"Автор іншого праці вкрай заплутав Селену. Він писав, що сенс кожного «знаку долі» визначався не тільки його місцем у загальному ланцюгу, а й сусідніми знаками. Малювати «знаки долі» було справою нелегкою: потрібно було точно витримувати довжину ліній і кути, інакше сенс повністю змінювався."
"— Чому ти все дуєшся? — докірливо запитав її Шаол. — Книги-то чим провинилися?"
"Він підвівся, підійшов до її столу й прочитав заголовок. Звичайно, він ніяк не був пов’язаний із убивством Ксав’єра."
"— Ну й що ти в них шукаєш?"
"— Нічого особливого, — збрехала Селена, прикриваючи фоліант руками."
"— А якщо сказати правду?"
"Селена зрозуміла: їй не викрутитися."
"— Пам’ятаєш, мене зацікавили «знаки долі» навколо Часової вежі? Ось я й вирішила пошукати відомості про них у книгах."
"Обмежившись напівправдою, Селена чекала саркастичних посмішок і їдких слів. Але капітан мовчав. Потім запитав:"
"— Чому ж ти така кисла? Відповідей не знайшла?"
"— Розумієш, усе, що я викопала, — суцільні здогадки й припущення, — надувши губи, зізналася Селена. — Ти чув таке словечко, як «Верд»? Автори деяких трактатів вважають Верд силою, яка керує Ерілеєю. І не тільки Ерілеєю, а й незліченними світами у Всесвіті."
"— Слово це я чув, — не зводячи очей із Селени, відповів Шаол. — Нічого загадкового в ньому немає. Я завжди думав, що Верд — це давнє слово, що означало щось на кшталт долі чи участи."
"— Я теж так думала. Але Верд — не релігія. У всякому разі, в північних частинах континенту. І Верд ніяк не пов’язаний із поклонінням Богині та іншим богам."
"Шаол опустив книгу на коліна."
"— І чому тобі не дають спокою ці знаки навколо Часової вежі? Невже ти вмираєш від нудьги?"
"‘Мені не дають спокою власна безпека. Ось так-то, пане капітане’."
"— Не скажу, що в замку дуже весело. Особливо в моєму становищі. Ось і доводиться замінювати нестачу свободи подорожами розуму. Знаєш, я тут на цікаве припущення натрапила. У одній книжечці знайшла. Там написано, що Богиня — всього-навсього дух із інших світів. Вона мандрувала між світами, а потім через «врата Верду» потрапила на Ерілею й побачила, що тут немає життя."
"— За такі слова тебе можуть звинуватити в святотатстві, — застеріг Шаол."
"Він добре пам’ятав часи, коли по всій Ерілеї палали багаття, а з плах падали відрубані голови. Йому тоді було дванадцять, і жахи страт міцно врізалися в пам’ять. Може, Селена думала, що йому було легше рости, ніж їй? А яково жити в тіні короля, що сіяв руйнування й горе? Шаол пам’ятав, як лицемірний двір оплесками зустрічав звістки про вбивство чужих королів, королев і спадкоємців. Друзі батька, попиваючи вино, зі сміхом розповідали, як спостерігали страту чергового мага чи відьми. А Ерілея невпинно занурювалася в темряву: затоплена кров’ю й сльозами, відкинута назад на цілі століття."
"Попередження не зупинило Селену. Їй потрібно було висловити вголос усе, що накопичилося в мозку. Може, тоді всі частини головоломки зберуться воєдино?"
"— А ще в одній книзі сказано: життя в Ерілеї існувало й до появи Богині. Була дуже давня цивілізація, яка потім зникла. Може, вони теж пішли через «врата Верду»? Збереглися руїни, які навіть народ фей називав давніми. Уявляєш?"
"Але як усе це пов’язане зі злодійськими вбивствами претендентів? І чи є взагалі тут хоч якийсь зв’язок? Цього Селена не знала. У її становищі вона чіплялася за будь-яку соломинку."
"Шаол відкинув книгу, підійшов до столу Селени й, нахилившись, запитав:"
"— Хочеш почути правду?"
"Селена витягнула шию, і він прошепотів їй на вухо:"
"— Твої слова схожі на марення божевільного."
"Селена різко відкинулася на спинку стільця й випалила:"
"— Прошу вибачення за інтерес до історії нашого світу!"
"— Це не історія. Здогадки. Припущення. Ти сама їх так назвала."
"Шаол знову сів і, розкривши роман, запитав:"
"— Я одного не можу зрозуміти: чому все це тебе так турбує?"
"Селена терла очі, боячись розридатися від досади."
"— Тому що я по горло сита здогадками й припущеннями. Я хочу знайти простий і ясний відповідь: що таке «знаки долі» й чому вони оточують Часову вежу?"
"У її запитанні був здоровий глузд. Король нещадно знищував усі сліди магії. Тоді чому він не наказав знищити «знаки долі» у себе під носом? І чому хтось намалював їх на коридорній стіні кров’ю вбитого Ксав’єра?"
"— Невже тобі більше нема чим заповнити вільний час? — запитав Шаол, занурюючись у читання."
"— Може, пряжу розмотувати для Фаліпи? Чи вишивати разом із нею? — огризнулася Селена."
"Вона не розуміла, навіщо взагалі капітан приплентався сьогодні до бібліотеки. Зазвичай вона ходила сюди в супроводі двох вартових, і ті нудьгували біля дверей, поки Селена рилася в пилових фоліантах. Невже йому захотілося побути поруч із нею? Здогадка була дурнуватою, але в Селени чомусь екнуло серце. Дівчина усміхнулася, але одразу прогнала шалену думку, змусивши себе повернутися до пошуків."
"Вона спробувала розкласти по поличках усе, що зуміла дізнатися. «Врата Верду». Кілька разів вони згадувалися разом зі «знаками долі». Вперше це поняття трапилося їй пару днів тому й здалося цікавим та інтригуючим. Селена почала копирсатися в книгах і сувоях, але ті розчарували її. Здавалося, автори трактатів змагалися між собою — хто придумає теорію позаковыристіше."
"Виходило, «врата Верду» були певними порталами, недоступними зору звичайних людей. Але за допомогою «знаків долі» люди могли викликати ці врата й входити в них. Значить, «врат Верду» було багато, і одні вели в добрі й світлі світи, а інші — в темні й небезпечні. Усі кровожерні хижаки, усі чудовиська прорвалися в Ерілею з темних світів."
"Селена підсунула до себе іншу книгу й широко усміхнулася. Ніби хтось читав її думки. Це був важкий чорний фоліант із потьмянілими сріблястими літерами назви — «Ходячі мерці». Добре, що капітан був поглинутий романом і не побачив, яку книжечку вона собі обрала."
"Але чи вона? Селена не пам’ятала, щоб така назва трапилася їй на книжкових полицях. Від книги виходив дивний запах вогкості, ніби та довго пролежала в землі. Морщачись, Селена почала гортати сторінки. Звичайно, вона шукала відомості про «знаки долі» й «врата Верду», а натрапила на щось набагато цікавіше."
"Перегорнувши ще кілька сторінок, Селена побачила гравюру. Їй зловісно усміхалося понівечене обличчя напівзгнилого трупа. На кістках гойдалися лахміття шкіри з прилиплими шматками м’яса. Селена здригнулася й розтерла змерзлі руки. Де ж їй трапився цей фоліант? І як взагалі його й безліч подібних книг не спалили дев’ять років тому? Чи король вважав, що в його бібліотеці жодних небезпечних книг немає й бути не може?"
"Селену знову пересмикнуло, тепер уже від жаху й відрази. Порожні, божевільні очі чудовиська були повні злоби. Їй здалося, що намальований мерць дивиться прямо на неї. Селена грюкнула книгою, відсунувши її подалі. Це велике благо, що на королівську бібліотеку ніхто всерйоз не звертав уваги, а то горіти б їй, як Головній бібліотеці Оринфа. І нікому було б ховати скарби знань і мудрості. Посаду королівського бібліотекаря скасували ще півстоліття тому."
"Шаол продовжував читати, забувши про її присутність. Селена збиралася ще раз зазирнути в жахливу книгу, але їй завадив дивний звук, що долинув із глибини бібліотеки. Звук нагадував приглушений звірячий крик."
"— Ти чув? — запитала Селена, смикаючи Шаола за рукав."
"— Нічого не чув, — відмахнувся капітан. — Краще скажи, коли ти збираєшся звідси йти?"
"— Коли втомлюся читати, — відрізала Селена."
"Вона знову відкрила чорний фоліант, підсунула до себе підсвічник і почала читати описи різних чудовиськ."
"Знову! Тепер уже зовсім поруч, мало не в неї під ногами. Скочивши, Селена відступила й ледь не вдарилася об сусідній стіл. На підлогу вона навіть боялася глянути, чекаючи, що зараз звідти висуне кігтиста лапа чи покажеться зубаста паща."
"— А це ти чув? — пошепки запитала вона."
"Шаол злорадно усміхнувся. Потім витягнув меч і поскріб ним мармурову підлогу, відтворивши «таємничий» звук."
"— Ідіот проклятий! — заричала на нього Селена."
"Вона підхопила дві книги й пішла до дверей. Чорний фоліант із потьмянілими сріблястими літерами так і залишився лежати на столі. У Селени не вистачило духу віднести його на полицю."

#Епізод 15

"Селена направила кий на білий, бойовий шар. Кий безшумно рухався між її пальцями. Знайшовши найзручніше положення для правої руки, Селена злегка нахилилася й ударила по шару. Той незрозумілим чином вивернувся з-під кия, відкотившись ліворуч."
"Пробурмотівши лайку, Селена зробила нову спробу. Цього разу кий ударив по білому шару. Шар, ніби цуценя, якого огріли батогом, закрутився по зеленому сукну й ткнувся в найближчий кольоровий шар. Хоч якийсь удар. І то успішніший, ніж її пошуки щодо «знаків долі»."
"Була одинадцята година вечора. Селена втомилася від вправ, від сидіння в бібліотеці, від роздумів про туманні слова Еліани й про можливі підлості Кейна. Але втома втомі рознь. Селена знала: лягати спати марно. Вона буде ворушитися з боку на бік і зіб’є собі весь сон. Сідати за клавікорди не хотілося, а грати самій із собою в карти вона не могла. Залишалося ганяти шари на більярдному столі. Беручи кий у руки, Селена щиро сподівалася, що швидко освоїть премудрості гри."
"Вона перейшла на інший край столу, прицілилася й… білий шар трохи покрутився на сукні й завмер. Стиснувши зуби, Селена ледь утрималася, щоб не переламати кий об коліно. Кажуть, грати в більярд учаться місяцями. Нічого, вона освоїть цю дурнувату гру за годину. До півночі вона буде легким рухом заганяти шари в лузу. А якщо не освоїть, розламає більярдний стіл на дрова й спалить Кейна живцем."
"Схопивши кий, Селена що є сили врізала по білому шару. Той зигзагами покотився по поверхні, розштовхав трапивші йому на шляху три кольорові шари, а третій відправив прямим повідомленням до лузи. Селена затамувала подих… Кольоровий шар завмер на самому краю лузи."
"Заверещавши від люті, Селена кинулася до лузи. Вона обругала шар, потім перенесла хвилю гніву на стіл, відхльоскавши його києм. Цього їй здалося мало, і вона запхала в лузу одразу три кольорові шари."
"— Ось уже не думав, що найкращий асасин світу так кепсько грає в більярд, — сказав Доріан, входячи до кімнати."
"Селена скрикнула й різко обернулася до нього. Вона була в вільній блузі й таких самих вільних штанях. Волосся вільно лежало по плечах, відпочиваючи від шпильок і заколок. Бачачи, як миттєво вона почервоніла, принц усміхнувся й нахилився до столу."
"— Якщо хочете образити мене, тоді не простіше так?"
"Селена махнула києм, закінчивши фразу досить непристойним жестом."
"Не звертаючи уваги на її випад, Доріан закотав рукави й узяв зі стійки інший кий."
"— Ти, випадково, не збираєшся вп’ястися в кий зубами? Якщо збираєшся, почекай, поки я покличу придворного художника. Таке миттєвість обов’язково треба закарбувати."
"— Ви що, прийшли знущатися з мене?"
"— Не треба так серйозно ставитися до всього."
"Доріан прицілився, ударив по білому шару, і той витончено покотився в бік зеленого шара, загнавши його в лузу."
"— Коли ти очманіло скачеш навколо столу й ще лупиш по ньому, мені не треба жодних лицедіїв."
"Доріан чекав нового спалаху злості, але Селена раптом засміялася:"
"— Кому забава, а кому — хоч на стіну лізь."
"Вона скопіювала всі рухи принца, але знову промахнулася."
"— Дозволь, я покажу тобі, як треба вдаряти по шару."
"Принц підійшов до неї, взявши її кий і відкладавши свій. Потім злегка підсунув Селену, зайнявши її місце. Серце в нього закалатало."
"— Дивись, як я тримаю кий. Великий і вказівний пальці завжди знаходяться біля самого кінця древка. Руку не затискай. І тобі всього-навсього потрібно…"
"Селена качнула стегнами, відштовхнувши принца й забравши в нього кий."
"— Нічого з мене дурну робити. Я знаю, як треба тримати кий."
"Білий шар знову довів Селені, що вона помилялася."
"— Ти мене не дослухала. Мало вміти правильно тримати кий. Потрібно ще й правильно рухати тулубом. Дозволь показати тобі й це."
"У словах Доріана не було жодного підступу. Колись точно так само вчили грати його самого. Праву руку він поклав поверх її правої руки, а ліву — поверх лівої. Звичайно, для показу рухів він був змушений майже притиснутися до Селени. Він показував цей прийом багатьом жінкам і ніколи не червонів. А тут Доріан раптом відчув, як його обличчя теплішає від приливу крові. Глянувши на Селену, він, на своє полегшення, побачив, що її обличчя таке ж червоне, якщо не червоніше."
"— Якщо ви не перестанете витріщатися на мене й не почнете показувати, я вирву ваші очка й заміню їх більярдними шарами, — пригрозила Селена."
"— Дивись уважно, — як ні в чому не бувало продовжив принц. — Жодного напруження. Потрібно тільки…"
"Тримаючи обидві її руки у своїх, Доріан злегка розвернув корпус Селени й плавно вдарив по шару. Шар слухняно покотився до лузи й сховався в ній. Доріан розтиснув руки."
"— Бачиш? Якщо все робиш правильно й без поспіху, удар виходить точним. Спробуй ще раз."
"Селена щось буркнула собі під ніс, потім сумлінно повторила всі рухи принца й ударила по бойовому шару. Той розметав усі кольорові шари, породивши хаос на столі. І все одно цей її удар був набагато кращим за попередні."
"Доріан махнув дерев’яним трикутником, вирівнюючи шари на столі."
"— Ну як, пограємо?"
"Гра тривала до другої години ночі. У самий розпал більярдного бою Доріан наказав подати «чогось смачненького». Селена віднекивалася, але непомітно для себе з’їла великий шматок шоколадного торта, додавши до нього й чималу частину шматка, призначеного Доріану."
"Принц вигравав усі партії, однак Селена майже не помічала цього. Поки її удари були більш-менш успішними, вона з дитячою безпосередністю хвалилася своїми успіхами. Кожен промах викликав у ній такий напад люті, що пекельне полум’я блідло порівняно зі словесним полум’ям, що виривалося з неї. Доріан реготав до упаду."
"У перерві між партіями вони говорили про книги. Точніше, говорила переважно Селена, а Доріан лише слухав. Мабуть, їй роками доводилося мовчати. Мовчання ввійшло в звичку, і принц боявся, як би Селена не спохватилася й не замовкла знову. Вона була лякаюче розумна й розуміла все, що він говорив про історію й політику. На його подив, Селена любила театр і зовсім не так, як жеманні придворні дами, що обожнювали порожні сльозливі п’єски. Доріан навіть пообіцяв звести її на виставу, коли «все це закінчиться». Селена раптом замовкла. Принц було злякався, що зіпсував таку прекрасну ніч, але Селена одразу заговорила про щось інше."
"Коли вони обидва зрозуміли, що більше грати не хочуть, Доріан розтягнувся в кріслі, підперши долонею підборіддя. Селена вмостилася в інше крісло, закинувши ноги на підлокітник. Сонними очима вона дивилася на вогонь у каміні."
"— Про що ти думаєш? — обережно запитав принц."
"— Сама не знаю, — позіхаючи, відповіла Селена, укладаючи голову на інший підлокітник. — Як ви вважаєте, убивство Ксав’єра й інших претендентів було випадковістю чи чиїмось задумом?"
"— Можливо. Хіба це щось змінює?"
"— Ні, — ліниво махнула рукою Селена. — Це я так."
"Не минуло й хвилини, як вона заснула."
"Доріан шкодував, що майже нічого не знає про минуле Селени. Та й Шаол, схоже, знав не більше. Капітан розповідав йому, що родом вона з Террасена. Рано залишилася без батьків, яких убили. І жодних пояснень — чому й за що. Ще загадковішими були обставини, що змусили Селену вчитися ремеслу асасина. А де вона навчилася грати на клавікордах? Невже в асасинів були уроки музики?.. Суцільні загадки."
"Доріану хотілося, щоб Селена сама розповіла йому про себе. Може, такий момент настане. А поки принц підвівся, розминаючи затерплі плечі. Він повернув у стійку обидва киї, склав акуратним трикутником шари на столі, після чого повернувся до посапуючої Селени. Коли він обережно торкнувся її плеча, вона щось заперечила крізь сон."
"— Ти, звичайно, можеш спати тут, але вранці в тебе болітиме все тіло."
"Майже не розплющуючи очей, Селена встала й попленталася до дверей. Бачачи, що вона ось-ось наткнеться на одвірок, Доріан підбіг і обережно взяв її за руку. Намагаючись не думати про теплу долоньку, принц провів дівчину до спальні. Селена впала на ліжко, навіть не відкинувши покривала."
"— Ваші книги тут, — промимрила вона, вказавши на столик."
"Доріан обережно увійшов до спальні. Селена лежала нерухомо, не розплющуючи очей. Простір спальні освітлювали три свічки: дві на великому столику й одна на маленькому. Доріан задув усі свічки й тільки тоді наважився підійти до її постелі. Спить вона чи тільки робить вигляд?"
"— Спокійної ночі, Селено, — сказав принц."
"Він уперше назвав її на ім’я, і ім’я легко злетіло з його язика. Селена щось пробурмотіла й не ворухнулася. На її шиї блищало якесь дивне намисто. Цікаво, звідки в неї ця штучка? Намисто здалося принцу достатньо знайомим, ніби десь він уже бачив таке. Ще раз глянувши на сплячу Селену, Доріан узяв прочитані нею книги й вийшов зі спальні."
"Якщо вона стане королівською захисницею, а потім отримає свободу, чи змінить це її поведінку й характер? Чи нинішня Селена — не більше ніж маска, яку вона начепила, аби отримати бажане? Але Доріану не вірилося, що Селена здатна лицемірити. Точніше, він не хотів у це вірити."
"Принц повільно брів до себе. У замку було темно й тихо."
"Наступного дня претенденти проходили чергове випробування. Селена стояла й дивилася на поєдинок Кейна з Могилою. Отже, Кейн розвідав, хто вона й звідки. Тепер усі її хитрощі й гра в «пані Ліліану» не допоможуть. Кейн напевно думав, що отримав владу над нею, і це дуже лоскотало його марнославство."
"Кейн і Могила упоєно билися. Дзвін їхніх мечів змушував Селену стискати зуби. Само випробування її не лякало. Між претендентами були влаштовані поєдинки. Переможці могли не турбуватися за себе, а долю переможених вирішував Брулло. Тільки від нього залежало, кому з них сьогодні доведеться попрощатися із замком."
"Треба віддати Могилі належне: він тримався молодцем. Незважаючи на тремтіння в ногах, він вперто протистояв Кейну. Але той був сильнішим, і зараз його удар ледь не збив Могилу з ніг. Нокс, що стояв поруч із Селеною, щось прошипів."
"Кейн майже не напружувався. Він навіть не спітнів. Випад, ще випад, і меч Кейна опинився біля горла конопатого асасина. Той оскалив свої гнилі зуби."
"— Чудово бився, — похвалив Кейна Брулло, поплескуючи його по плечу."
"Селена намагалася дихати якомога рівніше, заспокоюючи серцебиття."
"— Бережися, Кейне, — пролунав неголосний голос Веріна."
"Кучерявий злодій ухмилявся, поглядаючи на Селену. Вона зовсім не раділа, що їй випало змагатися з Верином. Добре, що не з Ноксом."
"— Так, Кейне, бережися, — повторив Верин. — Дівчина жадає отримати шматочок тебе."
"— Прикуси язика, Верине, — застеріг його Нокс, з труднощами стримуючи лють."
"— Чого? — ліниво запитав Верин."
"Сказано було навмисне голосно, щоб почули інші претенденти. Пелор, що вештався поблизу, відійшов на кілька кроків."
"— Захищаєш її, так? — не заспокоювався Верин. — У вас, мабуть, угода укладена. Вона для тебе ніжки розводить, а ти стежиш, щоб дівчинку не ображали. Я вгадав?"
"— Заткни своє рило, брудний кабане! — кинула йому Селена."
"Стояли біля стіни Доріан і Шаол підійшли ближче до місця поєдинків."
"— А то що буде? — зареготав Верин."
"Нокс напружився. Його рука потягнулася до меча. Але Селена не збиралася відступати."
"— Що буде? Язик тобі вирву!"
"— Припиніть! — гаркнув на них Брулло. — Наступна пара. Верин і Ліліана. Починайте."
"Верин одарував Селену зміїною усмішкою й попрямував у намальоване крейдою коло. Кейн обнадійливо поплескав його по плечу."
"Нокс торкнувся плеча Селени. Краєчком ока вона помітила спостерігаючих за нею Доріана й Шаола. Нехай дивляться. Досить із неї цієї дурнуватої гри в непримітність. І Кейн нехай подивиться."
"Верин мотнув головою, відкидаючи волосся з чола."
"— Як мені тебе почастувати? — їдко запитав він, піднімаючи меч."
"Селена пішла до нього, не поспішаючи витягати свою зброю. Ухмилка Веріна стала ще ширшою. Він махнув мечем, наміряючись закінчити поєдинок за лічені секунди. Але Селена кулаком ударила його по руці, вибивши меч. Другий її удар припав по лівій руці. Верин похитнувся. Селена махнула ногою. Верин ледь встиг вирячити здивовані очі, і тут же отримав найсильніший удар у груди. Його відкинуло за межі кола, де він шумно звалився на мармурову підлогу. Поразка. Швидка й нищівна. Зал завмер."
"— Якщо я знову почую від тебе щось подібне, наступного разу почастую мечем, — сказала Селена, плюнувши Верину під ноги."
"Повернувшись, вона побачила витягнуте обличчя Брулло."
"— Це й для вас урок, пане головний зброяр, — сказала йому Селена. — Мені потрібні справжні супротивники. А так… навіть меч не знадобився."
"Селена мовчки пройшла повз усміхненого Нокса й зупинилася біля Кейна. Вона дивилася йому прямо в обличчя. Належало б воно іншій людині, це обличчя можна було б навіть назвати приємним."
"— Ну ось і я, — сказала вона, розправляючи плечі. — Маленька собачка."
"Усмішка Селени сочилася отрутою."
"Чорні очі Кейна спалахнули."
"— Поки що я чую тільки гавкіт."
"Рука Селени так і норовила схопитися за меч. Ні. Не зараз."
"— Цікаво, який гавкіт почуєш ти, коли я виграю поєдинок із тобою."
"Перш ніж Кейн устиг їй відповісти, Селена пішла до столу, де стояли глечики з водою й кухлі."
"Із усіх претендентів тільки Нокс наважився з нею заговорити. Навіть Шаол утримався від докорів."
"Повернувшись до себе, Селена стала біля вікна. Над Рафтхолом ішов сніг. Великі сніжинки билися в скло. Провісниці швидкої хуртовини. Сонце не могло пробити пелену свинцевих хмар і лише додавало їм жовтувато-сірого відтінку, змушуючи сяяти все небо. Зовнішній світ здавався продовженням скляного замка."
"Відійшовши від вікна, Селена зупинилася перед старовинною шпалерою. Вона дивилася на безтурботне обличчя королеви Еліани й згадувала свої дитячі мрії. Як тоді їй хотілося перенестися в ту епоху. Хоча б частково її мрія здійснилася. Але Селена ніяк не думала, що до цього додасться битва за власну свободу. У дитячих мріях їй завжди хтось допомагав: вірний друг, старий однорукий солдат чи ще хтось. А тут… одна. Зовсім одна."
"Як їй зараз бракувало Саема. Він завжди знав, що й як робити, завжди прикривав її, хотіла вона того чи ні. Селена, не замислюючись, віддала б усі скарби світу, тільки б Саем був поруч."
"У неї щипало очі, але сліз не було. Рука ковзнула нижче й намацала амулет. Метал був зовсім теплим. Доторк до амулета, як не дивно, заспокоїв її. Вона трохи відійшла від шпалери, щоб бачити полотно цілком."
"У самому центрі стояв рослий, зрілий олень-самець, скоса поглядаючи на Еліану. У Террасені олень був символом королівського дому, заснованого Браноном, батьком Еліани. Нагадування про її корені, що залишилися в Террасені. Селена це добре розуміла. Куди б не занесла її доля, Террасен був і завжди залишиться частиною її душі."
"За вікном виє вітер. «Знайти зло, що причаїлося в замку…» Але єдиним злом у цьому світі був чоловік, що правив цим світом."
"А в цей час в іншій частині замка Кальтена Ромпір мляво плескала акробатам, що закінчили свої кувіркання й танці на руках. Нарешті їхнє довге представлення завершилося. Кальтена завжди вважала, що подібні розваги пасують для ярмаркових балаганів, але ніяк не для королівського замка. А ось королева Георгіна була на цей рахунок іншої думки, і Кальтені довелося сидіти біля трону й робити вигляд, що представлення її тішить і веселить. Вона розуміла: їй зроблено велику честь, за що вона мусить віддячити герцогу Перангону."
"Перангон домагався її, і Кальтена це знала. Загалом-то, при певному старанні вона могла б досягти шлюбу з ним і стати герцогинею. Однак цього Кальтені було мало. Дурно виходити за Перангона, коли Доріан поки що неодружений. Увесь тиждень мозок Кальтени вирував від міркувань. Звичайно, таке напруження не могло не викликати мігрень. Жодні зілля не допомагали. У скронях у Кальтени стукало: «Мені мало. Мені мало. Мені мало». Головний біль пробирався навіть у її сни, перетворюючи їх на кошмари. Прокинувшись, Кальтена марно намагалася згадати сон і не могла."
"— Ваша величносте, яке рідкісне задоволення ви подарували мені, запросивши подивитися на цих дивовижних акробатів, — сказала Кальтена, радіючи, що ті збирають свої стійки й обручі."
"— Так, вони сьогодні були просто в ударі."
"Королева блиснула зеленими очима й усміхнулася Кальтені. Як на зло, у цю мить мігрень атакувала голову пані Ромпір. Удар був настільки сильним, що Кальтена стиснула кулаки, сховавши їх у складках своєї пишної сукні апельсинового кольору."
"— Дуже шкода, що з нами не було принца Доріана, — ледь отямившись від болю, почала плести словесні мережива Кальтена. — Тільки вчора його високість говорив мені, як він любить сюди приходити."
"Брехня давалася Кальтені легко й якимось незбагненним чином втихомирювала підступну мігрень."
"— Доріан так і сказав? — запитала Георгіна, вскинувши попелясто-сірі брови."
"— Невже це дивує вашу величність?"
"Королева церемонно приклала руку до грудей."
"— Я думала, мій син відчуває огиду до подібних видовищ."
"— Ваша величносте, — прошепотіла Кальтена, — ви поклянетеся, що не видасте мене? Тоді я вам дещо розповім."
"— Звичайно не видам. Говори, — пошепки відгукнулася Георгіна."
"— Принц Доріан назвав мені причину."
"— Яку причину? — запитала королева, беручи Кальтену за руку."
"— Причину того, чому він рідко буває на придворних зібраннях. Принц сказав, що він занадто сором’язливий і просто губиться серед такого багатолюддя."
"Королева відкинулася на спинку крісла. Вогонь в її очах швидко згасав."
"— Я давно знаю про цю причину. Сама постійно чую про неї від принца. А я-то думала, ти розкажеш мені щось цікаве. Наприклад, що принцу сподобалася якась юна особа."
"У Кальтени кров прилила до обличчя, а в скронях знову застукали важкі молотки. І як вона могла не взяти з собою жодних зілля? Але ж не прикладати ж флакон до носа, сидячи поруч із королевою. Тільки ще не вистачало, щоб Георгіна дізналася про її мігрень. Асамблея могла тривати ще й годину, і дві. Усе залежало від настрою королеви. Піти раніше Георгіни означало б серйозно зіпсувати собі репутацію."
"— Я чула, — майже пошепки продовжила королева, — що в замку з’явилася якась молода особа, але хто вона — невідомо. У всякому разі, її ім’я нікому нічого не говорить. Може, ти щось знаєш про неї?"
"— Ні, ваша величносте, — відповіла Кальтена, посилено проганяючи з обличчя досадливе вираз."
"— Як шкода. Я сподівалася, що вже ти-то неодмінно знаєш. Ти ж, Кальтено, така розумна."
"— Дякую вам, ваша величносте. Ви дуже добрі до мене."
"— Чепуха! Справа не в доброті. Я вмію безпомилково судити про людей. З самого моменту твоєї появи при дворі я побачила в тобі надзвичайно кмітливу жінку. Тільки така, як ти, і може скласти пару для Перангона. Дуже прикро, що мій Доріан не зустрівся тобі раніше герцога!"
"‘Мені мало. Мені мало’, — знову застогнала мігрень."
"Кальтена змусила себе усміхнутися. Наставав її час."
"— Ваша величносте, навіть якби Доріан зустрівся мені раніше герцога, ви б не схвалили такий союз. Я ж занадто низького походження, щоб привернути увагу вашого сина."
"Усе це говорилося з шанобливим хихиканням."
"— Твоя краса й багатство компенсують цей недолік."
"— Дякую вам, ваша величносте, — знову промовила Кальтена, в якої закалатало серце."
"Якби королева прихильно поставилася до її союзу… Кальтена ледь встигла про це подумати, як Георгіна двічі плеснула в долоні. Заграла музика, але Кальтена її не чула."
"Що ж, бальні черевички Перангон їй здобув. Тепер пора танцювати."

#Епізод 16

"— Цілитися треба!"
"— А я, по-твоєму, що роблю? — огризнулася крізь зуби Селена, натягуючи тятиву лука."
"— Тоді стріляй."
"Для вправ у стрільбі Шаол обрав покинутий коридор. Відстань, з якої потрібно було вразити ціль, налякала б будь-кого, але тільки не її."
"— Подивимося, чи вдасться тобі влучити."
"Селена відповіла йому гримасою й трохи випрямила спину. Тятива тремтіла в її руці. Подумавши, Селена злегка підняла наконечник стріли."
"— Завдання: влучити в ліву стіну, — сказав капітан."
"— Якщо не замовкнеш, стріла влучить тобі прямо в голову."
"Селена повернулася до нього, насолоджуючись враженням, яке справила. Шаол відчутно напружився, але нічого не сказав. Продовжуючи дивитися на капітана, Селена злорадно усміхнулася й, не дивлячись, вистрілила."
"Стріла просвистіла кам’яним коридором, і невдовзі пролунав глухий звук. Але Селена й Шаол продовжували дивитися одне на одного. У капітана були втомлені й трохи запалені очі. Схоже, за три тижні, що минули після вбивства Ксав’єра, він спав уривками."
"Вона й сама не могла похвалитися міцним сном: прокидалася від кожного шереху. А Шаол досі так і не дізнався, кому знадобилося вбивати претендентів одного за одним. Селену більше хвилювало не це, а те, за якими ознаками вбивця обирав собі чергову жертву. Взаємозв’язку між п’ятьма вбивствами не простежувалося. Єдиною спільною рисою було лише те, що всі жертви були претендентами на титул королівського захисника. Селена не знала, чи залишили «знаки долі» і на місці двох нещодавніх убивств. Її туди не пустили."
"Селена зітхнула й опустила лук."
"— А Кейн знає, хто я насправді, — раптом зізналася вона."
"Обличчя Шаола не змінилося."
"— Звідки? — тільки й запитав він."
"— Йому розповів Перангон. А він знайшов зручний момент і ляпнув мені."
"— Коли?"
"Відчувалося, її словесна стріла влучила прямо в ціль. Капітан помітно напружився."
"— Кілька днів тому, — збрехала Селена, хоча минули вже тижні. — Я гуляла садом із Нехемією. Не хвилюйся, вартові йшли за мною. Раптом, звідки не візьмися, Кейн. Він усе знає про мене й навіть знає, що на заняттях і під час випробувань я намагалася не показувати свої справжні навички."
"— Як ти думаєш, Кейн розповів про тебе й іншим претендентам?"
"— Сумніваюся. У всякому разі, Нокс нічого не знає."
"Шаол обхопив ефес меча."
"— Дивний поворот. Розігрувати посередність більше немає сенсу. Не засмучуйся. Ти все одно переможеш Кейна в поєдинках."
"— Ти ніяк повірив у мене? — злегка усміхнувшись, запитала Селена. — Будь обережний, капітане."
"Шаол почав щось говорити, але йому завадив тупіт біжучих ніг, що пролунав у них за спиною. Там коридор робив поворот. Невдовзі звідти вибігли двоє захеканих гвардійців. Побачивши капітана, вони зупинилися й віддали військове вітання."
"Капітан почекав, поки вони віддихаються, і запитав:"
"— Що сталося?"
"Один із вартових — літній, лисий дядько — знову відсалютував і збивчиво промовив:"
"— Пане капітане… там… словом, вам туди треба."
"Обличчя Шаола знову не змінилося, але звістка його насторожила."
"— Що сталося? — повторив він, уже поспішніше."
"Селена це одразу помітила."
"— Новий труп, — відповів гвардієць. — У коридорі для слуг."
"Другий вартовій — щупленький хлопець — був зовсім блідий, і в нього тремтіли губи."
"— Ви бачили тіло? — запитала Селена."
"Дядько кивнув."
"— Кров встигла висохнути чи ні? — поставила вона нове запитання, заслуживши незадоволений погляд Шаола."
"— Уночі зарубали, — висловив свою здогадку гвардієць. — Кров уже наполовину висохла."
"Шаол дивився кудись убік. Відчувалося, вирішував, що робити."
"— Хочеш глянути, куди влучила твоя стріла?"
"— А треба?"
"Шаол махнув гвардійцям, що готовий іти з ними."
"— Ходімо, — коротко кинув він Селені, ледь обернувшись через плече."
"Забувши на мить про труп, вона досить усміхнулася."
"Перш ніж піти за капітаном, Селена все ж оглянула місце, куди влучила її стріла. Капітан мав рацію: вона промахнулася, пустивши стрілу лівіше на цілих шість дюймів."
"Хтось здогадався навести відносний порядок і виставити оточення навколо вбитого. І все одно капітанові й Селені довелося протискуватися крізь натовп слуг упереміш із гвардійцями."
"Ледь глянувши на труп, Селена відчула, як у неї слабшають ноги й опускаються руки. Шаол люто вилаявся."
"Селена не знала, на чому зосередитися насамперед: то на тілі з роздертою грудною кліткою й діркою в голові, то на слідах кігтів, що зуміли подряпати камінь. Але найсильніше приголомшили два «знаки долі», намальовані крейдою по обидва боки від лежачого тіла. У Селени похолола спина. Ось вони, сліди зла, про яке говорила Еліана."
"У натовпі охали й перешіптувалися. Капітан підійшов до одного з вартових оточення й запитав:"
"— Хто цього разу?"
"— Верин Іслік, — відповіла Селена раніше, ніж вартовій устиг розкрити рота."
"Вона впізнала б Веріна де завгодно. Його кучеряве волосся не сплутаєш ні з яким іншим. Від самого початку змагань він ішов серед перших. Виходить, її позбавили ще одного небезпечного суперника…"
"— Чиї ж це кігті можуть дряпати камінь? — запитала вона в Шаола."
"Капітан відповів щось незрозуміле, і Селена зрозуміла, що він сам губиться в здогадках. Невідомий звір із кігтями, які запросто проробляють у камені борозни глибиною не менше чверті дюйма. Селена провела пальцем по виїмці. Камінь був шорстким, але чистим. Насупивши брови, вона почала розглядати інші сліди."
"— Зверни увагу: у жолобках, залишених кігтями, немає слідів крові, — сказала вона Шаолу."
"Капітан присів навпочіпки поруч із нею й теж роздивлявся сліди."
"— Ти чуєш? Борозни чисті."
"— І що? — не зрозумів Шаол."
"— А те, що звір спочатку заточив кігті об підлогу й тільки потім кинувся на Веріна."
"— Я не розумію, що особливого ти в цьому знайшла?"
"Селена підвелася, оглянула сліди з висоти свого зросту, потім знову присідала."
"— Звірюга нікуди не поспішав. Розумієш? Він спокійно заточив кігтики, а потім кинувся й роздер Веріна."
"— Але звір міг спочатку заточив кігті, а після затаїтися й підстерігати свою жертву."
"Селена похитала головою."
"— Поглянь на факели. Усі вони догоріли майже до основи. Коли факели гасять, на стіні залишаються патьоки брудної води. Значить, убивство відбувалося при світлі факелів."
"— І що? — знову запитав Шаол."
"— А тепер поглянь на цю частину коридору. До найближчих дверей — футів п’ятдесят, а до найближчого кута й усі сімдесят буде. Якщо факели горіли…"
"— Верин мав би ще здалеку побачити небезпеку."
"— Тоді чому він не втік, а пішов назустріч вірній смерті? — запитала Селена, звертаючись не стільки до Шаола, скільки до себе. — Тільки тому, що в той момент ніякого звіра в коридорі ще не було. Але був якийсь чоловік. Знайомий чи незнайомий Верину — не так важливо. І цей чоловік раптом накинувся на Веріна, позбавив його можливості втекти, а потім покликав свою звірюгу. Як тобі такий хід?"
"Капітан мовчав."
"— Поглянь на щиколотки Веріна, — продовжувала Селена. — Бачиш сліди порізів? Йому перерізали сухожилля, щоб не втік."
"Селена підійшла до трупа, намагаючись не зачепити «знаків долі». Переборюючи огиду, вона підняла негнучу, холодну руку Веріна."
"— Поглянь, які в нього нігті. Стерті й обломані."
"У її горлі застряг грудок слини. З труднощами проковтнувши його, Селена своїм нігтем вичистила бруд під нігтями Веріна й розтерла його на своїй долоні."
"— Дивись! Пил і дрібні шматочки каменю."
"Вона підняла ліву руку вбитого й побачила слабкі борозни, залишені нігтями. Такі ж борозни знайшлися й біля правої руки."
"— Верин відчайдушно намагався відповзти. Він чіплявся нігтями за підлогу. Звір у цей час точив кігті, а його господар дивився на них обох."
"— І що все це означає? — запитав приголомшений капітан."
"— Це означає, — похмуро усміхнулася Селена, — що тобі додалося головного болю."
"У Шаола зблідло обличчя. Селену трясло від власної логіки. Вона б зараз багато чого віддала, щоб її міркування виявилися лише грою наляканого розуму. Але все невблаганно свідчило про протилежне, і висновок був страшнішим за міркування. Виходило, що претендентів убивала таємнича зла сила, про яку говорила Еліана."
"Селена сиділа за обіднім столом і лихоманково гортала книгу, принесену з королівської бібліотеки."
"Нічого. Ну рівним рахунком нічого! Селена намагалася знайти хоч якийсь натяк на сенс двох «знаків долі», залишених біля тіла Веріна. Навряд чи вбивця хотів похизуватися своїм знанням давніх символів. Повинен же бути якийсь зв’язок між цими жорстокими вбивствами й «знаками долі». Знайти б хоч крихітну зачіпку."
"Натрапивши на карту Ерілеї, Селена зупинилася. У картах було щось чаклунське; якась влада над простором, коли знаєш, де знаходишся сам і куди хочеш вирушити. Селена обережно провела пальцем уздовж східного узбережжя. Подорож почалася на півдні — в Банджалі, столиці Ейлуе. Роблячи зигзаги й виписуючи плавні криві, палець Селени став рухатися через увесь континент до Рафтхола. Вона «проїхала» Меа, потім рушила північніше й західніше, до Оринфа. Звідти повернулася до моря, опинившись на Соріанському узбережжі. Поступово Селена дісталася до самого краю континенту. Далі було Північне море."
"Як і належить на картах, Оринф був позначений жирним гуртком із крапкою всередині. Місто світла й знань, перлина Ерілеї, столиця Террасена. Місто, в якому вона народилася. Не бажаючи бередити душу, Селена шумно грюкнула книгою."
"Знову знайомий стан: хилить у сон. Але якщо лягти зараз, вона або буде ворушитися з боку на бік, або зануриться в черговий кошмар. Сни Селени наповнювалися давніми битвами. Їй снилися очісті мечі. «Знаки долі» кружляли над її головою: різнокольорові, осліпливо-яскраві. Вона бачила воїнів народу фей у блискучих обладунках і смертних людей, які билися з ними. Вона чула злобне ричання диких звірів і задихалася від запаху крові й гниючих трупів. Рідкісний сон обходився без поля битви, усіяного трупами. Подумавши, що сьогодні їй знову судилося зануритися в ці жахи, найкращий асасин Адарланського королівства здригнулася."
"— Добре, що ти ще не лягла, — пролунав у дверях голос спадкового принца."
"Селена зіскочила зі стільця, але ввійшов справді виявився Доріаном. Принц виглядав втомленим і трохи засмученим."
"— Ваша високосте, що це вас принесло на ніч глядя? — без жодної ввічливості запитала Селена. — Скоро північ, а в мене завтра — знову випробування."
"Разом із тим вона була рада появі принца. Вбивця вирішував нападати на претендентів, тільки коли вони були самі."
"— Бачу, твої інтереси перемістилися з літератури на історію? — запитав Доріан, роздивляючись книги на столі. — «Коротка історія сучасної Ерілеї», — прочитав він. — А це що? «Символ і сила. Ейлуейська культура й звичаї»."
"Дорін запитально подивився на неї."
"— Я читаю те, що мені подобається, — пояснила Селена."
"Він сів на стілець поруч, і його нога торкнулася її ноги."
"— Ти обираєш книги навмання, чи між ними є якийсь зв’язок?"
"— Кажу вам: я обираю книги за назвами, — збрехала Селена."
"Звичайно ж, у кожній книзі вона шукала хоча б крихти відомостей про «знаки долі». Книгу про Ейлуе вона взяла з тієї ж причини."
"— Гадаю, ви вже чули про загибель Веріна."
"— Так, — похмурніючи, відповів Доріан."
"Близькість його ноги насторожувала Селену, але вона не могла змусити себе відсунутися."
"— Невже вас не хвилює, що вже стільки претендентів стали жертвами якогось дикого й кровожерного звіра? Може, хтось для забави тримає його в своїх покоях?"
"— У нас щодо тварин суворі правила. Якщо якась придворна дама хоче завести собі собачку, вона просить дозволу."
"Доріан нахилився до Селени й продовжив, дивлячись їй прямо в очі:"
"— Ти даремно турбуєшся. Усі ці вбивства відбувалися в темних, порожніх коридорах, якими, окрім слуг, ніхто не ходить. Тебе всюди супроводжують вартові, а твої покої надійно охороняються."
"— Я турбуюся не про себе, — не надто щиро сказала Селена, злегка відсуваючись від принца. — Уявляю, як усе це відбивається на репутації вашого шанованого батька."
"— Селено, я тебе не впізнаю! — здивовано вигукнув Доріан. — Коли востаннє ти хвилювалася за репутацію мого «шанованого батька»?"
"— З тих пір, як я погодилася стати претенденткою його сина. У вас же напевно є свідомі люди. Доручіть розслідування їм. Бажано зробити це раніше, ніж я виграю заключний поєдинок, бо тоді я опинюся останньою живою претенденткою."
"— Чи будуть ще якісь вимоги? — запитав Доріан."
"Його губи були зовсім поруч."
"‘А не вкусити його?’ — раптом подумала Селена."
"— Ні, ваша високосте. Поки це все. Якщо я ще щось придумаю, то неодмінно повідомлю, — тоном придворної дами відповіла вона."
"Хто ж він насправді, цей спадковий принц? Селені не хотілося визнаватися собі, але вона раділа, що зараз не сама. Нехай це навіть людина з династії Хавільярів, зате він поруч із нею."
"Зусиллям волі Селена викинула з голови думки про відмітини кігтів на кам’яній підлозі й про трупи, у яких викрали мозок."
"— А чому ви в такому похмурому стані? Ніяк пані Кальтена змучила вас своїми люб’язностями?"
"— Кальтена? Хвала богам, я цілих два дні її не бачив. Але в мене сьогодні видався на рідкість огидний день. Цуценята виявилися суцільними дворняжками."
"Доріан обхопив голову руками."
"— Цуценята?"
"— Так. Я так чекав, коли одна з найкращих моїх сук ощенилася. І на тобі! Спочатку це непомітно. А тепер вони підросли… Я так сподівався на чистоту кровей."
"— Вибачте, ми говоримо про собак чи про жінок?"
"— А яку тему ти віддаєш перевагу? — лукаво усміхнувся принц."
"— Ні ту, ні іншу, — насупилася Селена, викликавши задоволений смішок Доріана."
"— Дозволь запитати, чому ти виглядаєш такою засмученою? — Принц перестав усміхатися. — Шаол казав, що взяв тебе на огляд трупа. Сподіваюся, тебе не це стривожило."
"— Це мене зовсім не стривожило, — знову збрехала вона. — Просто останнім часом я погано сплю."
"— Яке збіг. Я теж, — зізнався Доріан. — Може, пограєш мені на клавікордах?"
"Селену не раз дивувало вміння принца легко змінювати теми розмови."
"— Сьогодні ні. І не просіть, — сказала вона, бо їй справді не хотілося грати."
"— Тоді ти так чудово грала."
"— Якби я знала, що за мною будуть шпигувати, я б взагалі не підійшла до клавікордів."
"— Тобі для гри потрібен якийсь особливий стан? — запитав Доріан, відкидаючись на спинку стільця."
"— Так. Я не можу ні слухати музику, ні грати сама без… Не будемо про це."
"— Ні, будемо. Що ти хотіла сказати?"
"— Нічого цікавого, — відповіла Селена, збираючи книги в стопку."
"— Музика будить у тобі спогади? — запитав принц."
"Селена дивилася на нього, намагаючись уловити хоча б найменші сліди насмішки. Але їх не було. Запитання прозвучало цілком щиро."
"— Інколи, — коротко відповіла вона."
"— Спогади про твоїх батьків?"
"Принц теж підвівся й допоміг їй зібрати решту книг."
"— Не треба ставити мені таких дурнуватих запитань! — відрізала Селена."
"— Вибач, якщо моє цікавість зайшла занадто далеко."
"Селена промовчала. Двері в одну з кімнат її пам’яті, яку вона завжди намагалася тримати міцно зачиненою, раптом розчахнулися, і тепер Селена відчайдушно намагалася зачинити ці небезпечні двері. Особливо небезпечні, коли Доріан зовсім поруч і їхні обличчя розділені якоюсь парою дюймів… Нарешті двері зачинилися, і Селена поспішно повернула ключ."
"Звичайно, Доріан навіть не здогадувався, яку битву з собою довелося їй витримати."
"— Тому й запитую, що нічого про тебе не знаю, — пішов він на попятну."
"— Я асасин. У минулому — в’язниця Ендов’єра. Зараз — одна з претенденток на титул королівського захисника, — уже спокійним тоном відповіла Селена. — Думаю, вам цього достатньо."
"Принц зітхнув."
"— Але чому мені не можна дізнатися про тебе побільше? Наприклад, як ти стала асасином? І якою була твоє життя до цього?"
"— Нічого цікавого."
"— Я запитую не з пустої цікавості."
"Селена мовчала."
"— Добре, — не вгамовувався принц. — Тоді дозволь поставити тобі всього одне запитання. Обіцяю, воно буде найзвичайнішим."
"Селена обвела очима акуратну стопку книг. Що ж, на одне запитання вона цілком може відповісти. Чи не відповісти, якщо вважатиме його новою спробою вторгнення в її життя."
"— Я згодна. Одне запитання."
"Доріан розплився в усмішці й сказав:"
"— Дай мені трохи часу. Я хочу придумати гідне запитання."
"Селена знизала плечима й сіла."
"— Чому ти так любиш музику? — запитав принц."
"— Здається, ми домовлялися щодо звичайного запитання, — зробила гримасу Селена."
"— Ти вважаєш його занадто нав’язливим? Чим воно відрізняється від запитання про те, які книги ти любиш читати?"
"— Ні. Сам по собі це чудове запитання. — Вона заговорила, намагаючись дивитися не на принца, а на візерунок скатертини. — Я люблю музику, бо, коли я її чую, я… гублюся всередині себе. Ось так, якщо мої слова мають сенс. Я одночасно стаю порожньою й наповненою. Я відчуваю биття землі. Коли я граю, я… нічого не руйную. Навпаки, я творю звуками."
"Селена прикусила губу, але зупинитися вже не могла:"
"— Мені хотілося стати цілителькою… Це було давно… до того, як мені довелося вчитися іншому ремеслу… Але я пам’ятаю: в ранньому дитинстві я хотіла лікувати людей. Музика нагадує мені про це."
"Вона тихо засміялася. Потім, побачивши усмішку принца, сказала з образою в голосі:"
"— Я нікому про це не розповідала. Не смійся з мене."
"Доріан одразу перестав усміхатися."
"— У мене й у думках не було сміятися з тебе. Я просто…"
"— Ви просто не звикли, коли люди відкривають вам серце?"
"— Так."
"— Тепер моя черга, — злегка усміхнувшись, сказала Селена. — Чи тут існують обмеження?"
"— Жодних, — відповів Доріан, закладаючи руки за голову. — Я не настільки потайливий, як ти."
"Селена насупила лоба, ніби підбирала запитання. Насправді це запитання давно крутилося в неї в мозку."
"— Чому ви досі не одружилися?"
"— Не одружився? Мені ще й двадцяти немає!"
"— Але ж у спадкового принца є якісь зобов’язання."
"Доріан склав на грудях м’язисті руки. Селена намагалася не помічати сили, що виходила від них."
"— Запитай про щось інше, — сказав принц."
"— А мені хочеться отримати відповідь на це запитання. Думаю, відповідь буде дуже цікавою, раз ви так опираєтеся."
"Принц повернувся до вікна, де за склом клубочився сніг."
"— Я не одружений, — зізнався він, — бо мені огидна сама думка одружуватися з жінкою, яка розумом і духом нижча за мене. Для моєї душі це означало б смерть."
"— Але шлюб — не магічний ритуал, а крок, спрямований на збереження й зміцнення влади королівської династії. Спадковий принц не має права піддаватися романтичним поривам. А якщо б батько наказав вам одружитися в інтересах політичного альянсу? Невже б ви воліли розпочати війну, тільки б зберегти ваші романтичні ідеали?"
"— Ти це не так розумієш."
"— А як? Хіба батько не може наказати вам одружитися з якоюсь принцесою заради посилення своєї імперії?"
"— Для посилення імперії в батька є армія."
"— Шлюб не зобов’язував би вас любити тільки свою дружину й бути їй вірним. Ви могли б полюбити іншу жінку. Таке часто бувало в житті королів."
"Сапфірові очі Доріана спалахнули."
"— Або одружитися з тією, яку любиш, або не одружуватися взагалі."
"Селена мимоволі засміялася."
"— А наді мною, — спалахнув він, — значить, можна глузувати? Ти ж смієшся мені в обличчя!"
"— За такі дурні думки ви й заслуговуєте глузування. Я говорила мовою серця. А в вас зараз говорить лише самолюбство."
"— Як ти ловко виносиш судження!"
"— Навіщо тоді потрібен розум, якщо не міркувати й не виносити судження?"
"— А навіщо тоді потрібне серце, якщо воно не береже інших від суджень твого розуму?"
"— Чудово сказано, ваша високосте!"
"Доріан дивився на неї, надувшись, ніби хлопчисько."
"— Буде вам злитися. Навряд чи я так серйозно вас поранила."
"— Ти намагалася зруйнувати мої мрії й ідеали. Я й так достатньо натерпівся від матері. Не можна ж бути такою жорстокою."
"— Не треба звинувачувати мене в жорстокості. Я міркую з практичної точки зору, а це зовсім інше. Ви спадковий принц Адарлана. У вас є рідкісна можливість змінити життя в Ерілеї на краще. Ви могли б створити світ, де щастя було б можливим і без справжнього кохання."
"— І який же це був би світ?"
"— Такий, де люди самі керують собою."
"— Це анархія. Більше того, це замах на основи держави. Добре, що нас тут ніхто не чує."
"— Я зовсім не закликаю до анархії. Можете називати мене зрадницею. Мене вже й так судили як асасина."
"Доріан підсунувся до неї, і його пальці торкнулися її пальців: жорстких, мозолистих, але теплих."
"— Тебе так і тягне заперечувати всьому, що я говорю."
"Селену охопило занепокоєння, але вона не ворухнулася. Мабуть, він хотів розповісти їй щось важливе, а вона своїми дурнуватими розмовами все зіпсувала."
"— Які в тебе дивні очі, — раптом сказав Доріан. — Ні в кого я не бачив очей із золотими обідками."
"— Якщо ви лестите мені, сподіваючись домогтися від мене відомих утіх, то у вас нічого не вийде."
"— У мене немає таких думок. Я просто розмовляю з тобою."
"Його рука все ще лежала поверх її руки."
"— До речі, а звідки в тебе це кільце?"
"Селена висмикнула руку й стиснула пальці в кулак. Полум’я каміна грало на аметистовому гуртку."
"— Подарунок, — відповіла вона."
"— Від кого?"
"— Вас це не стосується."
"Навряд чи Шаолу сподобається, якщо Доріан дізнається, що це він приніс їй кільце."
"Принц знизав плечима й сказав:"
"— Просто мені хотілося знати, хто ж обдаровує кільцями мою захисницю."
"Селена спіймала себе на дивному бажанні. Вона дивилася на комір його чорного камзола; точніше, туди, де комір стикався із засмаглою шкірою шиї, і їй нестерпно хотілося ніжно провести своїм мозолистим пальцем по його шиї."
"— Пограємо в більярд? — запитала вона й підвелася. — Готова отримати ще один урок гри."
"Не чекаючи його відповіді, Селена попрямувала до кімнати для ігор і музикування. Їй дуже хотілося опинитися поруч із Доріаном і відчути на своєму обличчі тепло його дихання. Їй подобалося це відчуття. Але що ще гірше, вона раптом зрозуміла: їй подобається не тільки це відчуття. Їй подобається сам Доріан."
"У її постелі, в ногах, хтось стояв."
"Селена відчула це ще уві сні. Прокинувшись і не розплющуючи очей, вона обережно просунула руку під подушку й дістала ніж, зроблений нею зі шпильок, мотузки й мила."
"— Це зайве, — промовив жіночий голос."
"Селена рвком сіла на постелі, почувши голос Еліани."
"— А проти мене ще й зовсім марне, — додала давня королева."
"У Селени кров застигла в жилах. Перед нею, вся в примарному сяйві, стояла перша королева Адарлана. Постать Еліани була цілком відчутною, але контури її обличчя й тіла сяяли так, ніби були виткані зі зоряного світла. Довге сріблясте волосся обрамляло її дивовижно гарне обличчя. Вона усміхалася, дивлячись, як Селена запихає під подушку свою зброю."
"— Здрастуй, дитино, — сказала Еліана."
"— Що вам тут потрібно? — похмуро запитала Селена й тут же осіклася."
"Де відбувається їхня розмова? Уві сні? А якщо наяву? Почують чи їх вартові? Селена напружилася всім тілом, готова вистрибнути з постелі й побігти. Але куди? Швидше за все, до балкону, бо Еліана загороджувала їй шлях до дверей."
"— Хочеш знати, навіщо я прийшла? Просто щоб нагадати тобі: ти обов’язково мусиш перемогти в змаганнях."
"— Я це й сама знаю, — огризнулася Селена. «І заради цього вона мене розбудила?» — Я наміряюся перемогти не заради вас, а заради своєї свободи. Може, у вас є якісь корисні відомості? Чи тільки це… нагадування? Ви-то, напевно, знаєте, що за злодій косить претендентів, вириваючи в них нутрощі й мозок. Тож розкажіть."
"Еліана зітхнула, звівши очі до стелі, й зізналася:"
"— На жаль, я знаю не більше твого."
"Відчуваючи, що її слова лише сильніше роздратували Селену, королева додала:"
"— Ти все ще мені не довіряєш. Що ж, я розумію твої побоювання. Але віриш ти мені чи ні, ми з тобою перебуваємо на одному боці."
"Перевівши погляд на похмуру Селену, Еліана сказала:"
"— І ще я прийшла, аби застерегти тебе. Уважно стеж за тим, що праворуч."
"— Що-що? — перепитала Селена. — Знову туманні слова. А зрозуміліше можна?"
"— Дивись праворуч. Там знайдеш відповіді."
"Селена повернула голову праворуч, але нічого, крім шпалери, не побачила."
"— Ви мене…"
"Еліани в її спальні вже не було."
"Недоспана Селена розглядала столик, уставлений чашами з різнокольоровими рідинами. Від часу Самуїнна минуло майже три тижні. Попереднє випробування — метання ножів — Селена пройшла легко. Знову одним суперником менше. Але метальник-невдаха хоча б залишився живим і відправився назад до в’язниці. А ось ще одного претендента два дні тому усунули все тим же злодійським способом."
"Селена майже перестала спати. Шукаючи розгадку «знаків долі», вона приносила з королівської бібліотеки все нові книги й гортала їх, засиджуючись допізна. Нерідко вона схоплювалася серед ночі й починала перевіряти, міцно чи замкнені вікна й двері. Вона прислухалася до всіх стукотів і шерехів, боячись почути дряпання кігтів по каменю. На вартових, що охороняли вхід до її покоїв, надії було мало. Якщо чудовисько зуміло подряпати твердий камінь, що для нього четверо гвардійців?"
"Посеред зали, заклавши руки за спину, стояв Брулло. Він мовчки стежив за тринадцятьма залишеними претендентами. Ті завмерли кожен перед своїм столиком. Королівський зброяр глянув на годинник. Селена зробила те саме. У неї залишалося п’ять хвилин. За цей час вона мала не тільки розпізнати сім отрут, налитих у чаші, а й розташувати їх за силою дії: починаючи з найслабшого й закінчуючи найсильнішим."
"Однак справжнє випробування настане після закінчення цих п’яти хвилин, коли кожен претендент мусить випити зілля, яке він вважав найслабшим. У разі помилки… Брулло запевняв, що протиотрута напоготові, і того, хто грубо помилиться, усе одно врятують. І все ж…"
"Селена взяла одну з чаш, піднесла до обличчя, принюхалася. Запах був солодким, навіть надто солодким. Щоб відбити цей запах, у чашу додали пустельного вина. Селена злегка збовтала вміст, намагаючись визначити колір, але в бронзовій чаші це було зробити важко. Тоді вона занурила в чашу палець. По нігтю потекла пурпурова рідина. Напевно, тут знаходився розчин красавки."
"А що в інших чашах? Болиголов. Вовча стопа. Аконіт. Олеандр. Селена переставила чаші, помістивши красавку перед чашею зі смертельною дозою олеандру. Залишалося три хвилини."
"Вона взяла передостанню чашу. Принюхалася. Знову принюхалася. Вміст нічим не пахнув."
"Тоді Селена відвернулася від столика й кілька разів вдихнула повітря, прочищаючи ніздрі. Вона пам’ятала: коли нюхаєш різні сорти парфумів, то незабаром перестаєш розрізняти запахи. На цей випадок у парфумерів завжди під рукою якесь очищувальне засіб, що відновлює нюх. Селена знову понюхала вміст чаші, потім опустила в рідину палець. Схоже, що в чашу була налита звичайна вода…"
"Можливо, там справді була вода. Селена повернула чашу на столик і взяла останню, сьому. Судячи з вигляду, там знаходилося вино. Вино з тонким ароматом. Закусивши губу, Селена глянула на годинник. У неї залишалося дві хвилини."
"Хтось із претендентів лаявся крізь зуби. Той, хто припустився найгрубішої помилки, відправиться туди, звідки прибув… якщо протиотрута встигне подіяти."
"Селена знову понюхала чашу з водою, подумки згадуючи отрути, що не мають запаху. Але всі вони, якщо їх змішати з водою, давали якийсь відтінок. Селена взяла чашу з вином, хитнула, роздивляючись круговерть рідини. До вина можна підмішати будь-які сильнодіючі отрути, і воно відб’є їхній смак і запах. Знати б, що підмішано сюди."
"Ліворуч від Селени стояв Нокс, теребячи своє темне волосся. Він уже розставив чотири чаші й тепер мучився з останніми трьома. А часу залишалося півтори хвилини."
"Отрути, отрути, отрути. У Селени пересохло в роті. Якщо вона провалить випробування, чи буде Еліана докоряти їй?"
"Повернувши голову праворуч, Селена натрапила на погляд Пелора — довготелесого молодого асасина. Він стежив за нею й теж намагався визначити місця чаш із вином і безбарвною рідиною, дуже схожою на воду. Селену здивувало, що Пелор поставив чашу з водою в самий кінець, а чашу з вином — на початок."
"В очах асасина щось блиснуло. Пелор ледь помітно кивнув їй. Сам він стояв, заклавши руки в кишені. Він своє завдання виконав. Побоюючись, що Брулло помітить, Селена поспішно перевела погляд на свої чаші."
"Отрути. А адже ще в саме перше їхнє випробування, з тріском проваливши стрільбу з лука, Пелор заявив Брулло, що дуже вправний у застосуванні отрут."
"Селена скоса глянула на асасина. Столик Пелора знаходився праворуч від неї. «Дивись праворуч. Там знайдеш відповіді»."
"Селену прошиб холодний піт. Еліана сказала їй правду!"
"Пелор байдуже дивився на годинник, чекаючи, коли закінчаться п’ять відпущених хвилин. Але з якої стати він вирішив їй допомогти?"
"Селена поспішно поставила чашу з вином на самий початок. Чаша з безбарвною рідиною відправилася в кінець."
"Допомога Пелора дивувала її насамперед тим, що після Кейна Пелор був другим, хто найбільше знущався з неї. Насторожувало Селену й те, що з деяких пір Брулло раптом став благоволити Пелору. У Ендов’єрі вона завжди сторонилася тих, до кого наглядачі ставилися більш-менш прихильно."
"Решта претендентів мовчки переглядалися, не звертаючи жодної уваги на Пелора. Схоже, навіть Брулло забув, у чому сильний цей асасин, інакше головний зброяр напевно ускладнив би це випробування. Скажімо, відгородив би столики ширмами."
"— Час вийшов. Усім остаточно розставити чаші, — наказав Брулло."
"Доріан із Шаолом мовчки стояли біля стіни, спостерігаючи за Селеною й рештою претендентів. Цікаво, помітили вони підказку Пелора?"
"Нокс заковирливо вилаявся й поставив свої чаші в загальну чергу, навіть не намагаючись міняти їх місцями. Більшість претендентів зробили те саме. Тому Брулло, підходячи до претендента й велячи випити найслабшу отруту, майже кожному подавав флакон із протиотрутою. Дуже багато хто вважав вино пасткою й поставив чашу з ним у самий кінець. Ноксу теж знадобилася протиотрута: у нього першою стояла чаша з аконітом."
"Селена з насолодою дивилася, як почервоніло обличчя Кейна, що скуштував красавки. Верзила залпом проковтнув протиотруту. Селена щиро пошкодувала, що в Брулло не закінчився запас пухирців. Досі ніхто з претендентів не переміг у цьому випробуванні. Один випив безбарвну отруту, вважаючи її водою, і звалився на підлогу раніше, ніж до нього підбіг Брулло з протиотрутою. Селена згадала назву цієї отрути — «поцілунок зі смертю». Отрута вбивала дуже швидко. Навіть краплина її викликала жахливі галюцинації й втрату почуття реальності. Брулло все ж встиг врятувати бідолаху, але той був не в силі встати. Підоспілі гвардійці підняли його й понесли до лазарету."
"Нарешті Брулло зупинився біля столика Селени."
"— Давай, пробуй, — байдуже дивлячись на неї, велів головний зброяр."
"Селена озирнулася на Пелора. Світло-карі очі асасина блиснули. Вона піднесла чашу з вином до губ і зробила ковток."
"Нічого. Не було ні дивного смаку, ні миттєвих відчуттів у тілі. Але ж і повільні отрути спочатку не викликали жодних відчуттів."
"Брулло простягнув до неї руку зі стиснутими пальцями. Селена похолола. Невже й їй доведеться пити протиотруту? Але пальці Брулло розтиснулися, і він схвально поплескав Селену по спині."
"— Ти права: це просто вино."
"Почувши його слова, претенденти зашепотілися."
"Останнім, до кого підійшов Брулло, був Пелор. Асасин пригубив із чаші з вином. Брулло поплескав по плечу й його зі словами:"
"— Ти теж переміг у цьому випробуванні."
"Пролунав оплески. Їм обом аплодували й претенденти, й наставники, й навіть гвардійці. Селена з вдячністю подивилася на Пелора, і той густо почервонів."
"Звичайно, вона злегка обдурила Брулло, але вона виграла. Селена не трималася за перемогу й була готова розділити її з Пелором. А ось дякувати Еліані їй не хотілося навіть подумки. Нехай королева їй і допомогла, це нічого не змінювало. Можливо, їхні шляхи тимчасово переплелися. Ну й що? Селена не збиралася надалі служити туманним задумам Еліани. Їй потрібна ясність, а королева двічі обмежувалася загальними фразами, не бажаючи нічого розповідати."
"Злість на Еліану не минала. Не буде вона служити примарній королеві, навіть якщо та підкаже, як виграти в завершальному поєдинку."

#Епізод 17

"Сьогодні Селена й Нехемія скоротили свої мовні заняття й вирішили прогулятися садом. Нагулявшись, вони повернулися до замку й тепер повільно брели просторими коридорами. Телохранителі принцеси й вартові Селени рухалися слідом. Можливо, Нехемію й дивувало, що за її подругою всюди слідує півдюжини солдатів, однак думки з цього приводу вона тримала при собі. До Ільмаса залишався місяць, до остаточного поєдинку — місяць і п’ять днів. Далеко не завжди Селені хотілося займатися, але вона не могла порушити обіцянку, дану принцесі, і тому справно вчила Нехемію адарланської й училася в неї ейлуейської. Вона змушувала принцесу читати вголос, обираючи найцікавіші книги в королівській бібліотеці. Попутно Селена вирішила виправити вельми корявий почерк принцеси. Під її наглядом Нехемія кілька разів переписувала якийсь уривок, поки рядки не набували рівності, а букви — розбірливості."
"Найкраще принцесі давався розмовний адарланський. Тепер вона говорила досить швидко й правильно. Але між собою Селена й Нехемія спілкувалися ейлуейською. Їм подобалося дивитися на придворних, що виходили з себе від цікавості й намагалися підслухати, але не розуміли жодного слова. До того ж їх не могла підслухати й охорона Селени. Згадуючи Ендов’єр, Селена неохоче визнавалася собі, що хоч чомусь навчилася в цій жахливій дірі."
"— Ти сьогодні мовчазна, — сказала Нехемія. — Щось сталося?"
"Селена змусила себе усміхнутися. Так, сталося. Усю ніч вона знову проворочалася без сну, мріючи, щоб швидше настав ранок. У замку — новий роздертий труп."
"А тут ще Еліана зі своїми наказами! Можна подумати, служницю знайшла!"
"— Знову зачиталася допізна, ось і сонна трохи, — збрехала Селена."
"Вона озирнулася. Коридор був незнайомим. У цю частину замку вона ще не забредала."
"— Усередині тебе багато тривог, — раптом сказала Нехемія. — Я чую те, про що ти не говориш. Ти не наважуєшся розповідати про свої турботи й біди, але очі тебе видають."
"‘Невже мене так легко читати?’ — подумки здивувалася Селена."
"— Ми ж із тобою подруги, — продовжувала Нехемія. — Коли тобі знадобиться моя допомога, ти тільки скажи."
"У Селени ком став у горлі."
"— Мене давно ніхто не називав своїм другом, — зізналася вона, кладучи руку на плече принцеси. — Я…"
"Слова Нехемії приоткрили всередині Селени дуже небезпечні двері, і звідти, наче чорні хмари, поповзли спогади. Селена ледь стримувала їхній натиск."
"— Усередині мене є такі куточки, які…"
"Селена замовкла. Знову цей звук, що переслідував її у снах. Гуркіт десятків і сотень копит. Неминуче наближаюча стіна грому… Селена різко струснула головою. Гуркіт зник."
"— Дякую тобі, Нехеміє. Ти справжня подруга, — зовсім не лукавивши, сказала Селена, переходячи з принцесою на «ти»."
"У неї калатало серце, але темрява всередині поступово розсіювалася."
"Нехемія раптом скривилася, ніби теж згадала щось неприємне."
"— Уявляєш, королева запросила мене сьогодні подивитися виставу. Щось із її улюблених п’єс. Може, підеш зі мною? Якщо я чогось не зрозумію, ти перекладеш."
"Селена теж скривилася й сказала:"
"— Я… напевно, не вийде."
"— Не можеш піти, — з помітним роздратуванням промовила Нехемія."
"Селена винувато подивилася на неї."
"— Є певні обставини… — почала Селена, але принцеса затрясла головою."
"— У всіх нас є свої секрети… Загалом-то, мені цікаво, чому капітан так стежить за тобою, а вечорами замикає в чотирьох стінах. Будь я наївною простачкою, я б сказала, що вони тебе бояться."
"— Капітан лише виконує те, що йому наказано, — усміхнулася Селена."
"Вона згадала слова принцеси про вечірнє представлення, і втихла було тривога знову заворушилася в ній."
"— Значить, — сказала Селена, — адарланська королева до тебе прихильна? І ти не намагалася… потихеньку вирватися з-під її опіки?"
"Принцеса злегка похитала головою й відповіла:"
"— Відносини між нашими країнами зараз дуже напружені. Спочатку я намагалася триматися від Георгіни подалі, але потім змінила свою поведінку. Будь я просто знатною гостею, ніхто б не змусив мене слухати довгі й порожні промови королеви. Але я принцеса й повинна думати про інтереси батьківщини. І я почала частіше з’являтися в покоях королеви. Про що б не заходила розмова, я намагалася показати королеві, що відносини між Адарланом і Ейлуе можна поліпшити мирним шляхом. І сьогоднішнє запрошення я сприймаю як доказ моїх успіхів."
"Ось воно, тягар народжених у королівських родинах. Розумом Селена розуміла: Нехемія намагається, щоб її задуми дійшли до вух адарланського короля."
"— Уявляю, як це порадує твоїх батьків, — сказала Селена й усміхнулася, хоча сама терпіти не могла дипломатію."
"Із глибини коридору долинув заливистий собачий гавкіт."
"— Куди ми з тобою забрели? — запитала Селена."
"— На псарню, — повідомила Нехемія. — Принц водив мене сюди вчора й показував цуценят. Для нього це був зручний привід, щоб утекти від материнських розмов."
"Шаол явно не зрадів би, що вона гуляє такими місцями. А вже візит на псарню…"
"— Нам можна туди зайти?"
"— А чому ні? — здивувалася Нехемія, гордо розправляючи плечі. — Я ейлуейська принцеса й можу гуляти скрізь, де забажаю."
"Селені не залишалося нічого іншого, як піти слідом за сваволною принцесою."
"По той бік важких дубових дверей пахло так, що Селена скривилася й навіть хотіла затиснути ніс. Настінні факели освітлювали просторе приміщення, де в клітках і на прив’язі мешкало безліч собак найрізноманітніших порід."
"Тут були пси-гіганти, зростом їй по пояс. Цих тримали в клітках. На ланцюгах, прикріплених до дерев’яних жердин, бігали туди-сюди довгоногі сухорляві собаки. Усі породи були по-своєму красиві, однак щире захоплення в Селени викликали гончаки з витончено вигнутими тілами й такими ж витонченими ногами. У цих собаках поєднувалися краса, благородство й незвичайна швидкість. Їхня поведінка теж разюче відрізнялася від решти собачого племені. Гончаки не гавкали, не скиглили й не вили. Вони сиділи тихо й лише проводжали Селену своїми темними мудрими очима."
"— І це все — мисливські собаки? — запитала вона."
"Відповіді не було. Принцеса встигла піти вперед і тепер із кимось розмовляла. Другий голос теж був дуже знайомий Селені. Пройшовши ще кілька кроків, вона побачила ліворуч від себе щось на кшталт загона з напіввідчиненими воротами. У них стояв усміхнений Доріан. Нехемія вже перебувала всередині, розташувавшись за витонченим столиком."
"— Вітаю вас, пані Ліліано, — церемонно промовив Доріан, опускаючи на підлогу кумедного мохнатого цуценя із золотисто-бурою шерстю. — Не чекав побачити вас тут. Втім, враховуючи палку пристрасть Нехемії до полювання, я не дивуюся, що вона привела сюди й вас."
"На людях принц завжди тримався з Селеною офіційно. Спочатку це її дратувало, але потім вона звикла."
"— Тож це й є дворняжки? — запитала Селена, киваючи в бік чотирьох цуценят."
"Доріан підняв на руки іншого цуценя, погладив його по витягнутій голові й зітхнув:"
"— На жаль, це вони. Я просто приголомшений, хоча віддаю належне їхній чарівності."
"Цуценята, відчувши, що розмова йде про них, заверещали від радості, а двоє навіть підскочили до Нехемії на коліна. Селена увійшла. Принц зачинив ворота."
"— А чому той цуценя сумує в кутку? — запитала Нехемія, вказуючи на п’ятого цуценя. — Він хворий?"
"П’ятий цуценя був трохи більшим за інших і відрізнявся від них сріблястою із золотими прожилками шерстю. Він теж зрозумів, що говорять про нього, і уважно подивився на людей. Селена, не розбираючись у собаках, подумала, що п’ятому пощастило й він народився чистопородним."
"— Ні, цуценя цілком здорове, — відповів Доріан. — Просто він перебуває в поганому настрої й не бажає спілкуватися ні з людьми, ні зі своїми родичами."
"— Напевно, не без причини, — сказала Селена, прямуючи до сумного цуценя. — А чому він повинен тявкати й махати хвостом, якщо йому не хочеться? Тільки тому, що ви принц?"
"— Я не тільки принц, а насамперед — людина, — учтиво усміхнувся Доріан. — Собаки цінуються своєю здатністю ладнати з людьми й підкорятися їм. Якщо цуценя не відгукується на дружнє ставлення до нього, з нього виростає пес із непередбачуваним характером. А непередбачувані собаки бувають дуже небезпечними. Щоб уникнути зайвого ризику, таких цуценят зазвичай убивають."
"Усе це було сказано легко, з усмішкою, однак Селені стало не по собі."
"— Убивають? Ви й цього вб’єте? Але чому? Чим він устиг вас образити?"
"— Собаки цінуються тим, що вони друзі й слуги людей, — повторив принц."
"— Значить, ви готові вбити цього бідолаху тільки через його характер? Але це жорстоко. Може, він сумує без матері. До речі, де його мати?"
"— Насмілюся припустити, пані Ліліано, що у вас ніколи не було собак. Можливо, вас здивує, що собачі матері не тремтять над своїм потомством, як людські. Мати цих цуценят прибігає, тільки щоб їх нагодувати та інколи пограти. І потім, я вирощую собак для перегонів і полювання, а розпещені кімнатні собачки мені не потрібні."
"— А мені здається, ви навмисне не пускаєте матір до її малят."
"Селена сама не розуміла, чому їй раптом стало шкода цього цуценя. Вона підійшла й узяла його на руки. Цуценя мокрим носом ткнулося їй у підборіддя."
"— Я не дозволю вам погубити цього малюка!"
"Нехемія, здивовано усміхаючись, сказала Селені:"
"— Принц правий. Своєрідні собаки не піддаються вихованню й потім стають важким тягарем."
"— Тягарем для кого?"
"— Ліліано, чесне слово, я не розумію, чому ви так розхвилювалися через цього цуценя. Поговоріть із будь-яким псарєм, і він вам скаже те саме. Щодня по всій Ерілеї убивають сотні й тисячі непридатних цуценят. І нікого це особливо не хвилює."
"— Я не знаю про інших. Не вбивайте цього! — майже закричала Селена. — Віддайте його мені, якщо це єдиний спосіб зберегти йому життя."
"Доріан уважно дивився на неї."
"— Добре, — погодився він. — Якщо вам так шкода цю похмуру істоту, я не стану його вбивати. Я поселю його на псарні, знайду куток. Я навіть покличу вас, щоб ви переконалися, що цуценя ціле й неушкоджене."
"— Ви це справді зробите?"
"— По правді кажучи, я б за цього пса й гроша ломаного не дав. Але якщо він вам так сподобався, він залишиться жити."
"Принц підійшов до неї майже впритул. У Селени спалахнули щоки."
"— Ви… ви обіцяєте? — запитала вона."
"Доріан приклав руку до серця й сказав:"
"— Клянуся своєю короною: це цуценя залишиться жити."
"Якби не присутність Нехемії, Селена б обняла його. Чи він би обняв її. Занадто близько один до одного вони стояли."
"— Дякую вам, Доріане."
"Нехемія з неприхованим інтересом стежила за цією розмовою й навіть не помітила, як до воріт підійшли її телохранителі."
"— Принцесо, вам пора, — сказав ейлуейською один із них. — Вам ще потрібно встигнути перевдягнутися для візиту до королеви."
"Нехемія підвелася й, намагаючись не зачепити розіграшних цуценят, пішла до воріт загона."
"— Ти підеш зі мною? — запитала вона Селену."
"Селена кивнула, повернулася до принца й запитала:"
"— А ви йдете з нами?"
"Доріан похитав головою й зачинив ворота. Цуценята тепер стрибали біля його ніг."
"— Можливо, ввечері я вас відвідаю, — сказав він."
"— Якщо вам пощастить, — тихо промовила Селена й пішла слідом за принцесою."
"Вона йшла коридорами, усміхаючись собі."
"— Він тобі подобається? — раптом запитала Нехемія."
"Селена насупила лоба й заперечила:"
"— Звідки ти взяла? Звичайно, ні."
"— Ви говорили так… невимушено. Мені здалося, вас щось… пов’язує."
"— Пов’язує? — ледь не поперхнулася Селена. — Придумаєш теж. Мені просто подобається його дражнити."
"— У цьому немає нічого ганебного, якщо він тобі подобається. Мушу зізнатися, спочатку я була про принца зовсім невисокої думки. Він здавався мені зарозумілим, самовпевненим ідіотом. А він зовсім не такий."
"— Не забувай: він — із династії Хавільярів."
"— У цій династії були різні королі. Доріан зовсім не схожий на свого батька."
"— Ми з ним просто дуріємо й не більше того."
"— А мені здається, ти йому дуже подобаєшся."
"Селена не думала, що невинні слова принцеси відгукнуться в ній хвилею пекучої люті."
"— Та я швидше вирву власне серце, ніж полюблю людину з династії Хавільярів! — відчеканила вона."
"Далі вони йшли мовчки. Селена змусила себе заспокоїтися. Прощаючись із Нехемією, вона побажала їй приємного вечора в королеви й пішла до себе."
"Вартові, що йшли за нею, трималися на пошанній відстані. З кожним днем ця відстань ставала все більшою. Може, це був наказ Шаола?"
"За вікнами наставали сутінки. Перш ніж почорніти, небо стало темно-синім, і його неяскраве світло красиво забарвлювало сніг, що налип на скла. А їй нічого не варто було б цим же вечором утекти з замка. У місті вона запаслася б усім необхідним і до ранку вже пливла б собі на кораблі, що йде на південь."
"Селена зупинилася біля вікна й притулилася до холодних стекол. Вартові теж зупинилися й мовчки чекали. Повітря, що сочився ззовні, приємно холодило лоб. Якщо вона втече, іщейки короля швидко збагнуть, де її шукати. У такий час можна втекти тільки на південь. Ось якби вона вирушила на північ, їм би й на думку не спало шукати її там. Але взимку на північ вирушають лише ті, хто шукає смерті."
"Вікно відбивало шматок коридору, і коли за спиною Селени щось майнуло, вона різко обернулася й побачила… Кейна."
"Цього разу він не скалив зуби й не ухмилявся. Лоб Кейна покривала іспарина. Він важко дихав, ніби риба, викинута на берег. Темні очі шалено блищали. Правою рукою Кейн стискав собі горло. Здавалося, він ось-ось себе задушить."
"‘Добре б’, — подумала Селена."
"— Щось сталося? — цілком дружнім тоном запитала вона."
"Кейн не відповів. Селені здалося, що він навіть не одразу помітив її, бо погляд його кілька секунд блукав і тільки потім зупинився на ній. Масивні пальці колишнього солдата ще щільніше стиснулися на власному горлі, ніби він боявся, що звідти вирвуться слова. На пальці похмуро блищало чорне кільце. Селені здалося, що за кілька днів м’язи Кейна ще виросли. Таке відчуття виникало в неї не вперше. Щоразу, коли вона стикалася з Кейном, він виглядав усе сильнішим."
"Видовище було настільки дивним, що Селена губилася в здогадках. Замість нахабного, самовпевненого й самонадіяного Кейна перед нею був наляканий велетень."
"— Кейне, що з тобою? — знову запитала вона."
"І раптом він обернувся й стрімголов кинувся коридором. Він біг із шаленою швидкістю, набагато швидше, ніж під час змагань. Кілька разів Кейн озирався на бігу, але дивився не на Селену й не на здивовано перешіптуваних вартових. Він дивився повз них, у глибину коридору."
"Селена дочекалася, коли стихне тупіт його ніг, а потім поспішила до себе. Там вона написала короткі записки Ноксу й Пелору, просячи їх увечері ніде не відлучатися зі своїх кімнат і нікому не відчиняти дверей. Причин настільки незвичайного прохання вона не вказала."
"Кальтена кілька разів ущипнула себе за щоки, надаючи їм рум’янцю. Перш ніж покинути будуар, вона наказала служницям побризкати її духами, а сама в цей час залпом проковтнула келих цукрової води. Кальтена не була любителькою солодкого й воду випила, щоб відбити запах опіуму, який вона курила, коли до неї несподівано завітав герцог Перангон."
"Головні болі почали мучити пані Ромпір ще в отроцтві. Батько запрошував до неї найкращих лікарів, але їхні зілля давали лише тимчасове полегшення, поки один старий лікар не порадив давнє засіб — куріння трубки, набитої слабкою сумішшю опіуму. Кальтена пам’ятала його попередження: курити, тільки коли напад стане нестерпним, і ні в якому разі не пробувати сильніші суміші. Але якщо в батьківському домі до цього ставилися з розумінням, при дворі таку особливість Кальтени могли б розцінити зовсім по-іншому. Тому хитра провінціалка ретельно приховувала від усіх не тільки свої напади мігрені, а й дивне ліки. І вже тим більше їй не хотілося, щоб про це дізнався Перангон."
"Перш ніж вийти до герцога, що розташувався в її покоях, Кальтена змусила служниць ретельно її обнюхати. Переконавшись, що духи й цукрова вода заглушили запах опіуму, вона пройшла з гардеробної до спальні й уже звідти, через коридорчик, до вітальні, де томився Перангон."
"Вигляд у герцога був, як завжди, войовничий, ніби з вітальні Кальтени він збирався вирушити на поле бою."
"— Добридень, ваша світлосте, — промуркотіла Кальтена, присівши в глибокому реверансі."
"Від мігрені й опіуму в неї крутилася голова, а в усьому тілі відчувалася противна важкість. Кальтена простягнула герцогові руку, і він не стільки поцілував її, скільки обслинив своїми товстими губами. Звичайно, погляд герцога ковзнув вище, і його очі заблищали відвертим бажанням. Кальтена усміхалася, прикидаючи, скільки їй ще вдасться стримувати напор Перангона."
"— Сподіваюся, я вас не потривожив, — сказав герцог, випускаючи її руку."
"У Кальтени раптом виникло ясне відчуття, що вона замкнена в пастці, в красивій клітці, наповненій шпалерами, м’якими меблями й подушками."
"— А я прилягла подрімати, від чого вашій світлості й довелося мене чекати, — зі звичною легкістю збрехала Кальтена."
"Перангон шумно вдихнув повітря, і вона завмерла. Невже герцог учує опіум?"
"— Значить, я вас потривожив? — запитав герцог, заучено усміхаючись."
"— Що ви, ваша світлосте. Я завжди рада вашим візитам. Особливо несподіваним. Обожнюю сюрпризи."
"— Вас не було на обіді. Ось я й зайшов проведати."
"Перангон склав руки на грудях. Кальтена раптом подумала, що кулак герцога міг би легко пробити їй череп."
"— По правді кажучи, мені нездоровиться, — сказала вона й сіла на кушетку."
"Вона б із радістю поклала голову на м’яку подушку, але в присутності герцога це виходило за рамки пристойності."
"Герцог щось говорив, але вуха Кальтени перестали сприймати звуки. Шкіра на обличчі Перангона набула скляного блиску, а його очі перетворилися на два моторошні чорні мармурові кулі. Даремно вона дозволила собі три зайві затяжки."
"— Вибачте, ваша світлосте. Мені справді погано."
"— Принести вам води? — запитав герцог і підвівся. — А може, я не вчасно?"
"— Ні! — ледь не закричала Кальтена, і в неї закалатало серце. — Я почуваюся достатньо добре, щоб насолоджуватися вашим товариством, але ви мусите пробачити мені деяку розсіяність."
"— Тільки не вам, пані Кальтено, говорити про розсіяність, — заперечив герцог і знову сів. — Мені рідко зустрічалися розумні жінки, але ви — розумніша за всіх, кого я знав. До речі, його високість такої ж думки. Він мені вчора говорив про це."
"Кальтена одразу випросталася, не звертаючи уваги на біль у спині. Перед нею майнуло обличчя Доріана й корона, що вінчала голову спадкового принца."
"— Принц це сказав? Про мене?"
"Герцог торкнувся її коліна й почав гладити його великим пальцем."
"— Принц сказав би більше, але тут його перебила пані Ліліана."
"У Кальтени закрутилася голова."
"— А чому вона була поруч із принцем?"
"— Не знаю. Я б теж волів, щоб її там не було."
"Ні, цього допускати не можна. Вона, Кальтена Ромпір, мусить припинити таке безобраздя. Ця дівчина виявилася занадто спритною. Але якщо Ліліана затягла спадкового принца в свої мерзенні сіті, Кальтена його звільнить. Перангон міг би їй у цьому допомогти. При його впливовості… Ліліана просто безслідно зникла б. Ось тільки одна обставина заважає. Ця Гордена — знатного походження, а Перангон береже свою честь і не дозволить собі так обійтися з людиною благородних кровей. Чи дозволить?"
"Кальтена прикривала очі, і перед нею в шаленій танці закружляли десятки скелетів. А якщо переконати герцога в тому, що Ліліана — хитра самозванка?.. Від цієї думки мігрень Кальтени спалахнула з новою силою, стиснувши горло."
"— Цілком із вами згодна, ваша світлосте, — сказала Кальтена, розтираючи пульсуючу скроню. — Навіть не віриться, що така недостойна особа, як пані Ліліана, завоювала серце спадкового принца."
"Кальтена раптом подумала: якби вона зараз була поруч із принцем, її мігрень миттєво б припинилася."
"— Мені здається, комусь обов’язково потрібно поговорити про це з його високістю, — сказала вона, запускаючи пробний шар."
"— Ви назвали її… недостойною особою?"
"— Я тут чула, що її походження… зовсім не таке вже й знатне, як вона стверджує."
"— Що саме ви чули? — насторожився Перангон."
"Кальтена теребила самоцвіт, що звисав із її браслета, і поспішно придумувала відповідь."
"— В подробиці мене не посвячували, але деякі придворні вважають її просто самозванкою, що зуміла закрутити голову принцу. Більше того, вона ні з ким при дворі не бажає знатися. Я б хотіла докладніше дізнатися про цю пані Ліліану. Думаю, і ви теж. Нарешті, це наш обов’язок як вірних підданих корони. Ми мусимо оберігати нашого принца від таких осіб."
"— Безперечно, — тихо погодився герцог."
"Кальтена почула душу роздираючий крик. Дикий. Невгамовний. Він пролунав у неї в голові, відгукнувшись нестерпним спалахом головного болю. Усі думки зникли, окрім однієї. Вона мусить зробити все необхідне, щоб врятувати корону й… своє майбутнє."
"Селена гортала черговий давній фоліант, де викладалися розпливчасті теорії походження «знаків долі». Несподівано двері до її вітальні прочинилися, викликавши жалісний скрип. У Селени завмерло серце, однак вона постаралася зберегти зовнішню незворушність. Негоже, щоб принц побачив свою захисницю, що струсила. Але на порозі стояв не Доріан і вже тим більше не чудовисько з залізними кігтями."
"На порозі стояла Нехемія в дивовижно красивій сукні, цілком розшитій золотом. Очі принцеси були спрямовані в підлогу, а по щоках текли чорні струмки фарби, якою вона підводила брови й повіки."
"— Нехеміє, що з тобою? — стривожилася Селена. — Це вистава так на тебе подіяла?"
"Плечі Нехемії злегка піднялися й тут же опустилися. Потім вона повільно підняла на Селену запалені, повні сліз очі."
"— Я… я не знала, куди ще мені йти, — ейлуейською прошепотіла вона."
"Селена була в повному замішанні."
"— Ти можеш сказати, що сталося?"
"Тільки зараз вона помітила в тремтячій руці принцеси шматок зім’ятого пергаменту."
"— Вони влаштували бійню, — прошепотіла Нехемія, хитаючи головою, ніби не хотіла вірити в те, що говорить."
"— Хто? — запитала Селена, холонучи всім тілом."
"Нехемія відповіла приглушеним риданням і тільки потім заговорила:"
"— Легіон адарланської армії захопив у полон п’ятсот ейлуейських повстанців. Вони ховалися на кордоні Задубленого лісу й Кам’яних боліт."
"Чорні сльози текли в Нехемії по щоках, залишаючи доріжки на її дивовижно красивій сукні. Довгі пальці принцеси продовжували м’яти пергамент. Ймовірно, це був лист, переданий їй невідомо ким."
"— Батько пише, що полонених гнали до Калакулли. По дорозі кілька людей спробували втекти й… — Нехемія важко дихала, з трудом виштовхуючи кожне слово. — І тоді адарланські солдати вбили всіх. Усіх, хто там був. Навіть дітей."
"Нудота підступила до горла Селени. П’ятсот полонених, забитих, як скот."
"Тільки зараз Селена помітила в дверях телохранителів принцеси. Їхні обличчя залишалися безстрасними, але їхні очі… Селена боялася зустрічатися з ними поглядом. Напевно, серед полонених були їхні друзі чи навіть родичі. І напевно комусь із убитих Нехемія допомагала, когось оберігала."
"— Яка ж я спадкова принцеса Ейлуе, якщо мені нічим допомогти моєму народові? — шепотіла Нехемія. — Чи можу я взагалі називатися принцесою, якщо таке відбувається?"
"— Як я тебе розумію, — у відповідь прошепотіла Селена."
"Ці слова зруйнували оцепеніння, що володіло Нехемією. Вона кинулася до Селени, уткнулася в плече й дала волю сльозам. Селена відчувала: будь-які слова зараз марні. Вона просто обіймала ридаючу принцесу, сама завмерши й відмовляючись вірити в те, що сталося."

#Епізод 18

"Селена сиділа біля вікна спальні й розсіяно стежила за танцем сніжинок у вечірніх сутінках. Нехемія давно вже повернулася до себе. Від Селени вона йшла, змивши всі чорні смужки на щоках і гордо розправивши плечі, як і належить принцесі. Годинник пробив одинадцяту. Селена підвелася, потягнулася й тут же завмерла від болю в животі. Намагаючись дихати рівно, вона нахилилася й зачекала, коли судоми послабшають. У неї почалося це більше години тому. Разом із болем накочував озноб. Тепло яскраво палаючого каміна сюди не доходило, і Селена закуталася в ковдру. Дякувати Фаліпі, яка подала їй чашку трав’яного чаю."
"— Ось, дівчинко, випий, — сказала служниця, ставлячи чашку на столик. — Це допоможе."
"Вона нахилилася до Селени, спершись на спинку крісла, й майже пошепки додала:"
"— Бідолахи вони, ці ейлуейські повстанці. Уявляю, як зараз принцесі."
"Разом із спазмами всередині Селени піднімалася лють."
"— Добре ще, що в неї є така подруга, як ти, — сказала Фаліпа."
"— Дякую."
"Селена за звичкою обхопила руками чашку й ледь не обпекла собі коліна."
"— А ручка в чашки на що? — усміхнулася Фаліпа. — Ось уже не думала, що асасини бувають такими незграбними. Якщо допомога знадобиться, клич мене. Сама свого часу намучилася з цими жіночими справами."
"Селена кивком подякувала їй. Фаліпа пішла. Селена встигла зробити кілька ковтків і знову скривилася від гризучого болю внизу живота."
"Ендов’єр, відібравши в неї майже все, звільнив її від малоприємної щомісячної жіночої особливості. Але тепер, через три з половиною місяці життя в нормальних умовах і ситної їжі, це повернулося. Селена ледь не плакала. Як у такому стані вона буде вправлятися? До завершального поєдинку — всього місяць."
"А сніжинки, байдужі до її страждань, спалахували в світлі, що лилося з вікна, й продовжували свій дивовижний танець, музика якого була недоступна людському вуху."
"Еліана закликає її знищити зло в замку. А що скаже давня королева щодо зла в інших частинах Ерілеї? Жертви там обчислюються сотнями. Цікаво, чи хтось рахував, скільки людей знайшли свій кінець у Калакуллі та Ендов’єрі?"
"Думки Селени перервав новий гість."
"— Я чув про Нехемію, — сказав увійшовший Шаол."
"— Капітане, чи не запізно для візиту? — запитала Селена, закутуючись у ковдру."
"— Ти що, захворіла?"
"— Так, нездужаю."
"— На тебе подіяло звістка про вбивство повстанців?"
"‘Невже він не здогадується?’"
"— Ні. — Вона скривилася від нової різі в животі. — Мені погано."
"— Тут і справді захворієш, — підхопив Шаол, дивлячись не на неї, а на підлогу. — Є від чого. А тому, хто власними очима бачив Ендов’єр…"
"Капітан провів рукою по обличчю, ніби позбавляючись спогадів про страшне місце."
"— Треба ж, п’ятсот людей."
"‘Невже й його пробило?’ — здивувалася Селена."
"Шаол став ходити туди-сюди."
"— Послухай, я знаю, що інколи буваю суворий з тобою. Ти навіть скаржилася на мене Доріану. Але… — Він зупинився, повернувшись до Селени. — Це добре, що ти подружилася з принцесою. Мені подобається твоя чесність і вірність вашій дружбі. Ходять чутки, ніби Нехемія потайки допомагала ейлуейським повстанцям… Якби хтось завоював мою країну, я б теж робив усе можливе, тільки б повернути свободу."
"Селена хотіла відповісти, але їй заважав біль у попереку, що додався до спазмів у животі."
"— Знаєш, — знову заговорив Шаол, стаючи біля вікна, — я був у багатьох речах неправий."
"‘Ну навіщо він припхався?’"
"Навколишній світ закрутився, ніби дитячий дзиґа, нахиляючись то в один, то в інший бік. Найгірше, якщо її зараз почне нудити. У минулому таке бувало."
"— Шаоле, — тільки й могла промовити Селена, бо через підступаючу нудоту їй довелося терміново затиснути рот рукою."
"— Я весь час думав: невже тобі не хотілося…"
"— Ша-о-оле, — застогнала Селена."
"Капітан різко обернувся до неї, і тут, не в силах стримуватися, Селена вивергла на підлогу всю вечерю."
"Шаол скривився й відскочив убік. Рот Селени наповнився їдкою гіркотою, а хлинули сльози обпекли очі. Новий спазм змусив її опуститися на коліна. Селену знову вирвало, цього разу жовчю."
"— Тож ти… справді захворіла? — злякався Шаол."
"Він гукнув служницю й довів Селену до стільця. У голові в неї почало прояснюватися. Здається, він про щось питав."
"— Тобі треба лягти в ліжко. Я донесу тебе на руках."
"— Та я… по-іншому хвора, — застогнала Селена."
"Шаол усадив її на постіль, відкинув покривало. З’явилася служниця похмуро покосилася на забруднену підлогу й відправилася по допомогу."
"— Як це… по-іншому? — не зрозумів Шаол."
"— У мене… загалом…"
"Обличчя Селени буквально запалилося, загрожуючи ось-ось розплистися по підлозі."
"‘Ну й тупиця!’"
"— У мене почалися жіночі справи!"
"Обличчя капітана теж стало яскраво-червоним. Він збентежено провів рукою по волоссю."
"— Якщо… тоді… тоді я краще піду, — заїкаючись, пробурмотів Шаол і незграбно вклонився."
"Він стрімко вийшов і ледь не спіткнувся, зачепивши за дверний одвірок. Видовище було настільки комічним, що Селена, перемагаючи біль, усміхнулася."
"Прийшли служниці й мовчки почали прибирати підлогу."
"— Ви мене пробачте, — винувато почала Селена, але жінки відмахнулися й продовжили займатися своєю справою."
"Селені не залишалося нічого іншого, як забратися під ковдру й мріяти про швидкий сон."
"Але сну не було. Селена ворочалася, шукаючи найкраще положення для свого сказеного живота. Двері знову відчинилися, і на порозі з’явився сміючись Доріан."
"— Мені трапився Шаол, тож я знаю про твоє… «цікаве становище». Здається, ти перелякала бідолаху сильніше, ніж усі роздерті трупи."
"Селена розплющила очі. Принц безцеремонно вмостився на її постіль."
"— Ваша високосте, мені справді дуже погано, і сьогодні я — нікудишня співрозмовниця."
"— Від цього ще жодна жінка не померла, — парирував її заперечення Доріан."
"Він витягнув із кишені новеньку колоду карт."
"— Чому б нам не пограти? Можемо прямо на ковдрі, — запропонував принц."
"— Я вам уже сказала: мені погано."
"— По твоєму обличчю щось непомітно."
"Принц дістав колоду з футляра й зі спритністю завзятого гравця перетасував карти."
"— Усього разок. Не впертися."
"— Хіба в замку мало охочих вас розважити?"
"Очі Доріана спалахнули. Колоду він перегнув навпіл."
"— Тобі мало б лестити моє товариство."
"— Я буду дуже польщена, якщо ви підете."
"— А тобі не здається, що дивно розраховувати на мою прихильність і при цьому поводитися так зухвало?"
"— Зухвало? Я ледь почала."
"Живіт знову схопило, і Селена підтягнула коліна до грудей."
"Принц засміявся й прибрав колоду назад у кишеню."
"— До речі, якщо тобі цікаво: врятований тобою цуценя передавав привіт."
"— Ідіть геть, — застогнала Селена."
"— Я не дозволю прекрасній дівчині померти на самоті, — сказав Доріан, кладучи свою руку поверх її долоні. — Хочеш, я тобі щось почитаю, щоб скрасити останні миттєвості? Яку книгу?"
"Селена сховала руки під ковдру й прошипіла:"
"— Як щодо роману про дурного принца, який, не маючи ні краплі співчуття, мучив своїми розмовами нещасну дівчину-асасина?"
"— Чудова історія! Мені вона вже подобається, бо в неї щасливий кінець. Ця дівчина була зовсім не нещасною, а хитрою. Вона тільки вдавала, що хвора, щоб привернути увагу принца. Хто б міг подумати? Ця панянка вигадала спритний хід. А далі йде приголомшлива сцена в спальні. Там буде стільки дотепності."
"— Досить! Замовкніть! Ідіть в інші спальні, а мене залиште в спокої!"
"Схопивши книгу, Селена кинула її в принца. На щастя, Доріан встиг упіймати книгу раніше, ніж та зіткнулася з його носом."
"— Пробачте! — забормотіла перелякана Селена. — Я не подумала, що книга важка. Чесне слово, ваша високосте, я не хотіла завдати вам каліцтва."
"— Охоче вірю. Найкращий асасин Адарлана навряд чи стала б убивати мене настільки грубим способом. Думаю, це був би удар кинджалом чи ножем і бажано не в спину."
"Селена схопилася за живіт і навіть зігнулася від болю. У такі моменти вона завжди жалкувала, що не народилася чоловіком."
"— Перестань називати мене «ваша високосте». Я для тебе просто Доріан."
"— Добре."
"— Скажи це."
"— Що сказати?"
"— Те, що вже сказала, і назви мене на ім’я: «Добре, Доріане»."
"Селена витріщила очі: від болю й від його дурниць."
"— Якщо це приємно для вух вашої благородної святості, я буду називати вас тільки на ім’я, — сказала вона."
"— Благородна святість? Чудово. Мені це подобається."
"Доріан усміхнувся, подумавши, що так називається роман, який ледь не зіткнувся з його носом."
"— Щось не пригадаю, щоб я посилав тобі цю книгу. Та в мене й немає таких книжечок!"
"Селена ледь чутно засміялася й відпила кілька ковтків цілющого відвару, принесеного служницею."
"— Де ж, Доріане, таким книгам бути у вашій бібліотеці? Цей роман мені позичила одна зі служниць, яка любить читати."
"— «Страсті на заході», — прочитав він назву роману, після чого, навмання розкривши книгу, почав читати вголос: — «Його пальці ніжно пестили її молочно-кремову гр…»"
"У принца округлилися очі."
"— Чорт тебе побери, Селено! Ти справді читаєш цю маячню? Ніяк «Символи й сила» набридли? І трактат з ейлуейської культури — теж?"
"Селена допила імбирний чай. Фаліпа виявилася права: животу стало легше."
"— У мене, Доріане, коло читання ширше за ваше. А цей роман вам теж не завадило б прочитати. До речі, можу позичити, коли дочитаю. У автора чудовий стиль. І ще, — сором’язливо усміхнувшись, додала вона, — ви почерпнете там немало корисного щодо поводження з вашими подружками."
"— Я не читатиму таке, — процідив принц крізь зуби."
"Селена забрала в нього роман і відкинулася на подушку."
"— У такому разі ви уподібнюєтеся Шаолу."
"— Шаолу? — перепитав Доріан, не здогадуючись про пастку. — Ти й йому пропонувала читати цю маячню?"
"— Пропонувала, але він відмовився, — збрехала Селена. — Сказав, що капітану королівської гвардії не личить читати подібні книги."
"Принц вихопив у неї роман."
"— Ах ти, демон у жіночому подобі! Давай сюди цю писанину! Я не дозволю тобі протиставляти нас одне одному."
"Доріан знову покосився на книгу й перевернув її, сховавши обкладинку з назвою."
"Селена усміхнулася й стала дивитися на падаючий сніг. У спальні помітно похолодало, і вогонь у каміні не рятував від протягів, що проривалися через щілини в балконних дверях. Селена відчувала: Доріан спостерігає за нею. Але без настороженості, яку вона інколи помічала в погляді Шаола. Доріан спостерігав за нею, бо йому це подобалося."
"Неохоче вона зізналася собі, що їй теж подобається спостерігати за ним."
"— На що це ви так зачаровано дивитеся?"
"Запитання Селени вибило принца з незрозумілого стану, який справді був схожий на зачарованість."
"— На тебе. Ти гарна, — вирвалося в нього."
"— Не кажіть дурниць."
"— Я що, образив тебе?"
"Від приливу крові в нього застукало у скронях."
"— Ні, — коротко відповіла Селена й знову повернулася до вікна."
"Доріан бачив, як швидко червоніє її обличчя. Він не звик до довгих залицянь. Його стосунки швидко закінчувалися постіллю. Виняток, мабуть, становила Кальтена, яку він не мріяв побачити в постелі поруч із собою. А ось Селена манила його. Доріану хотілося цілувати її, гладити ніжну шкіру й стежити, як її тіло відгукується на його ласки."
"Тиждень, що передував Ільмасу, був часом відпочинку, часом тілесних насолод, які допомагають людям зігрітися довгими зимовими ночами. Жінки розпускали волосся, а деякі навіть відмовлялися від корсетів. Це був бенкет, на якому не існувало заборонених плодів, і кожен міг ласувати стільки, скільки дозволяли сили. Звичайно, принц щороку з нетерпінням чекав заповітної пори. Але зараз…"
"Зараз сама думка про свято здавалася йому кощунною. Яке тут веселощі, коли королівські солдати — солдати його батька — убили п’ятсот ейлуейських повстанців? Усіх, навіть дітей. П’ятсот загублених життів. Як тепер він дивитиметься в очі Нехемії? І як надалі він правитиме країною, де солдатів натаскують, наче бійцівських собак, що не знають співчуття?"
"У Доріана пересохло в роті. А адже Селена родом із Террасена — першої держави, завойованої його батьком. Це диво, що вона вціліла й якимось чином звикла до життя під адарланським пануванням. Чи затаїлася? Три шрами на її спині — вічне нагадування про жорстокість адарланського короля, хоча й не він хльостав її батогом в Ендов’єрі."
"— Вас щось турбує? — запитала Селена."
"Запитання було поставлене з обережною цікавістю, ніби її справді цікавили його думки. Не в силах дивитися на неї, принц відійшов до вікна. Скло було зовсім холодним, а за ним безупинно падав сніг."
"— Ти мусиш мене ненавидіти, — майже пошепки промовив Доріан. — Мене й мій двір. Вони розважаються, фліртують і не бажають знати про те, що відбувається за стінами замка й за межами Рафтхола… Коли мене повідомили, що королівська армія винищила п’ятсот полонених ейлуейських повстанців, я… Я не знав, куди сховатися від сорому."
"Він чув, що Селена підвелася й перебралася в крісло. Що їй його зізнання? Але слова рвалися з нього, і йому було не зупинитися."
"— Тепер я розумію, чому ти так легко вбивала адарланців. І я анітрохи не виню тебе за це."
"— Доріне, не зараз."
"Ні, саме зараз, бо тільки в тиші сплячого замка він міг висловити те, про що не наважувався говорити вдень."
"— Бувають природжені вбивці, але таких небагато. А з тобою… з тобою сталося щось жахливе, коли ти була ще зовсім маленькою. І швидше за все, у цьому винен мій батько. Ти маєш повне право ненавидіти Адарлан і адарланців. Наші вчені прихвостні запевняють, що сама Богиня повеліла Адарлану поширити свою владу на всі інші держави. І на Террасен, і на Ейлуе."
"Доріан уткнувся лобом у скло. Очі щипало, хоча тяга в каміні була справною."
"— Ти мені не повіриш, але я… не хочу бути частиною всього цього, — продовжив принц. — Я не можу називати себе чоловіком, якщо дозволяю батькові творити все нові й нові звірства. Але навіть якби я валявся в нього в ногах, благаючи про поблажливість до завойованих королівств, він і слухати б не став. Він вважає такий порядок речей правильним і навіть ідеальним. Я й тебе обрав своєю претенденткою лише тому, що знав: мій вибір розсердить батька."
"Селена скривилася від його слів і відновлених болів у животі, але Доріан хотів висловитися до кінця."
"— Якби я взагалі відмовився шукати собі претендентів, батько вважав би це бунтом проти нього, а я ще не настільки сильний, щоб відкрито йому протистояти. І тому я обрав тебе — найкращого асасина Адарлана. Іншого вибору в мене й бути не могло."
"Ось він і сказав це, і вона чула ці слова. Як вона їх сприйме — невідомо. Головне, він виплеснув те, що давно носив у собі."
"Доріан повернувся до Селени, їхні очі зустрілися."
"— Життя не повинно бути таким, — сказав він. — І… світ теж не повинен бути таким, як зараз."
"Селена заговорила не одразу. Деякий час вона прислухалася до биття власного серця."
"— Я не відчуваю ненависті до вас, — тихо, майже пошепки, промовила вона."
"Доріан опустився на сусідній стілець і обхопив голову руками. Вигляд у нього був зовсім самотній."
"— Ви не такий, як вони. І… пробачте, якщо я вас чимось образила. Я ж над вами весь час жартувала."
"— Ти мене… образила? Звідки ти взяла? Ти… ти зробила життя в замку трішки веселішим."
"— Усього лише трішки? — вскинула голову Селена."
"— Ну, на дві трішки, — усміхнувся принц, витягаючи ноги. — З одного боку, шкода, що ти не зможеш піти зі мною на святковий бал. Але з іншого — це й на краще. Бал у ніч Ільмаса…"
"— А чому я не можу піти? І чим цей бал відрізняється від інших?"
"— На Ільмас влаштовують не просто бал, а бал-маскарад. Ось, мабуть, і всі відмінності. Думаю, тобі не треба пояснювати, чому ти не можеш піти."
"— Вам із Шаолом подобається позбавляти мене розваг. Коли я в клітці, це спокійніше, вірно? А я люблю розваги."
"— Коли станеш королівською захисницею, можеш ходити на всі бали підряд."
"Селена скривилася, цього разу не від болю, а від досади. Доріан дивився на неї, не знаючи, що робити. Переконувати її, як він був би радий з’явитися з нею на балу? Що він дорожить цими рідкісними зустрічами з нею? Що думає про неї постійно? Швидше за все, Селена висміяла б його за ці зізнання."
"Годинник пробив північ."
"— Мабуть, мені пора, — сказав принц і потягнувся. — Завтра майже весь день доведеться стирчати з радниками. Герцогу Перангону навряд чи сподобається, якщо я буду клювати носом."
"— Передайте герцогу мої найкращі побажання, — їдко усміхнувшись, попросила Селена."
"Вона не забула, як герцог обійшовся з нею в Ендов’єрі, у день їхньої першої зустрічі. Доріан цього теж не забув, і зараз спогади наповнили його холодною люттю."
"Він раптом нахилився й поцілував Селену в щоку. Відчувши доторк його губ, Селена стиснулася, і хоча поцілунок був коротким, принц встиг вдихнути аромат її шкіри. Доріан ледь утримався, щоб не поцілувати її знову."
"— Спокійних тобі снів, Селено."
"— І вам спокійної ночі, Доріане."
"По дорозі до себе принц розмірковував, чому Селена так засмутилася й чому промовила його ім’я не з ніжністю, а з якоюсь відстороненою покірністю."
"Селена не могла заснути. Вона дивилася на широку смугу місячного світла, розлитого по підлозі. Бал-маскарад у ніч Ільмаса! І нехай адарланський двір вважався найбрехливим і помпезним у всій Ерілеї, від самого слова «бал-маскарад» віяло чимось романтичним. І знову, як і в ніч Самуїнна, вхід до бальної зали їй буде закритий. Селена протяжно зітхнула й поправила подушку. А може, Шаол хотів потайки запросити її на бал? Може, він про це почав говорити, коли її вивернуло?"
"Селена похитала головою. Розмріялася! Дочекаєшся від капітана такого запрошення! І потім, у них із Шаолом є справи поважніші. Наприклад, шукати того, хто вбиває претендентів. Селена пошкодувала, що нічого не сказала капітанові про дивну поведінку Кейна."
"Вона заплющила очі й усміхнулася, уявляючи собі святковий подарунок на Ільмас. Найкращим подарунком був би труп Кейна, знайдений… та хоч завтра вранці."
"Перша година ночі. Друга година. Третя. Час ішов, а сон так і не з’являвся. Селена лежала й думала. Про невідоме зло, що ховається в затишному кутку величезного замка. Про п’ять сотень убитих ейлуейських полонених, тіла яких напевно вже покидали в кілька великих спільних ям і засипали. Скільки ще таких ям з’явиться по всій Ерілеї стараннями його величності короля Адарланського?"
"Наступного дня, ближче до вечора, Шаол Естфол стояв у коридорі другого поверху й дивився в простір внутрішнього двору. Там, між припорошеними снігом живими огорожами, повільно брели двоє. Селену було легко впізнати по її білому плащу, а Доріана він і так би помітив де завгодно."
"Обов’язок вимагав від Шаола йти слідом за гуляючими, уважно спостерігаючи й роблячи все, щоб Селена раптом не захопила принца в заручники й не перетворила його на живий щит для своєї втечі. Проста логіка й роки досвіду, набутого на гвардійській службі, вимагали: «Негайно спустися вниз! Шестеро вартових недостатньо». При хитрості й кмітливості Селени що їй ці шестеро!"
"Але Шаол нерухомо стояв біля вікна. Він не міг змусити себе зробити ні кроку."
"Щодня він відчував, як руйнуються бар’єри. Він сам дозволяв їм руйнуватися. Чому? Бо йому подобався її щирий сміх, подобалося, що одного разу, прийшовши до неї, він застав її заснулою в обіймах із книгою. І головне, Шаол знав: вона виграє заключний поєдинок."
"Так, Селена Сардотін була злочинницею. Геніяльною вбивцею, королевою «дна»… і водночас — ще зовсім дівчинкою, яку сімнадцятирічною кинули в Ендов’єр."
"Від цієї думки Шаолу ставало погано. У свої сімнадцять він знемагав від муштри Брулло, але після виснажливих занять його чекав чан із гарячою водою, ситна їжа й дружня компанія. Доріан тоді втратив голову від своєї Рузанди й взагалі забув про все на світі."
"А Селена в свої сімнадцять опинилася в соляних копальнях Ендов’єра. На каторзі, звідки не повертаються. І вижила."
"Шаол сумнівався, чи вижив би він в Ендов’єрі, особливо взимку. Його ніколи не били батогом, у нього на очах ніхто не вмирав. Він не знав, що таке холод і голод."
"Селена засміялася. Напевно, якійсь жарті Доріана. Вона пережила Ендов’єр і не розучилася сміятися."
"Шаола лякало, що Селена перебуває поруч із Доріаном. При її навичках їй нічого б не коштувало задушити принца чи зламати йому шию. Але капітана ще сильніше лякало його власне довіра до цієї дівчини. Чим усе це може закінчитися для нього — Шаол теж не знав."
"Вони йшли між побілених снігом кущів живої огорожі. З обличчя Селени не сходила усмішка. Розчищена доріжка була досить вузькою, і це змушувало її йти майже поруч із Доріаном, однак не настільки близько, щоб його торкатися. Вона ледь встигла поїсти, як він з’явився в її їдальні й покликав на прогулянку. Судячи зі швидкості появи (служниця тільки почала прибирати зі столу), принц прийшов раніше й чекав у коридорі."
"Звичайно, якби сьогодні було тепліше, Селена нізащо б не дозволила взяти себе за руки й зігрівати їй долоні. Білий, обшитий хутром плащ лише з виду здавався теплим, а насправді анітрохи не рятував від холодних поривів вітру. Цікаво, як переносить мороз Нехемія? Цього Селена не знала. Після звістки про страту ейлуейських полонених принцеса майже весь час проводила в себе й на всі пропозиції погуляти відповідала відмовою."
"Від часу останнього нічного візиту Еліани минуло понад три тижні. З тих пір Селена встигла пройти цілих три випробування, найцікавішим із яких виявилося подолання перешкод. Воно було далеко не легким, але Селена відділилася кількома подряпинами й саднами. На жаль, Пелор у цьому випробуванні виявився найгіршим і був відправлений «додому». Селена уявляла, як йому буде повертатися в «рідні краї». Але головне — він залишився живим. А ось ще троє претендентів знайшли свою смерть у покинутих коридорах замка. Їхні тіла були роздерті до невпізнання. Тепер, ледь тільки починало темніти, Селена замикалася в себе. Тривога її зросла настільки, що вона схоплювалася від будь-якого дивного скрипу й шереху."
"У неї залишилося п’ятеро суперників: Кейн, Могила, Нокс, колишній солдат, чиє ім’я вона ніяк не могла запам’ятати, і Ренальт — підлий найманець, який став правою рукою Кейна, замінивши вбитого Веріна. Нічого дивного, що до нього перейшла й «традиція» глузувати з Селени."
"Але зараз, ідучи повз змовклий фонтан, їй не хотілося згадувати ні про вбитих претендентів, ні про колкості Ренальта. Краєчком ока Селена помічала, з яким захватом Доріан дивиться на неї. Ну й нехай дивиться! Звичайно, вона зовсім не думала про принца, наряжаючись у гарну сукню лавандового кольору. І коли служниця укладала їй волосся, не було жодної думки про нього. А ці білосніжні рукавички вона обрала тільки тому, що вони здалися їй теплішими за інші."
"— Куди б нам ще сходити? — запитав Доріан. — Ми двічі обійшли весь сад."
"— А хіба в принца немає важливих державних справ? — глузливо запитала Селена."
"Порив крижаного вітру проник їй під капюшон. Щоб не заморозити вуха, Селена натягнула капюшон поглибше й тут помітила, що Доріан уважно дивиться на її шию."
"— Що так зацікавило вашу високість?"
"— Ти завжди носиш це намисто. Що, ще один подарунок? — запитав принц і покосився на кільце, подароване їй Шаолом."
"Очі в нього більше не сяяли. Селена прикрила рукою амулет."
"— Ні, Доріане, усе набагато простіше. Я знайшла його в шкатулці для коштовностей, — збрехала Селена. — Спочатку надягати не наважувалася. А потім, коли моя шия перестала нагадувати жердь, надягла. Гарна штучка, правда?"
"— І дуже стара. Невже ти не поцупила родинні коштовності якоїсь придворної дами?"
"Усе це було сказано жартівливим тоном, але вже без колишньої теплоти."
"— Ні, Доріане, — досить різко відповіла вона. — Крадіжкою коштовностей у нас, якщо не забули, промишляє пані Ліліана. У мене інше ремесло."
"Селена не вірила, що амулет Еліани здатен захистити від убивці. Вона досі сердилася на королеву за ухильні відповіді, але намиста не знімала. Невідомо чому, цей амулет додавав їй спокою в довгі нічні години, коли вона без сну сиділа на постелі й дивилася на двері спальні."
"А принц так і не відривав очей від її шиї. Селена опустила затерплу руку."
"‘Нехай витріщається’, — вирішила вона."
"— У дитинстві я любив читати легенди про виникнення Адарланського королівства. Моїм героєм був Гавін. Напевно, я перечитав усе, що зміг знайти, про його битви з Ераваном."
"‘Невже він розумніший, ніж я думала? Невже він одразу здогадався? Ні, цього бути не може. Мало хто він там читав у дитинстві!’"
"— І при чому тут ця простенька прикраса? — запитала Селена, з усіх сил роблячи вигляд, що їй цікаво, але не більше того."
"— Та при тому, що в Еліани — першої королеви Адарлана — був магічний амулет. Гавін і Еліана разом билися проти Повелителя темряви, але ніяк не могли його здолати. Втім, Еліана тоді ще була тільки принцесою. І ось, коли Ераван уже збирався вбити Еліану, до неї явився якийсь дух чи привид і вручив амулет. Після цього всі чари Еравана втратили над нею силу. Еліана побачила, хто він є насправді, і назвала його справжнім ім’ям. Повелителя темряви це настільки здивувало, що на деякий час він забув про другого свого супротивника. Ось тоді Гавін його й убив."
"Тепер Доріан дивився на сніг під ногами."
"— Той амулет назвали «Оком Еліани», — додав принц. — Потім він зник, і, швидше за все, безповоротно."
"Як дивно було все це чути від Доріана — сина короля-злодія, що замислив винищити магію під корінь. Але Селена продовжувала розігрувати з себе цікаву дурочку."
"— І ви думаєте, ця дрібничка — «Око Еліани»? — хихикаючи, запитала вона. — Це ж скільки століть минуло! Якщо амулет і існував, він давно розсипався в порох."
"— Думаю, що не розсипався, — заперечив Доріан, розтираючи замерзлі долоні. — Я бачив картинки з його зображенням. Напевно, твоє намисто — просто копія."
"— Звичайно копія, — підхопила Селена й тут же змінила тему: — А ваш брат коли приїде? Ви говорили, він дуже просився на свята додому."
"— Доля мені посміхнулася, — відповів Доріан, піднімаючи очі до сірого неба. — Вранці гонець привіз листа. Гірські перевали тонуть у снігу. Він сам ледь пробрався. А Холлін у нас не звик їздити верхи. Тож братику доведеться сидіти в горах до весни. Уявляю, як дістанеться й учителям, і слугам."
"— А я уявляю, як це засмутить вашу матір, — усміхнулася Селена."
"— Погорює, а потім відправить туди слуг, навантажених подарунками. Треба ж ублажити «малюка»!"
"Селена слухала Доріана напіввуха, підтримуючи видимість розмови. Вони робили третє коло по саду. Усі думки Селени були зайняті легендою про амулет Еліани. Невже давня королева не розуміла, що хтось та впізнає її амулет? Але якщо це справді «Око Еліани», а не майстерна копія… Якщо король дізнається, він уб’є нахабку на місці: і за те, що знайшла потайний хід у заборонений склеп, і за те, що наважилася надягти амулет, що володіє магічною силою."
"І про що тільки думала Еліана, вручаючи їй намисто?"
"Селена відірвалася від книги й у черговий раз зупинила погляд на шпалері. Ніби жодних змін. Комод стояв на місці, загороджуючи вхід до виявленого коридору. Просто через усіх цих трупів їй мариться невідомо що. Селена струснула головою й повернулася до читання. Очі бігали по рядках, але сенс прочитаного вислизав."
"Чого домагається від неї Еліана? Померлі королеви не приходять у світ живих і не віддають накази. Селена грюкнула книгою. Ні, вона й не збиралася підкорятися наказам Еліани. Ще по дорозі в Рафтхол вона знала, чому мусить виграти змагання. Це єдиний спосіб повернути собі свободу. Однак зло, про яке говорила Еліана, не просто ховалося в темному кутку. Воно вбивало, і чомусь — тільки претендентів. Тут мимоволі почнеш ламати собі голову над тим, де ж гніздиться це зло."
"Скрип дверей застав Селену зненацька. Книга випала з рук. Селена схопила важкий мідний підсвічник, готова вскочити з постелі й атакувати непроханого гостя. Але пролунав знайомий голос. Це була Фаліпа. Накриваючи собі під ніс, жінка пройшла коридором і сховалася в кімнаті для слуг. Селена досадливо скривилася, лаючи себе за боягузтво. Тепер треба вилазити з теплої постелі за впалою книгою."
"Як на зло, книга залетіла під ліжко. Лаючись, Селена опустилася на коліна. Мармурова підлога здавалася шматком льоду. Селена шарпала рукою, безуспішно намагаючись намацати втеклу книгу. Довелося поставити підсвічник на підлогу. По гладких плитах книгу занесло до самої стіни. Селена потягнулася туди й раптом побачила білу смугу, що в’ється по підлозі саме під ліжком."
"Селена схопила книгу й поспішно підвелася з колін. У неї тремтіли руки. Перемагаючи тремтіння, вона вперлася в край ліжка й натиснула плечем. Громіздке ліжко рухалося ледь-ледь. Окоченілі ступні Селени ковзали по мармуровій підлозі, будучи поганою опорою. Нарешті їй вдалося відсунути ліжко на достатню відстань."
"У Селени окоченіли не тільки ступні, а й усе тіло."
"«Знаки долі»!"
"Їх були десятки, намальовані крейдою на підлозі. Вони звивалися у велику спіраль, і в її центрі білів великий, ретельно виведений знак. Селена відступила назад і вдарилася об край комода."
"Звідки це в її спальні? Хто пробрався сюди, минаючи вартових, і намалював цю зловісну спіраль? Селена тремтячою рукою схопила себе за волосся. У центрі спіралі був той самий знак, який вона бачила біля тіла Веріна."
"Їй здавалося, що хтось стискає їй кишки, зав’язуючи їх у тугий вузол. Ну не можна ж так просто стояти й дивитися на розмальовану крейдою підлогу. Оцепеніння змінилося рішучістю. Селена підбігла до столика з глечиком і виплеснула всю воду на підлогу. Потім принесла з умивальної ще води. Коли крейда трохи розм’якшилася, Селена схопила рушник і почала лихоманково відтирати підлогу. Вона шкрябала мармур, доки в неї не заболіла спина й не заніміли озяблі руки й ноги."
"Повертати ліжко на місце вона не стала. Нашвидкуруч одягнувшись, Селена вибігла в коридор."
"На щастя, вартові не стали заперечувати, коли вона попросила провести її до бібліотеки. Прийшовши туди, вартові вмостилися біля вхідних дверей великої зали, а Селена попрямувала далі — в пилову, запліснявілу нішу верхнього ярусу. Усі книги, так чи інакше пов’язані зі «знаками долі», були звідти. На цю нішу Селена натрапила випадково, хоча, як говорила Еліана, випадковостей не існує. Селена з труднощами переставляла ноги й постійно озиралася по сторонах."
"Що означала спіраль під її ліжком? Що наступна жертва — це вона, Селена Сардотін?"
"До ніші й знайомих полиць було рукою подати. Завернувши за ріг, Селена зупинилася як укопана. За столиком, де горіла одна свічка, сиділа Нехемія й широко розплющеними очима дивилася прямо на Селену."
"— Слухай, ну ти мене й налякала, — видихнула Селена."
"Серце в неї калатало так, що, напевно, навіть вартовим було чутно."
"Нехемія відповіла їй стриманою усмішкою. Селена підійшла ближче."
"— Що привело тебе до бібліотеки в першій годині ночі? — своєю рідною мовою запитала принцеса."
"— Не спалося. Чим ворочатися в ліжку, вирішила піти сюди, — збрехала Селена."
"Її погляд упав на книгу, яку читала принцеса. Книга й близько не нагадувала ті, за якими вони займалися. Це був товстий рукописний фоліант. На відміну від інших старовинних книг рядки в цій були досить дрібними й щільними."
"— А ти що читаєш? — запитала Селена."
"— Та так, нічого особливого, — відповіла Нехемія."
"Принцеса грюкнула книгою й підвелася."
"Селена здивувалася надменності її тону й насмішкувато-презирливому виразу обличчя."
"— Я думала, ти не настільки знаєш адарланську, щоб читати такі важкі книги."
"Нехемія підхопила книгу зі столу, запхавши собі під пахву."
"— У такому разі, Ліліано, ти нічим не відрізняєшся від усіх інших невігласних дурнів і дур цього замка, — бездоганною адарланською відповіла їй Нехемія."
"Раніше ніж Селена встигла розкрити рота, принцеса пішла геть."
"Селена отупіло дивилася їй услід. Усе це нагадувало безглуздий, безглуздий сон. Ну не може Нехемія читати важкі для розуміння книги, та ще й старому діалекті адарланської. Вона й прості-то читала з безліччю помилок у вимові."
"Позаду столу, на підлозі, валявся зім’ятий шматок пергаменту. Селена підняла його й розгорнула. Пергамент був усипаний «знаками долі». Селена майже бігом кинулася до виходу з бібліотеки. Пергамент вона сунула в кишеню й відчувала, як «знаки долі» обпікають їй тіло."
"Збігши внутрішніми сходами, Селена опинилася в темряві великої зали. Тут було тихо й спокійно, як і має бути в бібліотеці. Особливо вночі."
"Невже весь цей час Нехемія вела з нею підступну гру? Але навіщо? Селена відмовлялася в це вірити. Навіщо принцесі день у день удавати, ніби вона погано знає адарланську? Нехемія не могла виявитися майстерною брехункою… Чи могла?"
"Селена раптом згадала: а адже не хто інший, як Нехемія, розповіла їй, що дивні малюнки на садових плитах — це «знаки долі». Виходить, принцеса все відмінно знала. Більше того, вона без кінця перестерігала Селену, щоб та трималася від них подалі. Так і мусить поводитися справжній друг."
"Потім Селені згадався вечір, коли Нехемія ридала в неї на грудях, дізнавшись про страту п’ятсот співвітчизників. Принцеса тоді прийшла до неї, як до єдиної своєї подруги: самотня, розчавлена горем."
"Але не можна забувати, що Нехемія приїхала сюди із завойованої країни. Адарланський король зірвав корону з голови її батька, позбавивши його титулу. Нехемія знала про всі звірства й жахи, чинимі адарланцями на її батьківщині. Селена про них теж знала, від ейлуейських каторжників. Там вона вперше почула й про те, як ейлуейців продають у рабство, і про принцесу Нехемію, що потайки допомагає повстанцям."
"Вартові біля дверей бібліотеки ліниво йорзали в кріслах, борючись із дрімотою. Селена пішла до них, продовжуючи обмірковувати те, що сталося."
"У Нехемії були всі підстави ненавидіти Адарлан, адарланського короля й самих адарланців. Дізнавшись про змагання, принцеса стала робити все можливе, щоб їх зірвати й нагнати страху на мешканців замка. І найзручнішими жертвами були, звичайно ж, претенденти. Ну хто вони? Злочинці, лиходії. Хто стане сумувати про їхню загибель? Зате по замку розповзе страх."
"Але невже Нехемія збиралася погубити й її?"

#Епізод 19

"Йшли дні. Селена по-старому не бачилася з Нехемією. Ні Доріану, ні Шаолу вона не наважувалася розповісти про «знаки долі», виявлені в себе під ліжком, і про раптову зустріч із принцесою в бібліотеці. Вона могла підозрювати Нехемію, будувати всілякі здогадки, однак доказів у неї не було. Будь-який докір на адресу принцеси тільки б усе зіпсував."
"Вільний час Селена витрачала на спроби розібратися в сенсі «знаків долі», дізнатися, яким чином вони пов’язані з убивцею та його чотириногим чудовиськом. Чергове випробування промайнуло малопомітною подією. Найгірше показав себе солдат, чиє ім’я Селена постійно забувала. Тепер йому належало повернутися до в’язниці. Селена по-старому вправлялася з Шаолом і Ноксом. Через три дні п’ятірку залишених претендентів чекало останнє випробування, а ще через пару днів — попередні поєдинки й потім… завершальний."
"Настав Ільмас. Вранці Селена прокинулася й лежала, насолоджуючись тишею."
"Вона давно не відчувала такого спокою. Навіть неясність стосунків із Нехемією тимчасово відступила. Мороз розмалював віконні шибки, за якими падав і падав сніг. Якби не тріск поліна в каміні, напевно можна було б почути звук падаючих сніжинок. Селені не хотілося порушувати умиротворення святкового ранку думками про Нехемію, поєдинки й вечірній бал, куди її не запросили. У цей ранок, ранок Ільмаса, вона мала право бути щасливою."
"Ільмас вважався подвійним святом. Він був кануном, коли з темряви народжувалося весняне світло. Він був днем народження первістка Богині. Але для багатьох Ільмас служив приводом виявити трохи більше уваги до близьких, сусідів і незнайомців, що зустрілися на вулиці. У цей день люди дуже охоче подавали жебракам і згадували, що любов усе ще існує."
"Селена перевернулася на інший бік… і раптом її щока вперлася в щось жорстке, з смачним запахом…"
"— Солодощі! — як маленька, сплеснула руками Селена."
"Поруч із нею, біля подушки, стояв великий полотняний мішок, наповнений усілякими солодощами. Однак ні записки, ні якихось написів на самому мішку не було. Знизавши плечима, сяюча Селена зачерпнула з мішка жменю цукерок. Як вона їх обожнювала!"
"Сміючись від радості, Селена набила собі рот. Одні цукерки треба було смоктати, інші — жувати, а треті самі танули в роті. Селена перепробувала всі сорти, які були в мішку. До того моменту, коли шлунок наситився солодким, її щелепи боліли від старанного жування. Селена перевернула мішок і висипала рештки його вмісту на ковдру, анітрохи не збентежившись, що разом із цукерками звідти висипалася купка цукрової пудри."
"Тут було все, що вона любила: шоколадні цукерки з желейною начинкою, мигдаль у шоколаді, журавлина в цукрі, твердий фруктовий цукор, огранований, наче коштовне каміння. Вафлі прості й шоколадні, цукрова вата, цукерки з лакричним коренем і, звичайно ж, маленькі плиточки чистого шоколаду. А як спокусливо виглядали трюфелі з лісовими горіхами! Не втримавшись, Селена схопила найближчий до неї трюфель."
"— Хтось дуже добрий до мене, — жуючи горіхи, сказала вона."
"Потім вона знову уважно оглянула мішок. Хто ж послав їй такий розкішний подарунок? Швидше за все, Доріан. Навряд чи це могли зробити Шаол чи Нехемія. І вже тим більше не зимові феї, що приносять подарунки хорошим дітям. Феї перестали являтися до неї після того, як вона пролила першу людську кров. А може, Нокс? Але при всій симпатії до неї звідки в нього гроші?"
"— Селено, вставати пора, — почулося з боку дверей."
"Селена обернулася й побачила, що двері відчинені й Фаліпа вже якийсь час спостерігає за її бенкетом."
"— З Ільмасом вас, Фаліпо! Хочете цукерку?"
"Фаліпа не підійшла, а підлетіла до її постелі."
"— Та вже, посвяткувала, дівчинко. Подивися, у що ковдру перетворила!"
"Селена скривилася."
"— А зуби! Вони ж у тебе всі червоні!"
"Фаліпа схопила ручне дзеркальце й подала Селені."
"Служниця не обдурила її. Зуби Селени покривав яскраво-червоний наліт. Вона спробувала злизати наліт язиком. Він не піддавався. Спробувала зчистити пальцем — те саме."
"— Прокляті льодяники! — розсердилася Селена."
"— А хто їх смоктав без перерви? — резонно запитала Фаліпа. — Вдобавок у тебе всі губи й щоки в шоколаді. Навіть мій онук брудниться менше, коли дорветься до солодкого."
"— У вас є онук? — здивувалася Селена."
"— Так. Дуже охайний хлопчик. Ніколи ніде не накришить, нічого не розіллє й рот собі не перепачкає."
"Селена відкинула ковдру, і на підлогу полетіли крупинки цукру й глазурі."
"— Фаліпо, пробачте мене. Я й справді як маленька. Візьміть цукерку. Чи шоколадку."
"— Зараз сьома година ранку, — сказала Фаліпа, зметаючи собі в долоню рештки цукрової обсипки. — До полудня ти мучитимешся животом."
"— Животом? Та кому буває погано від солодкого? — здивувалася Селена, сяючи яскраво-червоними зубами."
"— Слухай, у тебе зубки як у демона. Сьогодні не вздумай рот відкривати, а то придворних розлякаєш."
"— Та чорт із ними, з придворними! — вирвалося в Селени."
"На її здивування, Фаліпа засміялася."
"— Зі святом тебе, Селено."
"Було дивовижно приємно почути, як Фаліпа назвала її справжнім ім’ям."
"— Тобі пора вставати. Треба ще встигнути вдягнутися. О дев’ятій почнеться церемонія."
"Фаліпа поспішила в гардеробну. Селена проводила її поглядом. У цієї жінки було велике й добре серце, таке ж червоне, як льодяники. Селена згадала, як спочатку обурювалася причіпками Фаліпи, а адже та ніколи не образила й не принизила її, хоча й знала, звідки «пані Ліліана» приїхала в Рафтхол. Грубовата доброта Фаліпи була для Селени набагато дорожчою за брехливу ввічливість придворних."
"Селені раптом подумалося: а адже в кожній людині, хай дуже глибоко, але неодмінно є крупинки доброти. Повинні бути."
"До спальні Селена повернулася вбраною в скромну зелену сукню. Фаліпа вважала її єдиним гідним вбранням для храмової служби. Червоний наліт на зубах не змивався й не зтирався нічим. Мішок зі солодощами, тепер лежавший на столику, викликав у Селени легку огиду. Але вона миттю забула й про зуби, й про солодке, побачивши Доріана Хавільяра. Той сидів у кріслі. Сьогодні принц був в осліплююче-білому камзолі, розшитому золотом."
"— Що наказуєте вважати подарунком: вас чи вміст кошика біля ваших ніг? — запитала Селена."
"— А це на вибір. Якщо хочеш, можеш розгорнути мене, — сказав Доріан, піднімаючи й ставлячи на стіл плетений кошик, зверху прикритий ганчіркою. — У нас до служби є ще ціла година."
"— З Ільмасом вас, Доріане, — засміялася Селена."
"— І тебе теж… Схоже, ти вже відзначила свято. Які чарівно червоні зубки."
"Селена закрила рот і струснула волоссям. Принц раптом підскочив до неї й схопив за ніс. Селена відбивалася, але він не відпускав. Мимоволі їй довелося дихати через рот, показуючи все пишноту червоних зубів."
"— До речі, ці льодяники треба запивати водою. Тоді зуби не почервоніють."
"— Дякую. Наступного разу неодмінно врахую, — пообіцяла Селена. — Це ви прислали? — запитала вона, намагаючись якомога менше відкривати рот."
"— Так."
"Доріан підняв мішок і похитав головою:"
"— Половини вмісту як не було."
"Селена винувато усміхалася."
"— А мені не можна було їсти до вашого приходу? — запитала вона."
"— Я б теж не проти чимось почастуватися."
"— По-перше, я не знала, що ви прийдете. А по-друге, там ще вистачить."
"— Солодощі залишимо на потім. А зараз пора снідати, якщо в тебе не пропав апетит."
"Селена взяла в принца мішок і поставила на стіл, але невдало. Мішок перекинувся, і солодощі розлетілися по скатертині. У цей час ганчірка на кошику заворушилася, звідти з’явилася витягнута золотиста мордочка й потягнулася до найближчої цукерки."
"— А це хто? — запитала спантеличена Селена."
"— Подарунок для тебе. Доповнення до солодкого, — усміхнувся Доріан."
"Селена відкинула ганчірку. Мордочка тут же шмигнула назад. У кутку кошика сиділо тремтяче цуценя із золотистою шерстю й червоним бантиком на шиї."
"— Яка собачка! — вигукнула Селена, гладячи цуценя."
"Цуценя тремтіло не то від холоду, не то від страху."
"— Чим ви так налякали нещасного? — запитала Селена. — Він боїться вас так, ніби ви його покусали."
"— До речі, це не він, а вона, — пояснив Доріан. — І взагалі, боятися треба було б мені. Бачила б ти цю красуню, коли я запихав її в кошик! Вона мені ледь руку не відтяпала. А потім вила на весь замок, поки я ніс її сюди. Тільки біля твоїх дверей і заспокоїлася."
"Цуценя тим часом освоїлося й злизувало цукрові крихти з пальців Селени."
"— Доріане, ну що я буду робити з собакою? — вигукнула Селена. — Зізнайтеся, ви мені її подарували, бо не змогли знайти їй господаря?"
"— Ні! — різко заперечив принц, потім, уже тихіше, додав: — Загалом-то, так. Я згадав, як вона лестилася до тебе в загоні. А ще раніше мене здивувало, що тобі сподобалися мої гончаки. Там, в Ендов’єрі. Ти виростиш із неї хорошу собаку. У тебе є дар."
"Селена знизала плечима. Собак у неї ніколи не було. Та асасинам цього й не дозволялося. Жодних зайвих прив’язаностей."
"Цуценя дивилося на Селену своїми золотисто-карими очима. Поки це просто кумедний песик, але через рік він перетвориться на велику, сильну й швидку собаку з міцними лапами. Селена усміхнулася подарунку. Подарунок махнув хвостом, потім ще й ще."
"— Собака твоя, — сказав Доріан. — Звичайно, якщо захочеш узяти."
"— А що я буду з нею робити, якщо мене відправлять назад до Ендов’єра?"
"— Не хвилюйся, я про неї потурбуюся, — заспокоїв її принц."
"Селена почухала цуценя за оксамитовими вухами й була винагороджена щирим маханням хвоста."
"— Значить, ти не візьмеш мій подарунок, — зітхнув принц."
"— Чому ж? Обов’язково візьму, — сказала Селена, потім згадала, що цуценя — це не просто кумедна іграшка, а жива істота. — Але я хочу, щоб вона отримала справжнє собаче виховання. Інакше це чарівне створіння буде робити калюжі, де заманеться, й гризти все, що трапиться їй у зуби: меблі, туфлі, книги. Вона мусить бігати нарівні з іншими собаками, інакше її лапи будуть млявими."
"Доріан підвівся, склав руки й дивився, як цуценя освоюється в житлі Селени."
"— Доріане, ви чули?"
"— Який довгий список вимог. Краще б я подарував тобі щось із коштовностей."
"Цуценя тим часом лизнуло Селену в щоку й уткнулося носом у її плече."
"— Ні, ваша високосте. Це скромний список моїх розумних прохань. Що буде з мисливською собакою, якщо вона почне цілими днями валятися на дивані? Тому, коли я вправляюся в залі, нехай і вона вправляється на псарні. А потім я забиратиму її на ніч."
"Селена підняла подарунок у повітря, щоб собачі очі були на рівні її очей. Псина відчайдушно дригала задніми лапами."
"— Запам’ятай, люба: якщо ти вздумаєш гризти мої туфлі, я зошью собі іншу пару з твоєї бездоганної шкури. Зрозуміло?"
"Собачий ніс зморщився. Цуценя тявкнуло, ймовірно підтверджуючи свою повну згоду з новою господинею. Селена опустила його на підлогу, і він, як належить будь-якій собаці, прийнявся обнюхувати кути й закутки. Коли Доріан спробував узяти цуценя на руки, той, не роздумуючи, сховався під ліжко."
"— Ну ось, ваш подарунок залишається тут, — сказала Селена. — Дякую вам, Доріане. Це чудовий подарунок. Залишилося тільки придумати кличку."
"‘Який же він добрий, — подумала Селена. — І батьківське виховання не зіпсувало його. У нього є серце. І совість’."
"Сором’язливо, як незграбна дівчинка-підліток, Селена підійшла до принца й поцілувала його в щоку, яка виявилася дивовижно гарячою. Може, принців треба цілувати не так? Він дивився на неї широко розплющеними очима. А раптом йому щось не сподобалося? Скажімо, губи в неї надто вологі чи липкі після цукерок? Селена сподівалася, що він не стане при ній витирати щоку."
"— Пробачте, що не приготувала вам подарунка, — опустивши очі, сказала Селена."
"— Я… та я й не чекав."
"Доріан густо почервонів і озирнувся на годинник."
"— Навіть поснідати з тобою не вдасться, — сказав він. — Мені треба бігти. Увидимся в храмі. А може, я зайду після балу? Я постараюся піти звідти якнайшвидше. Думаю, що Нехемія теж там не затримається. Принц і принцеса мають право піти, коли їм заманеться."
"Селена вперше бачила його в такому стані: збентеженим, що балакає якусь нісенітницю."
"— Бажаю добре повеселитися, — сказала вона."
"Доріан не хотів повертатися до неї спиною. Він поп’ятився й ледь не налетів на стіл."
"— Тоді я загляну до тебе, — знову сказав він. — Після балу."
"Селена піднесла руку до рота, ховаючи усмішку. Невже її поцілунок привів його в таке збентеження?"
"Принц підійшов до дверей."
"— Усього найкращого, Селено, — промовив він."
"Селена усміхнулася йому, блиснувши червоними зубами. Принц засміявся, відповів їй поклоном і сховався за дверима."
"Залишившись сама, вона вирішила глянути, як освоїлося живе подарунок принца й чи немає перших несподіванок. І раптом її пронизала думка: «Нехемія прийде на бал»."
"Спочатку це була просто думка, але вона потягнула за собою інші, вже тривожніші міркування. Якщо Нехемія й справді причетна до вбивства претендентів і якщо вона якимось чином зуміла привезти в замок небезпечного, кровожерного звіра, який за її наказом накидався й розривав обезумілого від страху людей…"
"Відчуття ранкової безтурботності напрочуд зникло. Припустимо, спочатку в Нехемії були думки просто зірвати змагання. Але після бійні, влаштованої адарланськими солдатами, й загибелі п’ятсот співвітчизників ейлуейська принцеса замислила помститися. І кращого місця для помсти, ніж святковий маскарад, не знайти. У дні свят люди стають безтурботними. У відповідь на одну бійню влаштувати іншу."
"Селена трясла головою, проганяючи безглузді думки. А раптом вони не такі вже й безглузді? Що, якщо Нехемія приведе своє чудовисько в залу?.. Селені не було б шкода Кальтену й Перангона. Але ж звір не стане розбирати й цілком може кинутися на Доріана. Чи на Шаола."
"Стискаючи кулаки, Селена ходила по спальні. Попередити Шаола? Але якщо ця загроза лише плід її поганої фантазії, вона безповоротно зруйнує свою дружбу з Нехемією, а заодно й усі дипломатичні зусилля принцеси. Що ж робити? Внушити собі, що це маячня?"
"І навіщо тільки ця проклята думка влетіла їй у голову? Друзям треба вірити… поки вони не продадуть і не зрадять тебе. З цим Селена теж стикалася й тому звикла обмірковувати всі варіанти, включно й найгірші. Можливо, Нехемія нічого не замислила, а все це — кошмари власної хворої уяви Селени. Вона б із задоволенням посміялася над своїми ідіотськими страхами. Але якщо цим вечором щось станеться…"
"Селена відчинила двері в гардеробну, оглянула нарядні сукні, розвішані вздовж стін. Шаол, звичайно, буде поза себе від люті, якщо вона самовільно з’явиться на балу, але це вона витримає. Вона витримає й заслання, якщо він накаже кинути її до в’язниці. Але ось якщо з ним щось станеться, цього вона собі не пробачить. Нехай краще її ризик виявиться марним."
"— Ти що, навіть на Ільмас не усміхаєшся? — запитала вона Шаола, коли вони йшли до скляного храму, що стояв посеред східного саду."
"— Зате ти скалиш свої червоні зуби, — буркнув він."
"— Гаразд, будемо вважати твою гримасу усмішкою, — вирішила Селена, але тут же закрила рот."
"Обганяючи їх, до храму пройшли кілька придворних у супроводі слуг."
"— Дивно, що ти сьогодні не скаржишся. Пам’ятаю, на Самуїнн ти мені всі вуха прожужжала про несправедливість."
"Ну чому він не вміє жартувати, як Доріан? Одного разу Шаол сказав про неї, що такі жінки — не в його смак. Звичайно, вона не зобов’язана відповідати його смакам, але це чомусь її засмучувало."
"— А що толку скаржитися? — з награною байдужістю запитала Селена. — Можна подумати, від моїх нарікань ти розтнеш і візьмеш мене на бал."
"Ні, він ніяк не міг здогадатися про її задуми. У них Селена посвятила тільки Фаліпу, і та пообіцяла не дошкуляти її питаннями, коли вона попросила підібрати їй відповідний наряд і маску."
"— Напевно, ти досі мені не віриш, — сказала Селена."
"Це було сказано безтурботним тоном, навіть із відтінком грайливості, але з погано прихованим жалем. Що ж, ти сам винен, Шаоле Естфоле, якщо тебе цікавить тільки моя участь у цьому дурному змаганні й нічого за його межами."
"Шаол хмикнув, і на його губах з’явилася подоба усмішки. Спадковий принц часом говорив їй неприємні речі, але поруч із ним вона ніколи не відчувала себе дурною чи злочинницею. Доріан міг дозволити собі бути безтурботним, а капітан королівської гвардії — ні. Як, втім, і будь-який асасин. І потім, напевно, Шаол відчуває її неприязнь до нього. Коли ж вона навчиться ставитися до цієї людини з гідною байдужістю?"
"А за самовільну появу на балу Шаол її точно по голові не погладить. Він її все одно впізнає, навіть у найхитромудрішій масці. На що ж тоді вона сподівається? На своє вміння не потрапляти на очі. І ще на те, що покарання не буде надто суворим."
"Усередині храм виявився просторішим, ніж думала Селена. Сидячи на одній із задніх лавок, вона старанно стискала губи, намагаючись, щоб ніхто не помітив її все ще червоних зубів."
"На відміну від скляного замка скляний храм їй сподобався. Візерунчасті плитки вапняку на підлозі — це все, що залишилося від колишнього, кам’яного храму. Король Адарлана наказав його зруйнувати й замінити скляним. Скляний купол пропускав достатньо світла, і тому свічок удень не запалювали. Оскільки зараз купол був частково вкритий снігом, сонячне світло лягало красивими плямами на підлогу й лави з палісандрового дерева. Лави тягнулися в дві смуги, по сотні в кожній. Оскільки стіни теж були скляними, віконні вітражі здавалися такими, що парять у повітрі."
"Селена підвелася. Їй хотілося роздивитися тих, хто попереду. На першій лаві розташувалися королева й Доріан. Кілька рядів позаду них були зайняті королівськими гвардійцями. Герцог Перангон із Кальтеною сиділи по інший бік проходу. Трохи подалі від них Нехемія, а поруч із нею — придворні, імена яких Селена не пам’ятала. Вона намагалася висотіти Нокса, Кейна й решту претендентів, але безуспішно. Що за безглуздя? Чому їй дозволили прийти до храму, але не бажають пускати на бал?"
"— Сядь! — сердито прошепотів Шаол, смикаючи її за сукню."
"Селена скривила йому гримасу й опустилася на м’яку лаву. Кілька прочан із числа дрібної знаті іронічно ухмильнулися. Селена прошепотіла вибачення й повернулася до вівтаря. Виявилося, вона проспала й проповідь верховної жриці, і співи. Залишалося лише висидіти процесію богів, і тортури закінчаться."
"— Скільки я спала? — пошепки запитала вона Шаола."
"Капітан мовчав."
"— Я тебе питаю!"
"У Шаола були злегка червоні щоки."
"— Ти що, теж заснув?"
"— Ти спала достатньо, щоб обслинити мені все плече."
"— Ах, який ти чутливий молодий чоловік, — усміхнулася Селена й отримала стусан у ногу."
"— Досить балаганити!"
"З вівтаря спускалися молодші жриці. Це під їхні співи Селена так солодко спала. Вона позіхала й разом з іншими прочанами кивком відповідала на благословення жриць. Залунав музика, і всі витягли шиї, щоб краще бачити початок процесії богів."
"Почулися шаркаючі кроки. Прочани підвелися з лав. Богів зображували діти не старші десяти років. На очах у кожного була пов’язка, що символізувала неупередженість. Щоб юні боги не спіткнулися й, чого доброго, не розтяглися на підлозі, в пов’язках були дірочки. Процесія віддавала ярмарковим балаганом, і водночас у ній було щось наївне й зворушливе. Щороку для процесії обирали дев’ятьох дітей. Якщо «бог» зупинявся перед кимось із прочан, це означало, що він дарує тій людині своє благословення. Благословення підкріплювалося маленьким подарунком."
"Фарнор — бог війни — спочатку зупинився перед Доріаном, але потім повернувся, минув прохід і вручив маленький срібний меч герцогу Перангону. Нічого дивного."
"Мимо Селени пройшов Лумас — бог кохання. До його спини були прикріплені блискучі крильця."
"‘Яка дурна традиція’, — схрестивши руки на грудях, подумала вона."
"За Лумасом ішла Денна — богиня полювання й юних дів. Селена переминалася з ноги на ногу й лаяла себе, що вмовила Шаола дозволити їй сісти поруч із проходом. Але що це? Дівчинка зупинилася прямо перед нею й зірвала пов’язку."
"Дівчинка була справжнім янголятком. Її обличчя обрамляли світлі локони. Очі в неї були досить рідкісного карого відтінку й додатково — із зеленими крапинками. Юна богиня усміхнулася Селені й простягнула руку, аби торкнутися її лоба. У Селени миттєво спітніла спина. Сотні пар очей були звернені зараз на неї."
"— Денна, мисливиця й покровителька юних дів, дарує тобі своє благословення й заступництво на весь рік. Дозволь вручити тобі цю золоту стрілу — символ її влади й прихильності."
"Дівчинка вклонилася й простягнула Селені тонку золоту стрілу. Селена заціпеніла. Шаол злегка штовхнув її в спину. Тоді Селена взяла стрілу й теж вклонилася дівчинці."
"— Нехай пребуде з тобою благословення Ільмаса, — сказала дівчинка."
"Селена подякувала їй. Звичайно, із лука таку стрілу не пустиш, але ця річ була з чистого золота."
"‘За неї непогано дадуть, якщо продати’, — подумала Селена."
"— Мені навряд чи дозволено тримати в себе такі подарунки, — сказала вона Шаолу, простягаючи йому стрілу."
"Прочани знову сіли. Шаол опустив стрілу їй на коліна."
"— Я б не став гнівити богів."
"Селена повернулася до нього. Схоже, щось у його обличчі змінилося. Ні, точно змінилося. Селена штовхнула його ліктем і усміхнулася."

#Епізод 20

"Хвилі шовку, хмари пудри, ліс гребенів і щіток, зірки перлів і діамантів… усе це розстилалося навколо Селени, обступало її, блищало й сяяло. Фаліпа уклала їй останній локон, потім наділа маску, що закривала очі й ніс, і водрузила на голову кришталеву тіару. Навіть якби Селена й опиралася своїм відчуттям, вона все одно була б змушена визнати: так, зараз вона виглядає як справжня принцеса."
"Фаліпа, кректаючи, нахилилася, щоб почистити кришталеві пряжки на срібних черевичках новоявленої принцеси."
"— У давні часи я б назвала себе феєю-чарівницею. Це справжня ма…"
"Служниця осіклася, аби не вимовити заборонене слово, яке адарланський король викорінював вогнем і вимивав кров’ю зі словника своїх підданих."
"— Тебе просто не впізнати, — сплеснула руками Фаліпа."
"— Чудово, — погодилася Селена."
"Це буде її перший бал, куди вона з’явиться без завдання когось убити. Але й цілком зануритися у веселощі вона не зможе. Треба стежити за Нехемією, щоб принцеса не влаштувала сюрпризів придворним і собі самій. І все-таки бал — це не караульна служба й не сидіння в засідці. Якщо вдасться, вона неодмінно потанцює… хоча б трішки."
"— Ти все-таки вважаєш, що твоя затія правильна? — запитала Фаліпа, розпрямляючи спину. — Капітанові Естфолу вона дуже не сподобається."
"— Я просила не ставити мені питань, — досить різко відповіла Селена."
"— Але коли вартові витягнуть тебе з балу, не проговорися капітанові, що я тобі допомагала, — з образою в голосі парирувала Фаліпа."
"Слова служниці зачепили Селену."
"‘Нам тільки ще посваритися не вистачало’, — подумала вона й, стримуючи роздратування, підійшла до дзеркала."
"Фаліпа рушила слідом. Селена не стільки милувалася собою, скільки перевіряла маску — чи не заважає дивитися. Але сукня, принесена Фаліпою, була настільки красивою, що в Селени мимоволі вирвалося:"
"— Таких гарних суконь я ще не носила."
"Сукня була білою, але з ніжним сіруватим відтінком. Широкий поділ не стискав рухів і не заважав танцювати. Корсаж був усипаний найдрібнішим склярусом і нагадував Селені іскристу поверхню моря. По обидва боки, ближче до боків, ішла майстерна вишивка білим шовком, і її візерунок нагадував пелюстки троянд. Виріз на шиї й короткі рукави були обшиті тонкими смужками горностаєвого хутра. У вухах Селени погойдувалися діамантові сережки-крапельки, а в волосся, зібране на потилиці, Фаліпа вміло вплела нитки перлів. Сіра шовкова маска щільно прилягала до обличчя. Маску прикрашали хитромудрі візерунки з кришталевих і перлинних намистин."
"— У такому вбранні ти могла б підкорити серце короля, — сказала Фаліпа. — Ну, якщо не короля, то спадкового принца."
"— Це ж, мабуть, треба було обшукати всю Ерілею, щоб дістати таку сукню, — пробурмотіла Селена. — Де ви її знайшли?"
"— Я теж прошу не ставити мені питань, — відрізала Фаліпа."
"— Значить, ми квиті, — криво усміхнулася Селена."
"Її раптом охопила сором’язливість. Вона відчула себе маленькою дівчинкою, що потай надягла материнську сукню. І сріблясті черевички здалися їй занадто просторими. Етак і розмокнути недовго. Селена подумки відругала себе за слабкість і нагадала, заради чого затіяла всю цю авантюру."
"Годинник пробив дев’яту вечора. Фаліпа повернулася до дверей, і Селена швидко сховала за корсажем саморобний ніж."
"— І все-таки, як ти думаєш пробратися в залу? — запитала служниця. — Сумніваюся, що вартові дозволять тобі піти самій."
"Селена усміхнулася й сказала:"
"— Ми розіграємо маленький спектакль. Усе виглядатиме так, ніби принц запросив мене на бал, а я прокопалася зі зборами. Ви почнете мене лаяти, казати, що негоже змушувати його високість чекати… ви ж це вмієте. Словом, влаштуєте метушню. Вартові й оговтатися не встигнуть, як я вже втечу."
"Фаліпа обмахувалася віялом помітно почервонілого обличчя. Селена схопила її за руку."
"— Фаліпо, ну будь ласка, підіграйте мені. Якщо мене спіймають, я все візьму на себе. Скажу, що нахабно вас обдурила й що ви зовсім ні при чому."
"— Ти впевнена, що тебе спіймають?"
"Селена обдарувала її променистою усмішкою."
"— Ні, звичайно. Це я так сказала. Обіцяю: я поводитимуся розсудливо й обережно. Але погодьтеся, образливо сидіти в чотирьох стінах, коли інші веселяться."
"Тут вона говорила майже правду."
"— Нехай боги тобі допоможуть, — пошепки промовила Фаліпа, а потім, уже на повний голос, продовжила: — Ну скільки можна милуватися собою в дзеркало! Іди! І так спізнюєшся!"
"Можливо, служниця переграла. Зазвичай Фаліпа ніколи не кричала. Але поправляти її Селена не наважилася."
"Фаліпа взяла Селену за руку й вивела в коридор зі словами:"
"— Чула? Дев’ята година вже пробила! Коли його високість запрошують, негоже спізнюватися. Іди!"
"Служниця стала на порозі, шумно переводячи дух. П’ятеро вартових дивилися не стільки на Селену, скільки на неї."
"— Дякую, що допомогли вдягнутися, — сказала чисту правду Селена."
"— Кажу тобі, іди! Не гальмуй!"
"Фаліпа шумно грюкнула дверима. Селена повернулася до вартових."
"— Яка ти гарна, — сором’язливо промовив Ресс."
"— Мене б хто на бал запросив, — зітхнув його товариш."
"— Потанцюй там і за мене, — попросив третій."
"Ні в кого й думки не виникло, що Селена вирушає на бал самовільно."
"— Я тебе проведу, — викликався Ресс і простягнув їй руку."
"‘Може, воно й на краще’, — подумала Селена."
"Головне — не зіткнутися по дорозі з Шаолом. Ні, цього не станеться; капітан уже напевно в залі."
"На підході до Великої зали, коли в коридорі стали чутні звуки музики й гул голосів, Селена трохи струсила. Їй раптом здалося, що в животі в неї літає й дзижчить бджолиний рій. Вона знову нагадала собі, заради чого йде на бал. У тій, минулій житті вона з’являлася на балах зібраною й холоднокровною. Але тоді вона вбивала зовсім незнайомих їй людей. Це легше, ніж стежити за подругою. Навіть якщо Нехемія й замислила щось проти неї, Селена поки не наважувалася викреслити принцесу зі свого життя."
"Попереду показалися скляні двері Великої зали. Вони були прочинені, і Селена побачила, що зала яскраво освітлена сотнями свічок і увита гірляндами. Звичайно, їй було б куди простіше непомітно з’явитися з бокових дверей. Селена уявила: вона бреде темними коридорами, підмітаючи їх своєю бальною сукнею. Ні, про таємний вихід із її спальні не повинна знати жодна жива душа. Може, сказати Рессу, що далі вона піде сама, й пошукати інший вхід? Теж ні. Ресс хоч і простий хлопець, але може запідозрити неладне."
"До дверей залишалося кроків двадцять, коли супровідний Селени зупинився."
"— Далі я не піду. Щасливо тобі повеселитися, Селено."
"— Дякую, що провів, Рессе, — усміхнулася вона."
"Насправді до горла підступала нудота, і Селена побоювалася, як би зараз не вивергнути з себе всі ранкові ласощі. Їй хотілося стрімголов кинутися назад, грюкнути двері в свої покої й забратися під ковдру. Пізно."
"Розгубленість змінилася злістю на себе. Чого їй боятися? Треба з витонченою недбалістю спуститися сходами в залу, а якщо вона одразу натрапить на Шаола, відвести його вбік і поговорити з ним так, щоб він дозволив їй залишитися."
"Їй раптом здалося, що її черевички недостатньо міцні. Не звертаючи уваги на стражників біля дверей, Селена відійшла вбік і що є сили тупнула. Переконавшись у надійності підборів, вона попрямувала до дверей. Гвардійці привітали її стриманими кивками й ширше розчинили двері."
"Саморобний ніж, схований під корсажем, вп’явся їй у шкіру. Селена молилася Богині, всім відомим їй богам, силі долі й іншим силам, щоб сьогодні цей ніж їй не знадобився."
"Розправивши плечі, Селена вийшла на майданчик сходів."
"‘Що вона тут робить?’"
"На майданчику стояла… Селена Сардотін. Доріан ледь не впустив із рук келих. Маска на її обличчі не завадила йому впізнати свою претендентку. При всіх її недоліках Селена нічого не робила наполовину. Звичайно, вона не задовольнилася б скромною сукнею, схожою на безліч інших. Але цим вбранням вона буквально себе перевершила. І все-таки що вона тут робить?"
"Доріан охоче визнав би її появу сном наяву. Але Селену помітили. Кілька голів повернулися в її бік, потім ще й ще. Усі, хто не танцював, з цікавістю витріщалися на таємничу незнайомку, яка, злегка піднявши поділ, почала неквапливо спускатися в залу."
"Здавалося, її сукня була виткана з небесних зірок. Сіра маска виглядала б цілком звичайною, якби не переливи коштовного каміння, у великій кількості розкиданого по шовку."
"— Хто це? — схвильовано прошепотів поруч із принцом молодий придворний."
"Селена спускалася в залу так, ніби вона була порожньою. Вона йшла, ні на кого не дивлячись, а на неї зараз дивилася ледь не половина зібраних. Навіть королева підвелася, вирішивши глянути на запізнілу гостю. Нехемія, що сиділа поруч із королевою, теж підвелася. Невже Селена втратила розум?"
"‘Треба підійти до неї. Взяти її за руку’, — думав Доріан."
"Але його ноги наче приросли до мармурової підлоги, і він міг лише дивитися, як зухвала дівчина проходить останні сходинки. Маленька чорна маска не могла приховати його почервонілого обличчя. Доріан сам не розумів, чому при вигляді Селени він починав відчувати себе чоловіком. Не розпещеним молодим принцом, а королем."
"Селена зійшла в залу, і Доріан ступив було до неї. Але його випередили."
"Принц стиснув зуби, бачачи, як вона усміхнулася, а потім і вклонилася Шаолу. Капітан королівської гвардії, навіть не потрудившись з’явитися на балу в масці, простягнув Селені руку. Її очі сяяли, її довгі білі пальці рухалися назустріч пальцям Шаола. Вона дивилася тільки на нього! Зібрані почали жваво перешіптуватися, проводжаючи їх здивованими й навіть захопленими поглядами. Невдовзі Селена й Шаол зникли серед гостей. Доріан сумнівався, що їхня розмова буде рясніти придворними люб’язностями. Може, й добре, що він залишився осторонь її божевілля."
"— Тільки не кажи мені, що Естфол раптом знайшов собі дружину, — з усмішкою сказав один із придворних."
"— Капітан Естфол? — здивувався його співрозмовник. — Хіба таке чарівне створіння вийде за цього сол…"
"Згадавши, що поруч перебуває Доріан, молодий базіка прикусив язика. Принц по-старому дивився туди, де зникли Селена й Шаол."
"— Ваша високосте, ви, випадково, не знаєте, хто ця чарівна дама?"
"— Не знаю, — майже пошепки відповів Доріан і пішов геть."
"Гримуча музика й танцюючі пари заважали зосередитися. Шаол не привів, а буквально приволік Селену в одну з бокових ніш, де було порожньо й сутінково. Уявивши капітана в масці, Селена подумки усміхнулася. Дурне було б видовище. Краще вже споглядати неприкриту лють на його обличчі."
"— А тепер, — прошипів капітан, боляче стискаючи їй зап’ястя, — ти почнеш заговорювати мені зуби й запевняти, що випадково забрела сюди? Не здивуюся, якщо в тебе вже заготовлено півдюжини «переконливих причин»."
"Селена спробувала вирвати руку, але Шаол не розтискав пальців. Капітан навіть не помітив, куди він її привів. На протилежному боці якраз перебували столи для найшанованіших гостей, і там сиділи королева Георгіна й Нехемія. Королева була зайнята розмовою, а принцеса, явно нудьгуючи, обводила очима залу й випадково натрапила на Селену. Вигляд у Нехемії був здивований, якщо не сказати стривожений."
"— Відпусти мою руку. Боляче, — зажадала Селена. — Я всього лише хотіла трохи розважитися."
"— Розважитися? Зірвати королівський бал — це ти називаєш «розважитися»?"
"Сперечатися з Шаолом було марно. Селена розуміла: капітана більше за все розлютило не саме її поява на балу, а те, що вона зуміла перехитрити охорону й вийти за стіни своєї розкішної клітки. І тоді Селена вирішила змінити тактику."
"— Мені було так самотньо, — сумно зітхнула вона."
"— Пам’ятаю, раніше ти казала інше. Була б цікава книжечка, і тобі не знадобиться нічиє товариство. Я це запам’ятав. То що ж, цікаві книжечки закінчилися?"
"Селена ривком висвободила руку й прошипіла:"
"— Я не розумію твоєї логіки. Чому Ноксу дозволено тут перебувати? А він же — справжній злодій. Уявляю, як він зараз облизуватиметься на все це достаток коштовностей! Але йому можна, а мені, значить, ні? Чому? Як я зможу бути королівською захисницею, якщо ти мені не довіряєш?"
"Запитання це давно вже займало Селену, і їй хотілося знати відповідь Шаола."
"Капітан прикрив обличчя й протяжно зітхнув. Майже застогнав. Селена сховала тріумфальну усмішку. Вона перемогла!"
"— Але врахуй: один хибний крок…"
"— Вважай це моїм подарунком тобі. Як-не-як сьогодні Ільмас, — тепер уже в повний рот усміхнулася Селена."
"Шаол прискіпливо оглянув її, потім просто махнув рукою:"
"— Тільки не змушуй мене шкодувати про цей… подарунок."
"Селена провела пальцями по його щоці й прошепотіла:"
"— Сама не знаю, але чомусь ти мені подобаєшся."
"Він мовчки спостерігав, як вона зникає в натовпі."
"Селена й раніше бувала на маскарадах, і її завжди насторожувала неможливість бачити обличчя тих, хто навколо. Ця настороженість повернулася до неї й зараз. У масках були майже всі, включно з Доріаном. Хтось обмежився простою й скромною маскою, інші прагнули вразити фасоном, незвичайним кольором чи багатством оздоблення. Були й ті, хто обрав собі маски звірів і птахів. Нехемія наділа бірюзову, прикрашену золотом, у формі квітки лотоса. Вона по-старому сиділа поруч із королевою, ведучи ввічливу придворну бесіду. Телохранителі принцеси стояли в неї за спиною й відверто нудьгували."
"Стараючись, щоб Селена не бачила його, Шаол продовжив за нею стежити. Знайшовши собі зручне місце, де її не штовхали, Селена зупинилася. Що ж, місце для спостереження вона обрала чудове: звідси проглядалася подіум для шанованих гостей, сходи й значна частина зали…"
"Доріан кружляв у танці невисоку брюнетку з досить пишними грудьми. Звичайно, принц дивився переважно в виріз її сукні, а не по сторонах. Невже він не помітив появи Селени? Навіть Перангон бачив, як Шаол тягнув її в нішу. На щастя, капітанові вдалося не допустити зустрічі Селени з герцогом."
"Невдовзі вона побачила Нокса. Той фліртував із якоюсь дівчиною, що наділа маску голубки. Схоже, злодій помітив Селену. Він привітно підняв келих, потім знову повернувся до своєї супутниці. Світло-блакитна маска закривала лише вузьку смужку навколо його очей."
"— Хочу тобі ще раз нагадати: не заграйся, — сказав Селені підійшовший Шаол."
"Вона мовчки, склавши руки на грудях, розглядала строкату святкову юрбу."
"Через годину вона почала лаяти себе за дурість. Нехемія по-старому сиділа поруч із королевою. За весь цей час принцеса жодного разу не глянула в бік Селени. І як тільки їй у голову спало, що Нехемія здатна на когось напасти? Хто-хто, тільки не ейлуейська принцеса."
"Селені стало нестерпно соромно. Ні, вона не заслуговує на те, щоб називатися подругою Нехемії. Убиті претенденти, таємничі злі сили й це дурне змагання просто затьмарили їй розум."
"Лівою рукою вона поправила хутряну облямівку на вирізі сукні. Шаол стояв поруч і мовчав. Він не міг демонстративно вивести її із зали, але після балу він неодмінно згадає їй це свавілля. Звичайно, дістанеться й ротозеям-вартовим."
"Нехемія раптом підвелася зі свого місця біля трону королеви. Її телохранителі тут же стрепенулися. Селена теж напружилася. Принцеса вклонилася королеві й спустилася з подіуму. Сумнівів не залишалося: вона прямувала туди, де стояли Селена й Шаол."
"У Селени стукало у скронях. Вона дивилася, як Нехемія витончено лавирує між танцюючими. Телохранителям принцеси це вдавалося гірше. Минуло ще кілька важких миттєвостей. Нехемія була майже поруч."
"— Який у тебе чудовий наряд, Ліліано, — сказала вона адарланською з ще сильнішим акцентом, ніж раніше."
"Селені здалося, що їй ляснули по щоці. Там, у нічній бібліотеці, Нехемія говорила бездоганною адарланською. Звідки взявся акцент? Вважати його пересторогою? Забороною згадувати про нічну зустріч?"
"— І ти теж чудова, — вичавлюючи з себе слова, відповіла Селена. — Тобі подобається маскарад?"
"Нехемія теребила складки сукні — справжньої бальної сукні. Швидше за все, це був подарунок королеви Георгіни."
"— Маскарад мені подобається, але я щось утомилася, — продовжила принцеса. — Мабуть, повернуся до себе."
"Селена відповіла ввічливим кивком."
"— Звичайно. Бали виснажують. У тиші тобі стане краще."
"‘Яку ж я маячню несу! — подумала Селена. — Розігрую з себе жеманну придворну дурочку’."
"Нехемія виразно подивилася на неї. Селену обпік цей погляд — стільки болю й гіркоти було в ньому. Потім принцеса мовчки повернулася й попрямувала до сходів. Селена проводжала її поглядом, доки ейлуейка не зникла за червоними дверима."
"— Може, розкажеш, заради чого ти все це затіяла? — порушив мовчанку Шаол."
"— Тебе це не стосується."
"Селена відчувала: з відходом Нехемії небезпека не зменшилася. Бал — занадто зручне місце, щоб ударити зненацька. А принцесу вона даремно підозрювала. Нехемія — не з тих, хто стане відповідати жорстокістю на жорстокість. У ейлуейки занадто високі поняття про честь і гідність. Селена проковтнула солодкуватий грудок слини. Саморобний ніж відчувався гирею."
"‘А що це ти нюні розпустила? — одернула себе Селена. — Якщо на балу Нехемія нікому не завдала шкоди, це ще не свідчить про її невинність’."
"Селена мотнула головою, проганяючи всі свої далеко не святкові думки. Тепер, коли Нехемія пішла, вона може не тільки нести караул, а й трохи розважитися."
"— Що з тобою? — допитувався Шаол."
"— А ти здогадайся, — огризнулася Селена. — Коли ти стоїш поруч і хмуришся на всіх підряд, мене ніхто не запросить танцювати."
"— Звідки ти взяла, що я хмурюся? — здивувався він."
"Навіть зараз, вимовляючи ці слова, капітан похмуро дивився на якогось придворного, що дозволив собі надто довго розглядати Селену."
"— Припини! — зажадала Селена. — Через тебе до мене бояться підійти!"
"Шаол зітхнув і відійшов. Селена пішла за ним до невидимої межі, що відокремлювала танцюючих."
"— Ізволиш, я відійду. Якщо хтось захоче з тобою потанцювати, нехай запрошує."
"Нове місце теж виявилося досить зручним для спостереження. У всякому разі, вона одразу помітить будь-якого звіра, якщо той вискочить у залу й почне вбивати нічого не підозрюваних гостей. Втім, капітанові це незачем знати."
"Селена озирнулася на нього, і їй навіть стало шкода Шаола. Здавалося, він випадково забрів на цей бал і тепер недоумкувато: навіщо?"
"— А ти не хочеш потанцювати зі мною? — запитала Селена."
"— З тобою? Ні, — усміхнувся він."
"Щоб не дивитися на Шаола, вона вперлася очима в підлогу. Саморобний ніж противно кольнув у бік."
"‘Тільки б не до крові’."
"— Шаоле, ти хоч на час залиши свої суворості. Тут же все-таки бал, — дорікнула вона капітанові."
"— Залишити суворості? А ти забула, що Перангон теж тут? Думаю, він не зрадів би твоїй присутності. Я не хочу зайвий раз привертати його увагу."
"— Боягуз."
"Очі Шаола стали трішки теплішими."
"— Якби герцога тут не було, я б із задоволенням…"
"— Ну так я можу легко це виправити. Дозволяєш?"
"Шаол похитав головою й поправив лацкан свого мундира. Мимо продефілювали Доріан зі своєю пишногрудою партнеркою. На Селену принц навіть не глянув."
"— Думаю, у тебе є привабливіші партії, — сказав Шаол, кивком вказуючи в бік принца. — Зі мною ти занудьгуєш."
"— Досі не занудьгувала."
"— Це ти так кажеш, — сухо заперечив Шаол, але погляд її витримав."
"— Я кажу те, що думаю. Ну добре, не хочеш танцювати зі мною, тут же повно інших жінок. Невже жодна не відповідає твоїм смакам?"
"— Швидше я не відповідаю їхнім смакам."
"Це було подано як жарт, однак Селена вловила глибоко прихований сум."
"— Та ти що, Шаоле? Хіба тебе можна порівняти з цими придворними недорікуватими? І потім, ти такий чарівний, — сказала Селена, торкаючись його руки."
"Вона не лукавила. Звичайно, у Шаолі не було того солоденького чоловічого шарму, який вона так ненавиділа в здешніх придворних. Його краса була грубуватою, зате справжньою, як і його сила, честь і вірність."
"Шаол дивився на неї, забувши про бал."
"‘Що ж ти раніше на мене так не дивився?’ — подумала Селена."
"— Ти це серйозно? — тихо запитав він, косячись на їхні переплетені пальці."
"Селена ще сильніше стиснула його руку."
"— А з якої стати мені…"
"— Чому це ви обидва не танцюєте? — почулося ліворуч від них."
"Селена опустила руку. Як їй зараз не хотілося повертатися й вступати в розмову з принцем!"
"— І з ким же мені танцювати, ваша високосте?"
"У своєму камзолі свинцевого кольору Доріан був чортівськи привабливий. Його вбрання чудово поєднувалося з її сукнею."
"— Бачу, ти просто сяєш від радості, — сказав він Селені. — Та й ти, Шаоле, від неї не відстаєш, — додав принц, підморгнувши другові."
"Селена все ж змусила себе глянути на Доріана, і в неї чомусь застукало у скронях."
"— Що бажаєш, красуне? Прочитати тобі нотацію про неприпустимість появи в тих місцях, куди тебе не запрошували? Чи замість цього підеш танцювати зі мною?"
"— Сумніваюся, що одне замінює інше, — сказав Шаол."
"— Чому? — хором запитали Селена й Доріан."
"Доріан підійшов до неї ще ближче. Селені знову стало соромно за те, що хай і в думках, але дозволила собі наклепати на Нехемію. Принцеса пішла до себе, Шаол і Доріан стоять поруч, і ніхто на них не нападає. Дурно якось усе виходить."
"— Чому? — перепитав Шаол. — Бо ваш танець приверне до себе зайву увагу."
"Селена надула губи, і Шаол, наче забувши про недавню розмову, з колишньою суворістю подивився на неї."
"— Нагадати тобі, хто ти?"
"— Ні, ти й так щодня нагадуєш мені про це."
"Карі очі Шаола потемніли. Селена могла поклястися, що їхня недавня розмова їй просто привиділася. Той Шаол був зі сну. А поруч стояв справжній Шаол, готовий бити по болючих місцях."
"Доріан поклав їй руку на плече й добродушно усміхнувся другові."
"— Заспокойся, Шаоле."
"Його рука ковзнула по її спині. Крізь тонку матерію його пальці пестили їй шкіру."
"— Вважай, що в тебе сьогодні звільнення, — продовжив Доріан, відводячи Селену від капітана. — Відпочинь, насолодися життям, — додав він через плече, але вже не таким веселим тоном."
"— Піду промочу горло, — пробурмотів Шаол і попрямував в інший бік."
"Селена проводила його поглядом. Якби капітан почав ставитися до неї як до друга, це було б дивом. Ну чому він досі підозрює її в якихось таємних задумах?"
"Доріан продовжував гладити їй спину. Селена повернулася до нього, і серце в неї понеслося галопом. Усі думки про Шаола розтанули, як роса під ранковим сонцем. Може, не можна було так нарочито від нього відчіплюватися, але… але… Вона хотіла Доріана й не в силі це заперечувати. Вона хотіла його."
"— Яка ж ти гарна, — сказав Доріан, і від його занадто пильного погляду в неї запалали вуха. — Я як побачив тебе в залі, так очей не міг відірвати."
"— Невже? А я думала, ви мене навіть не помітили."
"— Шаол мене випередив. І потім, мені треба було набратися хоробрості, щоб до тебе підійти. У тобі є щось лякаюче. Особливо в цій масці, — з усмішкою зізнався принц."
"‘Значить, з грудастою брюнеткою ти хоробрості набирався!’ — засміявся глузливий внутрішній голос."
"— І вам довелося танцювати з кількома дамами, щоб подолати страх?"
"— Але я все-таки наважився, і тепер я тут."
"Її серце перестало калатати й стиснулося. Селена раптом зрозуміла, що чекала від Доріана зовсім іншої відповіді. Якої? Чого взагалі вона хоче від спадкового принца?"
"Доріан нахилив голову й простягнув їй руку:"
"— Потанцюєш зі мною?"
"Який танець грав оркестр? Селена забула про музику. Увесь навколишній світ розчинився в золотавому полум’ї свічок. Але залишалися її ноги, її руки, її рот. Селена усміхнулася й прийняла його руку, одночасно продовжуючи спостерігати за залою."
"Він загубився — загубився в світі, про який завжди мріяв. Його пальці торкалися її тіла, а воно було таким ніжним. Її м’які пальці сплелися з його пальцями. Він кружляв її по мармуровій підлозі, намагаючись рухатися якомога плавніше. Вона не збилася ні в одному па й зовсім не помічала сердитих жіночих облич. Чи чутно таке — ангажувати його високість, не дозволяючи іншим дамам танцювати з ним?"
"Доріан розумів: так, це неввічливо, особливо для спадкового принца, зобов’язаного бути зразком ввічливості. Але після Селени він просто не міг танцювати з кимось ще."
"— Ви надзвичайно витривалий танцюрист, — сказала йому Селена."
"Коли вони розмовляли востаннє? Може, десять хвилин тому чи навіть годину тому. Усі обличчя в масках злилися для неї в одну величезну різнокольорову пляму."
"— Ви так любите танцювати?"
"— Усе набагато простіше. Замість порки батьки карали мене уроками танців."
"— Тоді, мабуть, ці уроки йшли майже безперервно."
"Згадавши, заради чого вона тут, Селена оглянула залу. Збоку могло здатися, що вона когось видивляється."
"— Тобі сьогодні наговорили стільки компліментів, — сказав принц, продовжуючи кружляти її в танці. — Ледь ти з’явилася на сходах. Власними вухами чув."
"Від кожного руху її сукня переливалася миріадами крихітних вогників."
"— Це ж Ільмас, — відповіла Селена. — А в день Ільмаса всі добрі."
"В її очах промайнув біль, але вже в наступну мить вони знову усміхалися, і Доріан не знав, справді він встиг помітити цей біль чи йому просто примарилося."
"— Як поживає твій подарунок? — запитав він, обіймаючи Селену за талію."
"— Спочатку ховався в мене під ліжком, потім освоїв їдальню. Там я його й залишила."
"— Ти замкнула цуценя в їдальні?"
"— А де ж іще? У спальні не можна — почне, чого доброго, гризти килим чи намочить його. І в кімнаті для ігор залишати небезпечно. Більярдні кулі цуценяті не по зубах, а от шаховими фігурами може й почастуватися. Уявляєте, якщо шматок дерева застрягне в собаки в горлі?"
"— Треба було відіслати її на псарню."
"— У такий день? Я б не наважилася відправити малючку в це жахливе місце!"
"Доріану раптом нестерпно захотілося поцілувати Селену. Пристрасно, прямо в губи. Але це було неможливо. Навколо повно людей, а коли бал закінчиться, закінчиться й ця казка. Селена знову стане асасином, що змагається за свою свободу; він — спадковим принцом, якого рідна мати вперто намагається одружити. Але ж із кінцем балу Ільмас ще не закінчується…"
"Доріан міцніше притиснув її до себе. Навколишній світ зі всіма мешканцями перетворився на гру тіней на стіні."
"Шаол похмуро стежив, як принц кружляє Селену по залі. Треба було цього не допустити, але тепер уже пізно. Добре, що він сам не погодився танцювати з нею. Капітан бачив, якого кольору набуло обличчя герцога Перангона, коли той зрозумів, із ким це танцює спадковий принц."
"До Шаола підійшов придворний на ім’я Отон."
"— А я думав, вона буде танцювати з вами."
"— Хто? Пані Ліліана?"
"— Тож ось як її звати! Я її раніше не бачив. Мабуть, вона недавно з’явилася при дворі?"
"— Так, — коротко відповів Шаол."
"Завтра він влаштує добру прочуханку цим дурням-вартовим. У них же був чіткий наказ: цього вечора ні в якому разі нікуди її не випускати й не супроводжувати. Капітан сподівався, що до завтрашнього ранку він трохи охолоне. Зараз він був готовий лупити по їхніх порожніх головах чим завгодно."
"— Як поживаєте, капітане Естфоле? — запитав Отон, досить безцеремонно поплескуючи його по спині."
"Від придворного тхнуло сумішшю вин."
"— Щось ви перестали обідати за нашим столом."
"— Отоне, я вже три роки як не обідаю за вашим столом."
"— Ну й час летить. Шкода. Повертайтеся. Нам так бракує ваших розумних розмов."
"Отон, звичайно ж, брехав. Йому потрібні були не розмови з Шаолом, а відомості про прекрасну незнайомку. Любовні походи Отона були відомі всьому замку. Якщо йому не вдавалося спокусити когось із новоприбулих придворних дам, він вирушав до розважальних закладів Рафтхола. Отона не виганяли із замка тільки тому, що він був другом дитинства короля."
"Доріан і Селена продовжували танцювати. Шаол бачив, як вона усміхається й як сяють її очі від слів, сказаних принцом. Навіть маска не могла приховати щастя, написаного на її обличчі."
"— Тож це нова подруга принца? — запитав Отон."
"— Пані Ліліана належить собі й більше нікому."
"— Значить, вона просто танцює з Доріаном?"
"— Як бачите, — стримуючи роздратування, відповів Шаол."
"— Дивно, — знизав плечима Отон."
"— Що дивно?"
"Шаолу раптом захотілося його задушити."
"— Не моє, звичайно, діло, що там у них, але, схоже, наш принц по вуха втрескалися в цю… Ліліану, — хихикнув Отон і побрів далі."
"Перед очима Шаола з’явилася димка. Він потер очі рукою. Селена весело сміялася, а Доріан продовжував дивитися на неї. За весь цей час принц жодного разу не відвів від неї погляду. Що це? Радість? Здивування? Захоплення? Плечі Доріана були розправлені, він не дозволяв собі сутулитися. Він виглядав чоловіком. Більше того, він виглядав як король."
"Невже Доріан справді в неї закоханий? Коли це сталося? Та й чи можна довіряти словам Отона? Що цей п’яниця й волокита знає про кохання?"
"Випите вино анітрохи не заспокоїло Шаола. Він усе так само дивився на щасливих Доріана й Селену."
"‘Як цей п’яниця Отон казав? Принц по вуха в неї втрескалися. Принц. Отон же не сказав, що вони закохані одне в одного. Отже, Селена сміється й кокетує з Доріаном, але зовсім його не любить. Це Доріан закохався в неї, як дурний хлопчисько. Він і є дурний хлопчисько. І закінчиться все це розбитим серцем. А Селена — вона не така дурна’."
"Ця думка заспокоїла Шаола, але не позбавила досади. Розуміючи, що більше йому тут робити нічого, капітан королівської гвардії покинув бал."
"Поза собою від люті й заздрощів, Кальтена стежила за спадковим принцом і цією вискочкою Ліліаною Горденою. Чим, питається, вона зачарувала Доріана, якщо вже котру годину він танцює тільки з нею, не помічаючи нікого навколо? Кальтена майже одразу впізнала, хто ховається за маскою з безсмаковими блискітками. Зробити це було нескладно. Ну хто ще наважиться прийти на бал у сірій сукні? Щоб заспокоїтися, Кальтена перевела погляд на свою сукню й досить усміхнулася. У її вбранні вміло поєднувалися відтінки синього, смарагдово-зеленого й світло-коричневого кольорів. Сукня й маска у вигляді голови павича коштували таких грошей, що на них можна було б купити непоганий будиночок. Звичайно, за все платив не вона, а Перангон. Він же подарував їй чудові коштовності, що сяяли зараз на її шиї й руках. Тут вам не дешевий склярус, який наляпала на свою сірятину ця самовдоволена шлюха."
"Герцог торкнувся її руки. Хлопаючи віями, Кальтена повернулася до нього."
"— Кохана моя, ви сьогодні на рідкість елегантні, — сказала вона, поправляючи золоту ланцюжок на його червоному камзолі."
"Обличчя герцога швидко набуло кольору камзола. Чи зможе вона цілувати його, вміло придушуючи огиду? Увесь цей місяць вона спритно ухилялася від його домагань, але зараз, коли Перангон встиг добряче навантажитися вином…"
"Треба якомога швидше придумати якийсь привід. Цю думку перебила інша, що повернула Кальтену до невеселих висновків. Ось уже й новий рік почався, а вона все так само далека від Доріана, як і минулої осені. Та й Ліліану їй досі не вдалося потіснити."
"Голову Кальтени пронизав нестерпний біль. На мить вона побачила розверзну безодню. Потім біль стих, і прийшло рішення, просте й ясне: Ліліану треба просто прибрати. Як — це вже інше питання."
"Коли годинник пробив третю годину ночі, Селена вирішила, що їй пора повертатися до себе. Хтось ще танцював, але королева вже покинула бал. Селена пошукала очима Шаола й не знайшла. Коли Доріан оголосив, що зараз принесе їм чогось прохолодного, Селена непомітно зникла. По інший бік червоних дверей її терпляче чекав Ресс. Вартовій повів її коротким шляхом — порожніми коридорами для слуг. Тим краще, тут їм не трапляться цікаві придворні, яким вона й так встигла намозолити очі. Що ж, навіть якщо її побоювання не виправдалися, вона трохи розважилася, танцюючи з Доріаном. Більше ніж «трохи», якщо вже говорити правду. Селена усміхалася, стукаючи підборами по гулких плитах. А адже Доріан поводився з нею не як із черговою своєю дурненькою подружкою. Принц забув про всіх інших жінок. Він взагалі забув про всіх, хто був у залі. Але що ще важливіше, він забув, що вона асасин і що її свобода поки залишається під питанням. Виходить, зовсім не дарма вона самовільно з’явилася на цьому балу."
"Нарешті Ресс звернув у знайомий коридор, що вів до її покоїв. Там, біля дверей, балакаючи з вартовыми, стояв Доріан. Схоже, принц знав ще коротший шлях із Великої зали сюди. У Селени знову закалатало серце. Вона боялася, що своїм самовільним відходом усе зіпсувала, й сором’язливо усміхнулася принцу. Доріан уклонився й мовчки відчинив двері. Вони увійшли. Селені було байдуже, як до цього поставиться Ресс та інші вартові."
"Селена квапливо зірвала маску й кинула на столик у передпокої. Після спекотної зали вона із задоволенням вдихала прохолодне повітря."
"— Звичайно, я не повинна була… — пробурмотіла вона, впираючись спиною в двері спальні."
"Доріан підійшов до неї майже впритул."
"— Ти пішла, навіть не попрощавшись, — усміхнувся він, впираючись руками в стіну."
"— Я подумала, що далі не можна дражнити придворних дам, а то вони роздеруть мене на шматки. Ви теж умієте непомітно зникати. Чудова якість. З вас би міг вийти асасин. Я дивуюся, як швидко ви сюди дісталися, і навіть без натовпу охаючих і ахаючих жінок."
"— Мене не цікавлять охаючі й ахаючі жінки, — тихо сказав принц, відкидаючи з обличчя пасмо волосся."
"Він обійняв Селену й міцно поцілував. У нього був теплий рот і м’які губи. Час і простір перестали для неї існувати. Її відповідний поцілунок був повільним. Доріан злегка відсторонив її від себе, зазирнув їй в очі й поцілував знову — тепер уже пристрасно, не приховуючи бажання."
"Її руки були одночасно важкими й легкими. Стіни й підлога передпокою кружляли, і Селені це подобалося. Вона не могла зупинитися. Їй подобалося, коли її цілують, подобався запах принца, смак його губ. Їй подобалося відчувати його поруч."
"Доріан знову притягнув її до себе, тепер уже міцніше. Вони самозабутньо цілувалися, не рахуючи поцілунків. Невже це той самий спадковий принц, той Доріан, що надменно поглядав на неї, коли вони вперше зустрілися в Ендов’єрі?"
"Ендов’єр. Селена розплющила очі, виринувши з блаженного безчасся. Навіщо вона цілує спадкового принца Адарлана? Її пальці розтиснулися, і рука, що лежала в нього на спині, опустилася."
"Доріан відірвався від її губ і усміхнувся. Бажання цілуватися не відпускало його. Він був готовий продовжити, але Селена пальцями закрила свої губи."
"— Мені пора лягати, — сказала вона."
"Доріан здивовано підняв брови."
"— Одній, — додала вона."
"Принц спробував знову поцілувати її, але Селена спритно прослизнула під його рукою й схопилася за дверну ручку. Не давши йому отямитися, вона вбігла до спальні. Доріан не робив спроб піти за нею, але й не йшов. Через хвилину Селена обережно визирнула в передпокій. Доріан усе так само стояв і усміхався."
"— Спокійної ночі, — сказала вона."
"Доріан нахилився до неї."
"— Спокійної ночі, — прошепотів він і поцілував її."
"Селена не опиралася. Світ знову перестав існувати…"
"Отямившись, Доріан досить різко відсторонився, і Селена ледь не впала. Їй удалося вхопитися за одвірок. Доріан тихо засміявся."
"— Спокійної ночі, — ще раз сказала вона, торкаючись палаючого обличчя."
"Доріан мовчки зник за вхідними дверима."
"Селена побігла до балкона, розчахнула його й із насолодою вдихнула холодне повітря. Притиснувши руку до губ, вона закинула голову й подивилася на зірки, відчуваючи, як її серце стає все більшим і більшим."
"Доріану не було куди поспішати. Він брів до себе під акомпанемент власного серця. Він усе ще відчував на своїх губах її губи, вдихав аромат її волосся й бачив золотаві відблиски свічок у її зіницях."
"Наслідки? Плювати йому на наслідки. Він знайде спосіб подолати наслідки. Він вишукає можливості бути з нею. Він мусить це зробити."
"Зворотного шляху немає. Він стрибнув зі скелі, не думаючи, що може потрапити в пастку."
"У нічному саду капітан королівської гвардії стояв під балконом Селени й дивився, як вона кружляє в танці під музику своїх мрій. Одне він знав точно: її думки зараз були не про нього."
"Потім вона перестала танцювати й підняла голову до неба. Навіть здалеку Шаол бачив, як почервоніли її щоки. Вона була вражаюче юною… ні, не юною. Вона була якоюсь новою, незнайомою йому Селеною. Капітан відчув незвичний біль у грудях."
"Він продовжував стояти й дивитися, доки вона зябко не повела плечима й не пішла з балкона. Йдучи, вона ще раз глянула на зірки. Дивитися вниз їй не хотілося. Та й що там може бути, окрім заметілей?"

#Епізод 21

"Щось мокре й холодне ткнулося їй у щоку, потім узялося облизувати обличчя. Селена скривилася й розплющила очі. На неї, виляючи хвостиком, дивився вчорашній подарунок принца. Селена підвелася на лікті. У вікно повним ходом світило сонце. Невже вона проспала? Їй же треба вправлятися. Через два дні — останнє випробування. Їх залишиться тільки четверо. Потім — два попередні поєдинки й один завершальний."
"Селена протерла очі. Цуценя узялося лизати їй руку."
"— Ти, напевно, хочеш сказати, що встигло наробити на підлозі? — запитала Селена, чухаючи цуценячі вуха."
"— Ні в якому разі, — почулося за дверима."
"Двері широко розчахнулися. На порозі стояв усміхнений Доріан."
"— Твого цуценяти вранці вигулювали разом з іншими собаками. Я подбав."
"Селена мляво усміхнулася принцу:"
"— Чи не зарано для візиту?"
"— Зарано? — перепитав Доріан, вмощуючись на край постелі."
"Селена відсунулася."
"— До речі, вже перша пополудні, — повідомив він. — Фаліпа мені сказала, що ти спиш як убита."
"Перша пополудні! Ну вона й заспалася. А як же вправи з Шаолом? Селена почухала ніс, потім сіла й посадила цуценя собі на коліна. Схоже, ніч пройшла спокійно. Нових нападів не було, інакше принц розповів би про них. Селена полегшено зітхнула, але тут же згадала про свої безглузді підозри щодо Нехемії. Її знову захлеснула хвиля сорому."
"— Ти вже придумала їй ім’я? — запитав Доріан, киваючи на цуценя."
"‘Який спокійний, зібраний, холоднокровний. Невже на балу й потім… усе це була вміла гра?’"
"— Ім’я? Ще не встигла, — відповіла Селена, якій від усіх своїх вад хотілося кричати на повний голос."
"— Може, назвати її… ну, скажімо, Золотинкою?"
"— Найдурніше з усіх собачих кличок, — заперечила Селена. — Так називають кімнатних собачок."
"Вона обережно взяла цуценя за передню лапу й почала її розглядати. Зараз це не дуже помітно, а адже собака виросте швидконогою… Ось і ім’я! Як просто, й голову ламати не треба."
"— Швидконога. Ось як я її назву."
"Здавалося, ім’я давно вже ховалося всередині Селени й чекало, коли вона дозволить йому вистрибнути назовні."
"— Так. Тебе звати Швидконога, — сказала вона цуценяті."
"— Уперше чую, щоб собаці давали таке ім’я, — здивувався принц. — І що воно означає?"
"— А це означає, що коли вона виросте, то обжене всіх ваших чистопородних псів."
"Селена поцілувала Швидконогу в ніс, потім підняла й зазирнула їй в очі. Дивно, але в цуценяти гончака були всі задатки кімнатної собаки. Схоже, найбільше Швидконозі подобалося ластитися й лизатися."
"— Це ми ще подивимося, — сказав принц."
"Швидконога спритно шмигнула під ковдру й затихла."
"— Тобі добре спалося? — запитав Доріан."
"— Як бачите. А вам, напевно, не дуже, раз ви піднялися в таку рань."
"— Послухай… — почав він, і Селені захотілося стрибнути з балкона. — Учора вночі… Пробач, якщо я був занадто наполегливим… Селено, чому ти кривишся?"
"Невже вона й справді скривилася?"
"— Вибачте."
"— Значить, я тебе засмутив?"
"— Чим?"
"— Поцілунком!"
"Селена поперхнулася й закашлялася."
"— Ні, що ви, — пробурмотіла вона, колотячи себе в груди, щоб протовкнути цей грудок. — Не скажу, щоб я цього чекала. Але й неприязні ваші поцілунки в мене не викликали, якщо вас це турбує."
"Вона одразу ж пошкодувала про сказане."
"— Тобто тобі сподобалося? — запитав Доріан, ліниво усміхаючись."
"— Ні! Ідіть геть!"
"Селена укрилася з головою. Їй стало нестерпно соромно. Ну чому вона поводиться як остання дурниця?"
"Швидконога радісно облизувала господиню. Ковдра була щільною, і денне світло крізь неї майже не проникало."
"— Це що за дівчачі штучки? — засміявся Доріан. — Можна подумати, що тебе ніколи не цілували."
"Селена відкинула ковдру. Швидконога залізла ще глибше. Здається, їй теж був неприємний візит принца."
"— Ні, мене цілували, — сердито заперечила Селена, намагаючись не думати про Саема й про те, що їх пов’язувало. — Але мене цілувало не зарозуміле нікчемство в мереживній сорочці, не самовдоволений, розбещений хлопчисько королівських кровей!"
"Доріан згадав, що так і не зняв учорашню мереживну сорочку."
"— А сорочка щось змінює? — здивовано й у якомусь замішанні запитав він."
"— Замовкніть! — крикнула Селена й ударила його подушкою."
"Вона перелізла на інший край постелі, встала й підійшла до балкона, спиною відчуваючи, що Доріан зараз повним ходом витріщається на неї. І на спину, благо виріз ззаду це дозволяв. І на три прокляті шрами."
"— Будете чекати, поки я перевдягнуся?"
"Доріан не відповідав. Селена повернулася до нього. Сьогодні його погляд був зовсім іншим, не таким, як учора вночі. Сьогодні його погляд був настороженим і якимось невиразно сумним. У Селени кров понеслася по жилах."
"— Чому ви мовчите?"
"— Твої шрами… які вони жахливі, — майже пошепки відповів Доріан."
"Селена зупинилася біля дверей гардеробної."
"— А в нас, Доріане, у всіх є шрами. Просто мої помітніші. Можете сидіти тут, якщо вам так подобається, а я пішла вдягатися."
"Кальтена йшла поруч із герцогом Перангоном нескінченно довгою королівською оранжереєю. Як і багато будівель замка, оранжерея теж була цілком зі скла. Волога задуха змушувала Кальтену постійно обмахуватися віялом. Треба ж було герцогу обрати таке дивне місце для прогулянки. Квіти й рослини цікавили пані Ромпір не більше, ніж брудні вуличні калюжі."
"Перангон зірвав білосніжну лілею й церемонно подав Кальтені:"
"— Це вам."
"З усіх сил вона старалася не кривитися при вигляді його вкритого віспинами обличчя й яскраво-рудих вусів. Одна тільки думка про близькість із ним викликала в неї шалене бажання повиривати з коренем усі здешні диковинні рослини й викинути на сніг."
"— Дякую вам, ваша світлосте, — сиплим голосом відповіла вона."
"Перангон кинув на неї пильний погляд."
"— Щось сьогодні ви не в настрої, люба Кальтено."
"— Невже? — запитала вона, змусивши себе кокетливо вскинути голову. — Сьогоднішній день блідне в порівнянні з чудовим балом. Я отримала стільки задоволення."
"Чорні очиці герцога так і буравили її. Відчувалося, Перангон не вірить її словам. Він узяв Кальтену під лікоть і повів далі."
"— Люба моя, не треба мене дурити. Думаєте, я не помічав, з якою жадібністю ви стежили за кожним жестом спадкового принца?"
"Кальтена здивовано вигнула вищипані брови."
"— Ваша світлосте, вам просто здалося."
"Перангон провів товстим пальцем по гілці папороті. Чорне кільце на пальці тьмяно блищало, і кожна спалах збігалася зі спалахом болю в голові Кальтени."
"— Не треба вдавати. Я теж за ним спостерігав. І ще більше за дівчиною, від якої він не відходив ні на крок. Настирлива особа, чи не так?"
"— Ви про пані Ліліану? — обережно запитала Кальтена, не знаючи, радіти їй чи ні."
"Головне, Перангон не помітив, як пристрасно їй самій хотілося опинитися поруч із принцем. А Доріан справді не відходив від цієї вискочки ні на крок. Тут герцог правий."
"— Це вона себе називає Ліліаною, — пробурмотів герцог."
"— Тож у неї інше ім’я? — затамувала подих Кальтена."
"Очі герцога стали такими ж чорними, як його кільце."
"— Невже ви серйозно думаєте, що вона знатного походження?"
"— А хіба ні? — розігруючи наївність, запитала Кальтена."
"Перангон криво усміхнувся й розповів їй, ким насправді є вчорашня пасія Доріана й із яких країв принц привіз її до замка."
"Коли герцог закінчив розповідь, Кальтена могла лише ошеломлено дивитися на нього. Тож Ліліана Гордена — це… подумати навіть страшно… Селена Сардотін! Найвідоміший асасин королівства. І тепер ця холоднокровна, безжальна вбивця готувалася вонзити свої кігті в серце Доріана. Якщо Кальтена справді хоче домогтися руки спадкового принца, треба діяти тонко й розумно. Можливо, придворним варто дізнатися, з ким вони живуть під одним дахом. Та й королеві не завадить повідомити. Але тут важливо не допустити навіть найменшої оплошності. Ризик може все зіпсувати."
"В оранжереї стало тихо, наче всі рослини й квіти теж затамували подих, ошеломлені страшною новиною."
"— Хіба ми можемо дозволити, щоб події розвивалися в небезпечному напрямку? Невже принц не розуміє, з ким він фліртує?"
"Обличчя герцога скривилося гримасою, але це тривало всього мить, і Кальтена нічого не помітила. Від почутого в її голові застукали молотки. Як невчасно! І знову їй доведеться терпіти, поки вона не добереться до рятівного опіуму."
"— Ми не маємо права залишатися осторонь, — сказав герцог."
"— Але як нам убезпечити принца? Може, негайно повідомити короля?"
"Перангон похитав головою. Його рука теребила ефес меча. Це допомагало герцогові думати. Кальтена розглядала рожевий кущ, водячи довгим нігтем по викривлених шипах."
"— Селену чекають поєдинки з рештою суперників, — нарешті промовив Перангон. — Перед завершальним поєдинком вона муситиме випити ритуальну чашу на честь Богині й богів."
"Кальтена завмерла."
"— Я мав намір зробити вас… посланницею Богині. Тоді ви зможете додати в чашу Селени… чогось іще."
"— Я мушу вбити її власними руками? — насторожилася Кальтена."
"Вона була готова зробити це чужими руками, але сама…"
"— Ні, звичайно, — похитав головою герцог. — Але король погодився: треба діяти найрішучішим чином і все обставити так, щоб Доріан повірив, ніби це був… нещасний випадок. Нам нема чого вбивати Селену. Треба підлити їй у вино крапельку «поцілунку смерті». Померти вона не помре, але втратить самовладання, і перемога дістанеться Кейну."
"— А хіба Кейн сам не може її вбити? Ви ж знаєте, скільки випадковостей відбувається під час поєдинків."
"Молотки в голові Кальтени застукали гучніше й вимогливіше. Кожен удар загрожував розколоти їй череп. Напевно, герцог правий. З отрутою менше клопоту…"
"— Кейн теж думає, що впорається з нею, але я не хочу ризикувати."
"Перангон стиснув руки Кальтени. Кільце на його пальці було холодніше льоду. Кальтена з труднощами стримувалася, щоб не висмикнути руки."
"— Хіба ви не хочете допомогти Доріану? — запитав він. — Як тільки він позбудеться прив’язаності до неї…"
"‘Він стане моїм, — подумки договорила Кальтена. — Він стане моїм, бо він мусить бути моїм. Але заради цього піти на вбивство… Він стане моїм’."
"— І тоді ми спільними зусиллями зуміємо повернути принца на правильний шлях, — широко усміхаючись, закінчив Перангон."
"Інтуїція кричала Кальтені: «Втікай із замка. Втікай негайно, без оглядки»."
"Однак крик інтуїції тонув у привітальних вигуках придворних, що славили королеву Кальтену. Вона бачила себе поруч із принцем, на троні. Корона — найкращі ліки для її голови."
"— Кажіть, що мені треба зробити, — прошепотіла Кальтена."
"На Часовій вежі годинник пробив десяту. Селена, що сиділа в себе в спальні над книгою, підняла голову й подивилася в темряву вікна. Найкращий час спати чи намагатися заснути. Швидконога, що дрімала в неї на колінах, широко позіхнула. Селена почухала цуценя за вухами й повернулася до читання. З книжкової сторінки на неї дивилися «знаки долі». Їхні лінії й вигини, стріли й кола зверталися до Селени мовою, в якій вона не знала не те що слів, а навіть букв. Скільки ж років Нехемія осягала все це? Можливо, з самого дитинства. І як сила «знаків долі» могла зберегтися, якщо магія покинула Ерілею?"
"Після балу Селена більше не бачилася з принцесою, не шукала зустрічі з нею й не наважувалася поділитися з Шаолом тим, що дізналася про ейлуейку. Швидше за все, Нехемія чудово говорила адарланською, але в неї були причини приховувати й це, й свою обізнаність щодо «знаків долі». Селена шкодувала, що пішла на бал. Її досі мучив сором: ну як вона могла навіть у думках допустити, що Нехемія здатна творити зло? Нехемія високо цінувала честь. І дружбу теж. Вона б не наважилася зробити свою подругу мішенню для помсти. Адже вони з Нехемією — подруги. Точніше, були подругами, подумки поправила себе Селена, ковтаючи гіркуватий грудок слини."
"Вона перегорнула сторінку й завмерла."
"З пожовклого пергаменту на неї дивилися ті самі знаки, що зустрічалися їй біля роздертих тіл. На полях чиясь рука поспішним почерком вивела пояснення. Запису цій було кілька сотень років: «Жертвоприношення риддераку. Кров’ю жертви окресліть простір навколо неї. Коли викликане чудовисько з’явиться, знаки слугуватимуть мірою обміну. За плоть жертви риддерак передасть покликавшому його силу жертви»."
"Безуспішно намагаючись угамувати тремтіння в руках, Селена узялася гортати далі, шукаючи хоча б крихти відомостей про знаки, виявлені під ліжком. Нічого. Тоді Селена повернулася до сторінки із заклинанням. Тож ось як звуть це чудовисько — риддерак. Хто він? Звір? Звіроподібна істота, що має деяку схожість із людиною? І звідки, з якої глушині його викликають цим заклинанням? Швидше за все, не з глушині, а з темного світу. І проходить він через…"
"Врата Вэрда! Селена піднесла долоні до втомлених очей. Значить, хтось за допомогою «знаків долі» відкривав портал, щоб викликати риддерака. Як таке можливо? Магія покинула Ерілею. Але в цій книзі вона прочитала, що «знаки долі» діють незалежно від магії. Діють… досі? Невже… невже Нехемія могла приготувати й їй долю бути роздертою риддераком? Своїй подрузі? І головне, навіщо? Навіщо принцесі взагалі вбивати претендентів і забирати собі їхню силу? І як їй вдавалося так добре оточувати свої діяння таємницею?"
"Селені було соромно підозрювати Нехемію. Але що вона по-справжньому знає про ейлуейську принцесу? Тільки те, що Нехемія їй розповідала. А Нехемія цілком може виявитися вмілою лицедійкою. Вона побачила самотність Селени, потребу в спілкуванні й уміло зіграла на почуттях колишньої в’язниці Ендов’єра. І адже як уміло все обставила! Вони обидві — чужі в цьому замку, де стільки ворожого. Їм треба триматися разом хоча б для того, щоб просто розмовляти. Нехемія зуміла зачарувати собою Селену, і та, як наївна дитина, бачила в принцесі лише те, що хотіла бачити, радіючи їхній дружбі."
"Селена кілька разів ковтнула повітря. Вона боялася продовжувати ці міркування, як діти бояться, що чарівна казка не витримає дотику з реальним світом. Нехемія гаряче любила свою батьківщину. У цьому вона не лукавила. Селена бачила: принцеса була готова на все, щоб в Ейлуе було якомога менше потрясінь."
"А раптом Нехемії мало хиткого миру з Адарланом? Мало жалюгідних поступок адарланського короля? Що, якщо принцеса замахнулася на більше — зробити так, щоб адарланський король назавжди попрощався з задумами підкорення Ейлуе? Звичайно, цього не доб’єшся бесідами з дурнуватою Георгіною. Цього не доб’єшся проханнями й благаннями, зверненими до короля."
"Селену пронизала думка, від якої все всередині вкрилося товстою кіркою льоду. А що, якщо Нехемія готує… повстання? Це слово боялися вимовляти вголос. Що, якщо принцесі недостатньо розрізнених купок повстанців, що ховаються по лісах і горах? Раптом вона хоче, щоб усі королівства повстали проти Адарлана? Колись розумні голови саме до цього й закликали. Але кожна країна думала, що адарланський король підкорить її сусідів і на цьому зупиниться."
"Тільки навіщо вбивати претендентів на титул королівського захисника? Розумніше було б обезголовити королівську раду, і бал — найвдаліше місце для цього."
"Селена подумки уявила покої Нехемії. Вони були просторішими, ніж відведені їй, але й там принцеса не змогла б сховати риддерака. Це чудовисько взагалі було неможливо сховати ні в одному, навіть найзатишнішому кутку замка… Але зате під замком існував цілий лабіринт забутих і покинутих переходів і приміщень, куди десятками, якщо не сотнями років не ступала жодна нога."
"— Ні! — майже крикнула Селена."
"Вона поривчасто встала, перекинувши стілець. Швидконозій удалося вчасно зістрибнути з колін господині."
"Бути цього не може, бо Нехемія, бо…"
"Кректаючи, Селена відсунула вбік важкий комод і підняла нижній край шпалери. Як і два місяці тому, із щілин потягнуло холодним, вологим повітрям, але сьогодні в ньому не було й натяку на аромат троянд. Селена згадала дивну закономірність: усі вбивства відбувалися за два дні чи за день до чергового випробування. Це означає… нинішньої чи наступної ночі хтось із претендентів стане новою жертвою риддерака. Дурно сподіватися, що цього разу чудовисько не з’явиться в замку. А якщо згадати «знаки долі», намальовані в неї під ліжком… найближчий візит риддерак нанесе саме їй."
"Вигнавши тремтячого й скавулячого цуценя зі спальні, Селена взяла підсвічник із майже цілою свічкою, свій саморобний ніж і книгу. Відкривши двері в потайний коридор, вона розгорнула шпалеру, а книгу, наче клин, вставила між одвірком і дверима, щоб не зачинилися. Битися з риддераком жалюгідною зв’язкою шпильок було все одно що йти на лева з соломинкою, але іншої зброї Селена так і не обзавелася. У крайньому разі, згодиться й важкий підсвічник."
"Досить міркувати, сидячи за столом. Досить будувати здогадки. Якщо Нехемія їй збрехала, якщо принцеса вбивала претендентів, Селена мусить переконатися в цьому власними очима. І якщо страшні припущення виявляться правдою, Нехемію вона вб’є й голими руками."
"Селена спускалася назустріч холодним потокам повітря. Минулого разу тут було тепліше, а зараз у неї з рота йшов пар. Опинившись біля трьох знайомих порталів, Селена з тугою подивилася на середній. Ні. Навіщо їй тікати зараз, коли вона так близько до перемоги? Ось якщо вона програє, то втече із замка раніше, ніж вони зберуться відправити її в Ендов’єр."
"Лівий портал вів угору, в покинуті коридори й вузькі лази під стелею Великої зали. Правий — у забутий склеп, де поховані Еліана й Гавін. По дорозі туди Селена бачила численні бічні відгалуження."
"Наблизившись до правого порталу, Селена завмерла на місці, побачивши ланцюжок слідів, що зникають у темряві. Сліди були зовсім свіжі, інакше вітер замів би їх пилом."
"А адже в цих підземеллях можна спокійно сховати цілу дюжину риддераків. Швидше за все, і в покоях Нехемії була двері, що виводила в потайний коридор. Користуючись свободою пересування замком, принцеса напевно вивчила всі його закутки. І навряд чи вона щоразу викликала риддерака. Ні, вона ховала своє чудовисько в здешніх підземеллях. Селені раптом згадалося, як тоді, в саду, Верин дозволив собі посміятися над принцесою. Тієї ж ночі він загинув, роздертий риддераком."
"Селена міцніше стиснула в лівій руці підсвічник, а правою дістала з кишені свій сміхотворний ніжик. Спуск починався майже одразу після порталу. Крок за кроком вона почала рухатися вниз. Верхня площадка зникла в темряві, а нижня ніяк не наближалася. Невдовзі до слуху Селени почав долітати якийсь шепіт. Вона одразу згадала голоси привидів. Невже знову вони? Селена сповільнила кроки й закрила рукою свічку. Ні, голоси були цілком людськими. І навіть не голоси, а один голос, поспішно, майже наспів промовляючий слова."
"Це не був голос Нехемії. Це був чоловічий голос."
"Сходи вивели її на площадку. Сходинки продовжувалися далі, йдучи вниз, а ліворуч відкривався прохід у приміщення. Звідти пробивалося зеленкуватий світло. Пройшовши ще кілька кроків, Селена відчула, як у неї встають дибки волосся. Голос промовляв не слова, а різкі, скреготливі й утробні звуки. Таких звуків не було й не могло бути ні в одній мові Ерілеї. У Селени почало холодіти все тіло, наче ці бурмотіння відбирали в неї тепло. Разом із жахливими звуками вона чула важке дихання того, хто їх промовляв. Здавалося, вони палять йому горло, бо він шумно втягував у себе повітря."
"Потім людина замовкла. Опустивши на підлогу підсвічник, Селена поповзла до дверей. Важкі дубові двері були відчинені навстіж. У іржавому замку стирчав такий же іржавий ключ. Усередині кімнатки, перед чорним прямокутником, густа чорнота якого, здавалося, ось-ось накинеться й поглине все навколо, на колінах стояв Кейн."

#Епізод 22

"Кейн. Це він з кожним днем, з кожним випробуванням ставав усе сильнішим і вправнішим. Раніше Селена пояснювала його успіхи старанними вправами… Ні, Кейн обрав легший і зловісніший шлях. За допомогою «знаків долі» він викликав кровожерне чудовисько й в обмін на кров і плоть жертв отримував їхню силу."
"Кейн стомлено провів руками по підлозі. Його права рука рухалася вздовж межі темряви, і темрява втягувала зеленкуватий світло, що струменіло з пальців. Ліва рука була вся в крові."
"Селена завмерла. Вона боялася, що звук дихання видасть її присутність. Із темряви долинули шкребучі звуки. Чиїсь кігті дряпали камінь. Потім почулося шипіння, схоже на шипіння полум’я, що заливають водою. Нарешті перед коліноприклонним Кейном з’явився риддерак."
"Це не був кошмарний сон чи легенда епохи богів давнини. Це була кошмарна яв. Безформна голова, зовсім безволоса, обтягнута сірою шкірою, і величезна, широко розкрита паща, усипана гострими чорними зубами."
"Зубами, що розірвали на клапті й пожерли нутрощі Веріна й Ксав’єра. Людські мізки, напевно, вважалися в риддерака ласощами. Ісчаддя, точніше не скажеш. Будь його облік цілком звірячим, він викликав би менший страх. Але тіло риддерака радше нагадувало людське, ніж звіряче. У нього були досить короткі ноги й занадто довгі руки. Явившись із темряви, риддерак присів навпочіпки, вп’явши кігті рук у камінь. Кейн підняв голову й повільно встав. Риддерак опустився на коліна й уп’явся в підлогу чорними очима. Чудовисько корилося Кейну."
"Селена тільки зараз відчула, що вся тремтить. Вона обережно поп’ятилася. Тільки б швидше покинути це страшне місце й тікати, стрімголов тікати до себе в спальню. Їй згадалися слова Еліани. Так, риддерак був утіленням первісного зла. Він був створений зі зла й не знав іншого, як тільки творити зло. Амулет на шиї Селени здригався, наче живий. Здавалося, і він вимагав: «Тікай!» У роті в неї пересохло, у скронях стукала кров. Крок назад. Ще крок."
"У цей час Кейн різко обернувся й побачив її. Риддерак закинув голову, роздувши щілини ніздрів. Селена завмерла, а ще через мить сильний порив вітру вдарив їй у спину, вштовхнувши назад."
"Уся увага Селени була прикута до важко дихаючого, мокрого від поту риддерака."
"— Загалом-то сьогодні я збирався почастувати його не тобою, — усміхнувся Кейн. — Але гріх не скористатися нагодою."
"— Кейне, — тільки й могла прошепотіти Селена."
"Очі риддерака… вона ніколи не бачила нічого подібного. Навіть у кошмарних снах. У цих очах відображався голод. Невгамовний, що налічував сотні років. Риддерак явився сюди з іншого світу. З світу темряви й голоду. Виходить, «знаки долі» зберігали свою силу, і Врата Вэрда не були поетичною метафорою. Селена дістала саморобний ніж. Жалюгідна зброя, якою не кожного людини вб’єш. А тут — риддерак."
"Кейн одним стрибком опинився в Селени за спиною, встигнувши вихопити в неї ніж. Жодна людина, навіть найшвидша й найспритніша, не могла б рухатися зі швидкістю вітру чи тіні."
"— Співчуваю, — прошепотів він, ховаючи її зброю в кишеню."
"Селена дивилася то на нього, то на риддерака, не в силі повірити, що все це відбувається наяву."
"— Може, мені варто було б залишитися й подивитися, як він тобою закусує, — усміхнувся Кейн, беручися за ручку дверей. — Але піду, не буду вам заважати. Прощавай, Селено."
"Він шумно грюкнув дверима."
"На підлозі зеленкувато мерехтіли «знаки долі», які Кейн намалював власною кров’ю. Їхнього світла вистачало, щоб бачити голодні, безжальні очі риддерака."
"— Кейне, — п’ятившись до дверей, прошепотіла Селена."
"Двері не піддавалися. Селена смикнула ручку. Він замкнув двері на ключ. У цій клітці — нічого, окрім каменю й пилу. Кам’яні стіни, кам’яна підлога, звідки не виламати навіть маленького шматочка. Як же вона дозволила Кейну так легко себе роззброїти?"
"— Кейне! — тепер уже крикнула вона й прийнялася молотити кулаками в двері."
"Двері не піддавалися, а Кейн давно зник."
"Риддерак стояв на чотирьох, погойдуючись із боку в бік. Селена помилилася: його задні кінцівки не були коротшими за передні. Вони були однакової довжини. Тонкі, схожі на жердини. Але чому риддерак не кинувся на неї одразу, як тільки Кейн пішов? Чудовисько принюхувалося й дряпало підлогу, залишаючи глибокі борозни."
"Селена зрозуміла: вона потрібна йому живою. Кейн обезрухлив Веріна й лише потім викликав риддерака. Ця тварюка любила пити гарячу кров. Тепер, без господаря, риддерак, швидше за все, спочатку її просто покалічить, щоб напитися крові, а потім…"
"У неї перехопило дихання. Смерть у кам’яному мішку? Ні, тільки не тут. Риддерак роздер її й повернеться в свій чудовищний світ, а її ніколи не знайдуть. Ніхто й на думку не візьме шукати її в підземеллях. Шаол буде губитися в здогадках і проклинати її за свавілля. Вона не зможе зізнатися Нехемії, що помилялася. А Еліана… в останньому своєму явленні Еліана повідомила: хтось хоче, щоб вона спустилася в склеп і побачила… побачила що?"
"Селені згадалися й інші слова давньої королеви, промовлені раніше: «Відповідь ти знайдеш праворуч». Що ж тут може перебувати праворуч? Тільки стіна. А якщо не тут?"
"Ну звичайно! Як вона раніше не здогадалася? Якщо спуститися нижче, на такій же площадці, праворуч, буде прохід у склеп Еліани й Гавіна."
"Риддерак знову присів навпочіпки, готуючись до стрибка. Замисел, миттєво народжений у голові Селени, був божевільним і відчайдушно хоробрим. Вона скинула заважливий плащ."
"З риком, від якого затремтіли стіни, риддерак кинувся до неї."
"Вона залишалася біля дверей, стежачи за рухами чудовиська. Із-під кігтів риддерака вилітали іскри. Не добігши трьох футів, риддерак стрибнув, наміряючись схопити її за ноги. І тоді Селена кинулася назустріч розкритий пащі, повній чорних гнилих зубів."
"Маневр вдався: вона стрибнула й перелетіла через голову риддерака, а той, не в силі зупинитися, вдарився в важкі двері. Слухаючи оглушливий тріск ламаючогося дерева й глухий стукіт падаючих уламків, Селена із завмиранням серця уявляла, у що могли б перетворитися її ноги."
"На якийсь час риддерак забув про неї. Він повернувся в приміщення й лихоманково обтрушувався. Цієї миті Селені вистачило, щоб через пролом вибратися в коридор і опинитися на сходах."
"Куди тепер? Угору? Навряд чи вона добереться живою до своєї спальні. А ось до склепу, якщо пощастить, добігти вдасться."
"Від рику риддерака тремтіли сходи. Селена бігла, не озираючись. Униз, униз, униз. Туди, де на площадку пробивалося місячне світло зі склепу."
"Опинившись там, Селена кинулася до дверей склепу, молячись усім богам, чиї імена давно забула. У ній теплилася надія, що боги не забули її."
"‘У ніч Самуїнна хтось привів мене в склеп. Хто — цього не знає навіть Еліана. Там я мушу щось побачити. Можливо, це щось врятує мені життя’."
"Риддерак її наздоганяв. Він був настільки близько, що Селена відчувала його смердюче дихання. Двері в склеп виявилися відчиненими навстіж. Невже хтось її тут чекав?"
"‘Допоможіть мені!’ — знову подумки взмолилася вона, звертаючись сама не знає до кого."
"Селена вбігла в склеп, вигравши кілька дорогоцінних секунд. Місячне світло збило риддерака з пантелику, і він забіг у сусіднє приміщення. Це принесло Селені ще кілька секунд. Але риддерак швидко наздоганяв втрачений час. Він улетів у склеп, вирвавши шматок дверей."
"Ноги самі несли Селену між надгробками, туди, де в місячному світлі блищало лезо Дамаріса. А адже коли вона вдруге, вже вдень, прийшла сюди, сподіваючись позичити ніж чи кинджал, склеп був порожній. Напевно, і Дамаріс з’являвся тут звідкись із інших світів. Головне, що зараз меч був на своєму місці й сяяв так, ніби його викували вчора, а не тисячу років тому."
"Риддерак заричав. Селена почула, як він шумно втягує повітря, готуючись до нападу. Кігті шкребли мармурову підлогу. Потім риддерак стрибнув. У Селени не було часу схопити меч правою рукою, і вона схопила Дамаріс лівою, розвернулася й махнула давньою зброєю."
"На мить перед нею майнули два бездонні чорні очі й сіра перетинчаста шкіра… Селена що є сили всаджувала лезо меча риддераку між очима."
"Від її удару вони обидва втратили рівновагу, влетіли в стіну й повалилися на підлогу, розкидаючи коштовності. Праву руку Селени обпік нестерпний біль. У обличчя їй бризнула смердюча чорна кров риддерака."
"Селена лежала нерухомо й тільки дивилася в очі чудовиська з іншого світу. Вони були зовсім близько, за кілька дюймів від її обличчя. Її права рука була затиснута між чорними зубами риддерака, і її кров — червона, людська кров — струменіла по його підборіддю. Селена важко дихала, усе ще стискаючи в лівій руці Дамаріс, і тільки дивилася. Через якийсь час чорні очі риддерака помутніли, і Селену притиснуло його обм’яклим тілом."
"Амулет на шиї знову ожив. Тепер усе залежало від послідовності й точності її дій. Це як танець, де не можна збитися ні в одному па, інакше… інакше вона ніколи не вибереться зі склепу."
"Перш за все Селена висвободила праву руку з пащі мертвого риддерака. Кистю пекло, наче рука побувала у вогні. Сильніше за все дісталося великому пальцю — він був увесь у точкових глибоких ранках, залишених чорними зубами. Після цього Селена скинула з себе труп чудовиська й, похитуючись, встала. Дивно, але мертвий риддерак виявився майже невагомим. Голова в неї кружилася, очі застилала туманна пелена. Який наступний крок? Треба витягти Дамаріс із голови риддерака."
"Селена відірвала лоскут від своєї нижньої сорочки й ретельно витерла лезо меча, після чого повернула зброю Гавіна на місце. Тепер зрозуміло, чому в ніч Самуїнна її привели сюди й показали Дамаріс. Показали й сховали до пори до часу. До того моменту, коли меч їй знадобиться для порятунку власного життя."
"Вона не стала витягати труп риддерака зі склепу, залишивши чудовисько лежати на купі коштовного каміння. Вона позбавила замок від зла. А прибиранням нехай займаються ті, хто кликав її сюди. З неї вистачить."
"Але щось усе ж змусило її зупинитися біля статуї Еліани."
"— Дякую, — хрипко промовила вона, дивлячись на прекрасне мармурове обличчя давньої королеви."
"Селена не пам’ятала, як вибралася зі склепу, як піднімалася сходами, притискаючи до грудей поранену руку. З останніх сил вона зачинила двері, опустила шпалеру й присунула комод. Кров не зупинялася й продовжувала капати на підлогу. Треба піти в умивальну й ретельно промити руку. Права долоня зовсім задубіла. Треба…"
"Її ноги підкосилися, і Селена повалилася на підлогу. Повіки відяжеліли, очі самі собою заплющилися. А чому її серце б’ється ледь-ледь?"
"Селена змусила себе розплющити очі. Зір по-старому залишався розмитим, і замість руки вона бачила змішання червоних і рожевих плям. Оцепеніння встигло поширитися по всьому тілу й дістатися ніг."
"Потім вона почула шум. Гучний, навіть дуже. Якесь незрозуміле «бум-бум-бум», що змінилося повискуванням. У кімнаті стало темніти."
"Селена очуняла від жіночого крику. Чиїсь теплі руки обхопили її обличчя. До цього часу її обличчя стало пекуче крижаним. Невже в спальні відчинили вікно?"
"— Ліліано, очнися! — Нехемія трясла її за плечі. — Ліліано? Що з тобою?"
"Усе, що відбувалося далі, Селена пам’ятала невиразно. Сильні руки підхопили її й понесли в умивальну. Нехемія розділа Селену й усадила в таз із гарячою водою. Ледь торкнувшись води, права рука відгукнулася спалахом болю. Селена поривалася вибратися назовні, але принцеса міцно тримала її, промовляючи слова незнайомою мовою. Світло в умивальній якось дивно пульсувало. Шкіру Селени кололо безліч крихітних голочок. Вона раптом побачила, що її руки вкриті сяючими бірюзовими «знаками долі». Нехемія не випускала її з води й повільно гойдала, як дитину."
"Далі Селена нічого не пам’ятала. Вона провалилася в темряву."
"Селена розплющила очі."
"Її тіло знову було звично теплим. Золотавими вогниками перемигувалися свічки. У повітрі пахло лотосом і злегка — мускатним горіхом. Селена шморгнула носом, кілька разів моргнула й спробувала встати. Що з нею було? Вона слабко пам’ятала, як добиралася сюди, як зачиняла потайні двері й опускала шпалеру."
"І де її блуза? Хто й коли встиг перевдягнути її в нічну сорочку? Але найбільше її здивувала власна права рука. Біль зник, і пальці вільно ворушаться. Про рани нагадував лише маленький вигнутий шрам між великим і вказівним пальцями й точки, що залишилися від нижніх зубів риддерака. Селена оглянула шрам, потім знову поворушила пальцями, бажаючи переконатися, що кистя повністю зберегла рухливість."
"Але хто ж її вилікував, та ще так швидко? Подібне можливо тільки за допомогою магії. Піднявши голову, Селена побачила, що в спальні вона не одна."
"Біля постелі сиділа Нехемія й дивилася на неї. Губи принцеси не усміхалися, а в очах чітко читалася недовіра. Біля ніг ейлуейки дрімала Швидконога."
"— Що сталося? — запитала Селена."
"— Я чекала, поки ти прокинешся, щоб поставити тобі те саме запитання, — ейлуейською відповіла принцеса. — Коли я тебе знайшла, жити тобі залишалося лічені хвилини. Якби я спізнилася, ти б померла від укусу."
"З підлоги були відмиті всі сліди крові."
"— Дякую тобі, — прошепотіла Селена, повертаючи голову до вікна, за яким темніло небо. — Який сьогодні день?"
"Невже вона пролежала два дні поспіль, тим самим проваливши останнє випробування?"
"— Ти проспала всього три години, — заспокоїла її Нехемія."
"Селена полегшено зітхнула. Значить, завтра вона може вправлятися цілий день. А післязавтра — випробування."
"— Я не розумію, як ти…"
"— Це не так важливо, — перебила її Нехемія. — Мені важливіше знати, де ти отримала цей укус? Сліди крові були тільки в твоїй спальні. Ні в коридорі, ні в інших кімнатах їх не було."
"Селена стискала й розтискала пальці правої руки, дивлячись, як розтягуються й стискаються шрами. Вона була на межі смерті! Селена подивилася на принцесу, потім знову на свою руку. Що б Нехемія ні замишляла, в змові з Кейном вона явно не була."
"— Я не та, за кого себе видавала, — тихо сказала Селена, не наважуючись дивитися подрузі в очі. — Жодної Ліліани Гордени немає й не було."
"Нехемія мовчала. Селена змусила себе повернутися до неї. Принцеса врятувала їй життя. Як у її голові могла виникнути дурна думка, що Нехемія керує риддераком? Найменше, чим вона могла заплатити ейлуейці за своє порятунок, — це розповісти правду."
"— Моє справжнє ім’я — Селена Сардотін."
"Принцеса розкрила рот і недовіриво похитала головою."
"— Але ж тебе заслали в Ендов’єр. Ти перебувала там… — Очі Нехемії округлилися. — Тож ось де ти навчилася нашому простонародному діалекту! Я знаю: в Ендов’єрі томиться багато ейлуейських селян."
"У Нехемії затремтіли губи."
"— Тебе відправили… тебе заслали в Ендов’єр? Але це ж каторга… місце смерті. Звідти не повертаються. Чому… чому ти мені не розповіла? Ти мені не довіряєш?"
"— Довіряю, — зітхнула Селена."
"Нехемія наочно довела свою непричетність до вбивств претендентів."
"— Король суворо наказав мені мовчати."
"— Король? — здивувалася Нехемія. — Тож він знає, що ти тут? І він віддає тобі накази?"
"Селена випросталася й відповіла:"
"— Король, звичайно, знає, бо я тут за його примхою. Це ж він влаштував дурні змагання за титул королівського захисника. Коли я переможу… якщо переможу… я ще цілих чотири роки мушу прослужити королівським асасином, убиваючи за його наказом. Тільки після цього я отримаю свободу, і з мене знімуть усі обвинувачення."
"Нехемія ошеломлено дивилася на неї."
"— Думаєш, я рада своєму життю в замку? — вигукнула Селена, відчуваючи, як у неї застукало у скронях. — Вибір у мене був невеликий: або погоджуватися на участь у змаганнях, або гнити в Ендов’єрі. Я пережила там минулу зиму, але сумніваюся, що пережила б ще й цю."
"Нехемія мовчала, і Селені в її очах примарився докір."
"— Перш ніж ти наговориш мені правильних слів чи втечеш звідси й сховаєшся за своїх телохранителів, знай: навіть перемога в змаганнях не заслоняє від мене майбутнього. Я щодня мучуся думками. Думаю, як мені буде вбивати за наказом короля… за наказом того, хто знищив усе, що я любила!"
"Селені стало важко дихати. Двері в заборонене сховище пам’яті то й діло відчинялися, і звідти виривалися картини минулого, про яке їй хотілося забути назавжди. Селена знову й знову зачиняла ці двері. Вона мріяла забитися зараз під ковдру, сховатися в темряву. Нехемія мовчала. Швидконога поскулювала. Перед подумним зором Селени майоріли обличчя, місця, події, а її вуха чули давно забуті, заборонені слова."
"Кроки повернули Селену до дійсності. Постіль скрипнула. Це Нехемія сіла до неї на ковдру. Ще поштовх — на постіль забралася Швидконога."
"Нехемія обережно взяла руку Селени в свою теплу, суху долоню. Селена розплющила очі, однак дивилася не на принцесу, а на протилежну стіну."
"— Селено, ти моя найдорожча й найближча подруга, — сказала Нехемія, стискаючи її руку. — Уявляєш, як боляче мене вдарило, коли ти раптом стала холодною зі мною. Я не могла зрозуміти, чим викликане твоє раптове недовір’я до мене. Твій погляд ранив мене сильніше, ніж меч. Я дуже не хочу… я просто боюся коли-небудь знову побачити цей погляд. І тому я маю намір подарувати тобі те, що дарувала дуже небагатьом."
"Темні очі принцеси спалахнули."
"— Самі по собі імена нічого не значать, — продовжила вона. — Важливо те, що в тебе всередині. Я знаю, через які муки ти пройшла в Ендов’єрі. Твоя доля була не легшою за долю моїх співвітчизників. І так — день за днем. Але соляні копальні не перетворили твоє серце на камінь і не озлобили твою душу."
"Принцеса начертила в себе на долоні якийсь знак і стиснула руку Селени."
"— У тебе багато імен. Я дам тобі ще одне."
"Рука Нехемії торкнулася чола Селени й начертила той самий знак."
"— Я нарікаю тебе Елентією, — сказала принцеса, цілуючи її в лоб. — Носи це ім’я з честю й згадуй про нього, коли інші імена стають занадто важкими. У перекладі з давньої мови «Елентія» означає «дух, який неможливо зламати»."
"Селена здивовано мотала головою. Нове ім’я огорнуло її сяючим покривалом. Це ім’я було пронизане безмежною любов’ю. Досі вона думала, що друзі, подібні до Нехемії, існують лише в уяві романістів. Чому ж доля посміхнулася їй, зробивши такий подарунок у реальному житті?"
"Нехемія усміхалася."
"— А тепер розкажи мені, як ти стала Адарланським асасином, за що потрапила в Ендов’єр, як вирвалася звідти й чим займалася в замку. І звичайно, розкажи мені про це безглузде змагання."
"Селена теж усміхнулася. Швидконога усміхатися не вміла, а тому просто лизала руку Нехемії."
"Їй врятували життя. Яким чином — про це вона дізнається потім. Нехемія мала право знати про неї все… чи майже все. І Селена почала розповідати."
"Селена йшла поруч із Шаолом, дивлячись собі під ноги. За вікнами під ранковим сонцем осліпливо іскрився сніг, від чого в коридорі було неймовірно світло. Як не дивно, після безсонної ночі Селена не відчувала себе втомленою. Вона розповіла принцесі дуже, дуже багато, однак промовчала про деякі сторони свого минулого. Обережність, що стала її другою натурою, змусила Селену промовчати про Кейна й битву з риддераком. Нехемія більше не запитувала, хто покусав їй руку. Принцеса лежала поруч із нею. Вони говорили й не могли наговоритися. Знаючи про можливості Кейна, Селена взагалі сумнівалася, що зможе тепер спати вночі, і товариство принцеси було як ніколи до речі."
"Яскраве сонце анітрохи не наповнювало коридор теплом, і Селена щільніше закуталася в плащ."
"— Щось ти сьогодні тиха, — сказав Шаол, дивлячись не на Селену, а перед собою. — Невже з Доріаном посварилася?"
"Доріан. Принц учора намагався завдати їй візиту, але Нехемія випровадила його, не пустивши до спальні."
"— Не вгадав. Доріана я не бачила з учорашнього ранку."
"Після нічних подій учорашній ранок здавався ранком тижневої давнини."
"— Напевно, рада, що вдосталь натанцювалася з ним на балу?"
"Запитання було цілком невинним, але Селена вловила в ньому ревнощі."
"Коридор розгалужувався, і вони звернули ліворуч, прямуючи не в загальну залу, а в непомітну кімнатку, де зазвичай вправлялися."
"— З ким же ще мені було танцювати? — усміхнулася Селена, намагаючись обернути це в жарт. — Ти пішов рано. А я-то думала, ти станеш стерегти мене до самого кінця балу."
"— Стерегти тебе? Тепер це зайве."
"— Це було зайве з самого початку."
"— Зараз я знаю, що ти нікуди не втечеш, — знизуючи плечима, сказав Шаол."
"За вікнами завивав вітер, здіймаючи райдужну сніжну пил."
"— Чому ж нікуди? Ти забув про Ендов’єр."
"— Ти не повернешся в Ендов’єр."
"— Звідки ти знаєш?"
"— Знаю, і все."
"— Це додає мені цілу гору впевненості."
"Капітан лише усміхнувся:"
"— Дивно, як це твоя собака не причепилася до тебе. Вона так скавчала, навіть смішно."
"— Якби в тебе була собака, тобі б не було смішно, — похмуро відгукнулася Селена."
"— Я завжди чудово обходився без домашніх тварин. Навіть у дитинстві не просив їх у батьків."
"— Тоді я бажаю тобі знайти супутника хоча б в образі собаки!"
"Шаол штовхнув її ліктем. Селена засміялася й відповіла тим самим. Їй було дуже приємно нарешті почути його сміх."
"Підійшовши до місця, де коридори сходилися в один, вони здивувалися незвичайному скупченню гвардійців. І майже одразу Селена побачила його… адарланського короля."

#Епізод 23

"Король. Селена відчула, як її серце видало беззвучний крик і шмигнуло в п’яти. Зануло всі свіжі шрами на правій руці. Король рухався прямо на них із Шаолом, і від його громіздкої постаті просторий коридор став тісним. Звичайно, король їх помітив. Селена спітніла й одразу відчула озноб. Шаол зупинився й низько вклонився королеві."
"Селені зовсім не посміхалося гойдатися на шибениці, тому вона теж низько вклонилася. Король пронизав її сталевим поглядом. У Селени волосся стало дибки. Очі короля свердлили її, намагаючись проникнути в найпотаємніші глибини. Король знав: у його замку щось не так, за час його відсутності щось змінилося, і причини змін пов’язані з нею."
"Шаол і Селена майже вдавилися в стіну, пропускаючи короля й гвардійців."
"Проходячи повз, король не спускав із неї очей. Але чи бачив він те, що в неї всередині? Чи знав він про здатність Кейна відкривати портали між світами? Справжні портали. Чи знав король, що всупереч його вигнанню магії «знаки долі» по-старому володіють магічною силою? Неймовірною силою. І король міг би спрямувати її на свої страшні задуми, навчившись викликати демонів на кшталт вчорашнього риддерака…"
"Від очей короля віяло чимось чужим і холодним. Вони були схожі на дві міжзоряні безодні. Чи здатна ця людина знищити весь світ? Невже жага влади, що пожирає його, настільки безмежна? Селена дивилася на короля, і їй чувся гул і гуркіт битв."
"Навколо цієї людини витала небезпека. Запах смерті, який вона відчула вчора, коли опинилася перед чорною порожнечею, викликаною Кейном. Навіть не запах, а сморід іншого світу, світу мертвих. І навіщо Еліані знадобилося, щоб Селена стала однією з головних наближених адарланського короля?"
"Король пройшов далі. До Селени повернулася здатність рухатися. Глянути на Шаола вона не наважувалася, хоча й відчувала, що капітан уважно стежить за нею. Дякувати, що мовчки."
"Увесь залишений шлях до своїх покоїв Селена йшла, майже торкаючись Шаола плечем. Капітан мовчав і з цього приводу."
"Провівши Селену, Шаол повернувся до себе. Її після відпочинку чекали вправи в загальній залі. Що чекало його самого, капітан не знав. Перекусивши з Селеною, Шаол відправився читати звіт про королівську подорож. За десять хвилин він тричі прочитав його й тепер м’яв у руках пергамент. Обтічні фрази й нічого по суті. Чому король повернувся один? І, що незрівнянно важливіше, чому загинули всі його супроводжуючі? Зазвичай у таких випадках детально писали: хто з солдатів коли загинув і за яких обставин. Так само туманно в звіті говорилося й про те, в які місця їздив його величність. Білоклицькі гори — занадто обширний край, і королеві просто не вистачило б часу побувати там скрізь… І все-таки чому він повернувся один?"
"Король побіжно повідомляв про якихось повстанців, яким вдалося отруїти їстівні припаси його загону. І знову туман. Виходило, що всі, хто супроводжував короля, отруїлися й померли, а він дивом залишився живим. Надмірна неясність залишала широке поле для всіляких здогадок і домислів. Швидше за все, солдати, що супроводжували короля, загинули за зовсім інших обставин. А чого варта, наприклад, ця фраза: «Я не хочу вдаватися в сумні подробиці, аби не засмучувати моїх підданих»? Можливо, придворним і не обов’язково знати всі подробиці. Але Шаол — як-не-як капітан королівської гвардії. Якщо король йому не довіряє…"
"Бідна Селена. Бачила б вона себе збоку, коли вони натрапили на раптово поверненого короля. Переляканий звірятко, та й годі. Шаолу навіть захотілося обнадійливо поплескати її по спині. Селену просто вибило з колії. Такою він бачив її тільки в день королівської аудієнції для претендентів."
"За ці місяці Селена досягла вражаючих успіхів. Тепер уже не їй, а йому доводилося за нею встигати. Вона з легкістю лазила по стінах і одного разу, демонструючи свої навички, без жодних мотузок і смоли забралася до себе на балкон. Успіхи Селени радували й водночас лякали Шаола. Вона стверджувала, що ще не увійшла в колишню силу. Якою ж тоді вона була перед Ендов’єром? Під час їхніх поєдинків вона атакувала не вагаючись, але інколи він відчував, що вправляється не з нею, а з її оболонкою. Селена вислизала в себе всередину, де часом було спокійно й прохолодно, а часом гамірно й гаряче. Шаол не сумнівався: вона здатна за лічені секунди вбити будь-кого, включно з Кейном."
"Але якщо вона переможе в заключному поєдинку й стане королівською захисницею, чи небезпечно буде відпускати її з дорученнями саму? А як інакше? У асасинів не буває супроводжуючих. І потім, Селена навряд чи наважиться грати з королем у ризиковану гру. На ці чотири роки невидимі ланцюги прикують її до замка."
"Цікаво, про що король подумав, побачивши їх обох сміючимися? Але навіть якщо йому це не сподобалося, їхній сміх ще не привід, щоб тримати свого капітана в невіданні про причини й обставини загибелі загону. Королю взагалі байдуже до чужого настрою. І потім, вони ж сміялися не на офіційній церемонії."
"Шаол поскріб плече, подряпане Селеною під час їхнього ранкового поєдинку. Він згадав, як вона стиснулася, побачивши короля. Навіть стала меншою на зріст."
"Зовні король анітрохи не змінився. Та й у поводженні — теж. Він і раніше був грубим із Шаолом. Але до минулої осені його дії були більш-менш пояснюваними. І раптом — раптовий від’їзд із невеликим загоном, повна відсутність звісток, а тепер — таке ж раптове повернення в повній самотності. І розпливчастий звіт, складений формальності заради… Схоже, десь кипів казан нових королівських задумів, і король навідався туди, аби підкинути дров і помішати своє вариво. Селена це теж відчула."
"Капітан королівської гвардії притулився до стіни, дивлячись у стелю. Він не вправі втручатися в королівські справи. Зараз йому треба зосередитися на розгадці причин звірячих убивств претендентів і зробити все можливе, щоб Селена вийшла переможницею. І справа тут не в амбіціях Доріана. Селені не можна повертатися в Ендов’єр. Вона там не виживе."
"Скільки ця дівчина встигла накоїти за якихось три з гаком місяці життя в замку! Шаол уявив, які сюрпризи вона піднесе їм за чотири роки, і усміхнувся."
"Важко дихаючи, Селена й Нокс опустили мечі. Головний королівський зброяр крикнув п’ятьом претендентам, що їм дозволено підійти до столу, де стояли глечики з водою. Завтра — останнє випробування. Селена старалася триматися подалі від Кейна й, коли той попрямував до дальнього кінця столу, стежила за кожним його рухом. Оцінювала м’язи, зріст, розворот плечей. Усе це було наслідком сили, викраденої ним у вбитих претендентів. А чорне кільце на його пальці — воно теж якимось чином пов’язане з його жахливими здібностями?"
"— У тебе щось сталося? — запитав Нокс, підходячи до неї."
"Кейн, Могила й Ренальт, ставши в гурток, шумно пили воду й перемовлялися."
"— Ти сьогодні трохи… ну, як би не тут, — пояснив Нокс."
"Де, в кого навчився Кейн викликати риддерака й що це за чорна порожнеча, з якої той виліз? Перемогти в змаганнях — єдина мета Кейна? Чи риддерак був йому потрібен ще для якихось гидотних справ?"
"— Ти й зараз про щось думаєш. Про що? — не відставав Нокс."
"Зусиллям волі Селена змусила себе не думати про Кейна."
"— Ти щось питав?"
"Нокс дурнувато усміхався."
"— Тепер я розумію, чому ти не тут. Напевно, в думках ти по-старому на тому балу й насолоджуєшся увагою принца."
"— Не твоя справа, — огризнулася Селена."
"— Пробач, я це так. Звичайно, не моя, — погодився Нокс, примирливо піднявши руки."
"Селена мовчки підійшла до столу, взяла глечик, налила собі кружку, не наливши другу для Нокса."
"— А шрами на твоїй правій руці зовсім свіжі. Звідки? — нахилившись до неї, запитав цікавий злодій."
"Селена сховала руку в кишеню."
"— Не твоя справа, — повторила вона, сердито подивившись на Нокса."
"Його така відповідь не влаштувала. Він схопив Селену за руку й прошепотів:"
"— Пам’ятаєш, ти прислала мені записку з попередженням, щоб я нікуди не виходив? А твої шрами дуже схожі на сліди укусів. Кажуть, Веріна й Ксав’єра роздер якийсь звір… Ти ж щось знаєш, — додав він, примружуючи сірі очі."
"Селена озирнулася на Кейна. Той як ні в чому не бувало перекидався жартами з Могилою."
"— Нас залишилося всього п’ятеро, — сказала вона. — А завтра, коли закінчиться останнє випробування, буде четверо. Загибель Веріна й Ксав’єра ніяка не випадковість. Якщо пам’ятаєш, їх обох убили за два дні до випробування."
"Селена висмикнула руку."
"— Будь обережний, — сердитим шепотом додала вона."
"— Розкажи мені все, що знаєш, — зажадав Нокс."
"‘Розкажи тобі все, і ти одразу назвеш мене божевільною’, — подумала Селена."
"— Ось що я тобі скажу. Якщо ти ще не розучився міркувати, забирайся із замка, і якомога швидше."
"— Чому? — здивувався Нокс і покосився в бік Кейна. — Про що ти?"
"Брулло допив воду й пішов туди, де залишив меч. Це означало кінець перерви й відновлення занять."
"— Я ось про що. Будь у мене інший вибір… якби мені не довелося вибирати: або ці змагання, або смерть… я б утекла звідси без оглядки й, швидше за все, була б уже на іншому краю Ерілеї."
"— Знову нічого не розумію, — зізнався Нокс, розтираючи затерплу шию. — Чому в тебе немає вибору? Я знаю, у тебе з твоїм батьком нелады, але ж він…"
"Селена виразно подивилася на нього."
"— Значить, ти — зовсім не викрадачка коштовностей? — раптом запитав Нокс."
"Вона похитала головою. Нокс знову глянув у бік Кейна."
"— Кейн це теж знає? Тому він весь час і намагається тебе піддати, щоб ти показала, хто ти є насправді?"
"Селена кивнула. Що особливого, якщо Нокс про це дізнається? У неї зараз є турботи поважніші. Наприклад, як дожити до завершального поєдинку. Чи як зупинити Кейна."
"— Але тоді хто ти? — не міг заспокоїтися Нокс."
"Селена прикусила нижню губу."
"— Ти казала, батько відправив тебе в Ендов’єр. А потім принц поїхав туди за тобою й привіз у замок."
"Кажучи це, Нокс раптом глянув на її спину. Ось вони, свідчення. Злодій не дурень, зуміє скласти головоломку."
"— Розумію, — ошеломлено прошепотів Нокс. — Ти була в Ендов’єрі, але не в тому. На каторзі. На соляних копальнях. Тому ти й була схожа на жердь, коли я вперше тебе побачив."
"Брулло гаркнув на них, вимагаючи закінчити балаканину й відновити вправи."
"Нокс і Селена залишалися біля столу. Очі злодія округлилися. Він здогадався!"
"— Тож ти була… рабинею в Ендов’єрі?"
"Відпиратися марно. Нокс достатньо кмітливий хлопець. Селена кивнула."
"— Стривай. Але ти ж зовсім дівчинка. Що ж ти встигла накоїти, якщо…"
"Нокс помітив стоячих неподалік Шаола й кількох вартових, але своїх розпитувань не припинив."
"— А я десь чув твоє справжнє ім’я? Я мусив його чути."
"— Так. Коли мене туди заслали, моє ім’я знали всі."
"Селена бачила, як перрантський злодій морщить лоба, перебираючи в пам’яті всі імена, так чи інакше пов’язані з Ендов’єром. Потім він зрозумів. Жахнувся. Відсунувся від неї."
"— Невже це ти?"
"— Уяви собі. Усі дивуються. Чомусь люди думають, що я набагато старша."
"Нокс провів рукою по злиплих темному волоссю."
"— Значить, тобі або ставати королівською захисницею, або — назад в Ендов’єр?"
"— Так. Тому я й не можу втекти із замка."
"Брулло гаркнув на них, і вони попленталися в свій кут. Селена впіймала суворий погляд Шаола. Напевно потім буде розпитувати."
"— Селено, зроби мені послугу, — попросив Нокс."
"Їй було дуже дивно почути своє ім’я з його уст."
"— Відірви Кейну голову, — прошепотів він, нахилившись до її вуха."
"Сказавши це, Нокс зловтішно усміхнувся. Селена відповіла йому такою ж усмішкою й кивнула."
"Ранньою вечірньою порою, не сказавши нікому ні слова, Нокс покинув замок."
"Годинник пробив п’ять. Кальтена відчайдушно боролася з бажанням повернути назад, лягти в постіль і заснути. Їй здавалося, що опіум скупчився в неї всередині й тепер струменить з усіх пор. Захід сонця забарвлював коридори замка в червоні, помаранчеві й золотаві тони, змішуючи їх у найнеймовірніших поєднаннях. Перангон попросив її бути сьогодні на обіді у Великій залі. Знаючи, що їй доведеться вирушити в людне місце, вона б не дозволила собі курити опіум. Але проклятий головний біль, що дошкуляв їй з ранку, ставав усе нестерпнішим."
"Коридор, по якому вона брела, здавався таким, що йде в нескінченність. Кальтена старалася не помічати тих, що траплялися їй по дорозі придворних і слуг, і дивилася тільки на гру сонячних плям. Але назустріч їй, підминаючи собою золотаві й помаранчеві відблиски, рухалося щось чорне, схоже на стовп. Стовп злегка погойдувався, розбризкуючи тіні, і вони осідали на вікнах, стінах і стелі, наче краплі чорнила."
"Кальтена хотіла прочистити горло, але виявила, що її язик налився свинцевою важкістю й став зовсім сухим."
"З кожною секундою стовп ставав усе більшим і вищим. У вухах Кальтени стукало, але це були не молотки головного болю, а стукіт її серця. Звичайно, це все через опіум. Вона перевищила свою звичайну порцію й зробила більше затяжок, ніж належало. До стукоту серця приєднався інший звук — шелест крил."
"Чорний стовп виявився Кейном. Кальтена могла поклястися, що бачила — хай лише мить, — але бачила якихось страховищ, що кружляли над ним. Їй здалося, ніби вони чогось чекають. Чекають. Чекають…"
"— Моє шанування, пані Кальтено, — уклонившись, промовив Кейн і пройшов повз."
"Вона не відповіла. Стиснувши спітнілі долоні, попленталася далі. Поступово хлопання крил стихло, а до того моменту, коли Кальтена вмостилася поруч із герцогом за столом, зустріч у коридорі начисто вивітрилася з її пам’яті."
"Селена коротала вечір, граючи в шахи з Доріаном. Згадуючи, як вони цілувалися після балу, вона думала, що це було не таким уже поганим заняттям. Дуже навіть хорошим, якби Селена не лукавила з собою. Але сьогодні принц і словом не обмовився про ті поцілунки. Не запитав він і про шрами на правій руці, а якби й запитав, вона б нізащо не розповіла йому про риддерака. Ні зараз, ні навіть через мільйон років. При всіх симпатіях до Доріана Селена пам’ятала, чий він син. Якщо принц розповість батькові про «знаки долі» й Врата Вэрда… При одній цій думці в неї крижаніла кров."
"Так, вона пам’ятала, чий він син. Однак зараз, дивлячись на обличчя Доріана в відблисках камінного полум’я, вона не знаходила в принці й найменшої схожості з батьком. Він добрий і розумний. Можливо, трохи зарозумілий… Швидконога ткнулася їй у щиколотку, і Селена пальцем ноги почухала цуценя за вухом."
"Їй здавалося, що, скуштувавши її, принц швидко охолоне до неї й захопиться якоюсь новою жінкою."
"‘Ну що ти вигадуєш? — подумки обірвала себе Селена. — Чверть години поцілунків — яке ж це «скуштування»?’"
"Доріан пересунув свою королеву."
"— Ви впевнені, що це правильний хід? — запитала Селена й засміялася."
"Принц знизав плечима. Тоді Селена посунула свою пішака по діагоналі й легко взяла його королеву."
"— Чорт! — крикнув Доріан і з досади по-хлоп’ячому тупнув."
"— Будемо вважати, що ви не подумали, — сказала Селена, подаючи йому фігуру. — Поставте її на місце й оберіть інший хід."
"— Ні. Я граю як чоловік і приймаю поразку!"
"Вони обидва засміялися, але сміх швидко стих. Селена ще продовжувала усміхатися, коли принц потягнувся до її руки. Вона хотіла відсмикнути руку, але не могла себе змусити. Доріан поклав її долоню на стіл і прикрив своєю рукою. Їхні пальці переплелися. Його долоня була мозолистою й сильною. Селена не виривалася. Вона просто не знала, як учинити."
"— У шахи грають обома руками, — нарешті сказала вона, боячись, чи не вибухне в неї серце."
"Швидконога, відчувши, що краще не заважати господині, ретирувалася під ліжко."
"— Шахи — не клавікорди, — усміхнувся принц. — Мені для гри вистачає й однієї руки. Бачиш? — запитав він, рухаючи фігуру."
"Селена прикусила губу. Її долоня по-старому залишалася в полоні його долоні."
"— Ви знову хочете мене поцілувати? — запитала вона."
"— Так, — коротко відповів принц і потягнувся до неї."
"Доріан був усе ближче. Він навалився на стіл, підминаючи шахові фігури. Його губи завмерли зовсім поруч із її губами."
"— А я сьогодні в коридорі натрапила на вашого батька, — випалила Селена."
"Доріан повільно опустився на стілець."
"— І що?"
"— І нічого, — збрехала Селена. — Вклонилася йому й пішла далі."
"Принц примружився. Потім пальцем торкнувся її підборіддя."
"— Сподіваюся, ти розповіла про це не для того, щоб уникнути неминучого?"
"Ні. Їй просто хотілося, щоб принц засидівся тут довше. Краще, якщо до ранку, щоб не залишатися самій у цю ніч. Від Кейна можна чекати чого завгодно. І хто краще захистить її в нічні години, ніж спадковий принц? Коли він тут, Кейн не наважиться напасти."
"Її думки повернулися до риддерака. Значить, усе, що вона прочитала в тій книзі, — правда? І підтвердження страшної правди — на її долоні. І значить, Кейн здатен викликати істот з інших світів. Можливо, і зі світу мертвих теж. Зникнення магії розорило багатьох, тому знайшлося б немало охочих узяти Кейна до себе на службу. Та й сам король явно зацікавився б його здібностями."
"— Ти тремтиш, — сказав Доріан."
"Вона тремтіла. Тремтіла, як остання дурниця."
"— Може, ти застудилася?"
"Доріан підсунув стілець і сів поруч із нею."
"Ні, вона не могла йому розповісти про це. Принц не повинен знати, що не далі як сьогодні, заглянувши в пошуках Швидконого під ліжко, вона знову виявила там намальовані крейдою «знаки долі». І знову вона відскрібала їх, не розуміючи, хто й коли встиг пробратися в її покої й начертити зловісні знаки. Якщо це Кейн… виходить, йому теж відомий її потайний коридор? Тепер, коли його таємниця розкрита, він особливо небезпечний. Що він замислить? З’явиться сьогодні вночі? Чи затаїться? Одне Селена знала напевно: спокійний сон у неї почнеться не раніше, ніж її меч увонзиться йому в серце."
"— Селено, я питаю: ти не застудилася?"
"— Ні, просто трохи втомилася, — пошепки збрехала Селена."
"Вона боялася наполегливих розпитувань принца. Раптом щось у ній на мить втратить пильність, і вона все-таки розповість йому?"
"— Ти впевнена, що… — почав Доріан, але Селена потягнулася до нього й заглушила слова поцілунком."
"Вона ледь не штовхнула принца на підлогу. Вхопившись однією рукою за стілець, принц зумів утриматися. Другою рукою він обійняв Селену за талію. Його дотики, смак його губ заповнили її розум, вимиваючи звідти всі інші думки й страхи. Селена цілувала його, щоб до кінця розчинитися в цьому потоці. Ймовірно, Доріан хотів того ж, бо він цілував її з таким же шаленством."
"Пробило третю годину ночі. Селена сиділа в постелі, підтягнувши коліна до підборіддя. Після кількох годин поцілунків, що перемежовувалися розмовами, і розмов, що перемежовувалися поцілунками, Доріан побажав їй спокійної ночі й пішов. Їй так хотілося попросити його залишитися. Мабуть, зараз це було б найрозсудливішим і найздоровішим рішенням. Але якщо сюди увірветься Кейн чи ще один риддерак і через неї постраждає Доріан? Думки про безпеку принца переважили, і Селена, теж побажавши йому спокійної ночі, залишилася сама."
"Вона занадто втомилася, щоб читати, але перезбуджений мозок і страх не дозволяли їй заснути. Залишалося просто сидіти й дивитися на полум’я догораючого каміна. Кожен шурхіт, кожен звук, що долинав із коридору, змушував її насторожуватися й вихоплювати з-під подушки новий саморобний ніж. Його Селена теж спорудила зі шпильок, поцупивши кілька штук у зазеваної Фаліпи."
"Але якщо до неї вломиться риддерак чи інше чудовисько, викликане Кейном, його не зупиниш ні ножем, ні важкою книгою, ні підсвічником."
"‘Даремно я не взяла з склепу Дамаріс’, — пошкодувала Селена."
"Можливість була втрачена, а йти за мечем знову… ні, поки Кейн живий, вона туди не піде. Селені згадалася темрява, звідки з’явився риддерак. Одне спогад кинуло її в дрож, і вона покріпше обхопила коліна."
"Мабуть, Кейн дізнався про силу «знаків долі» в себе на батьківщині — в Білоклицьких горах. Прокляті ці гори служили природним кордоном між Адарланом і Західним краєм, куди поки ще не дотягнулася владна рука адарланського короля. Поголосували, що в руїнах Королівства Відьом і по сьогодні таїться зло, могильною змією виповзаючи звідти. І на гірських стежках трапляється-трапляється зустріти стареньких із залізними зубами."
"Озноб не минав. Селена щільно закуталася в тепле хутряне ковдру. Якщо вона доживе до парних поєдинків і завершальної дуелі, вона неодмінно переможе Кейна, і тоді з одним злом буде покінчено. Тоді вона знову міцно спатиме вночі… якщо тільки в Еліани не з’явиться якийсь новий, грандіозніший замисел."
"Селена притулилася щокою до коліна й дивилася на перемигуючі вугілля."
"Вершник знову й знову хльостав коня, змушуючи його скакати швидше. Кінські копита вдаряли по розмоклій землі, грузнучи то в снігу, то в глині. Снігопад припинився, і в нічному повітрі кружляли лише окремі запізнілі сніжинки."
"Селена бігла. Бігла швидше, ніж могли витримати її дитячі ноги. У неї боліло все тіло. Голі гілки дерев чіплялися їй за одяг і волосся, камені впивалися в ноги. Вона продиралася крізь колючі кущі, ловлячи повітря широко розкритим ротом. Кричати вона вже не могла. Та й хто почує її крики тут, у лісі? Зараз головне — дістатися до мосту й перебіжати на інший бік. У цьому її порятунок. Демону міст не перетнути."
"За спиною почувся лязкіт меча, що вихоплюють із піхов."
"Селена посковзнулася й упала в грязь, ударившись об камінь. Демон її наздоганяв. Копита його коня гуркотіли десь зовсім близько. Селена намагалася встати, але в’язка глина її не відпускала. Селена вчепилася за найближчий кущ, обдираючи руки в кров. Демон був майже поруч, і тоді вона…"
"Селена застогнала й прокинулася. Її рука була притиснута до грудей. Серце калатало. Але це був усього-навсього сон."
"У кружеві попелу гасли останні вугілля. Крізь портьєри пробивалося сутінкове світло раннього ранку. Сон. Усього лише сон. Звичайний нічний кошмар. Вона все-таки заснула, але такий сон був гірший безсоння. Селена схопилася за амулет на шиї, уперши великий палець у його середину."
"‘Напевно, це ти мене захистив від риддерака’."
"Амулет мовчав. Селена укутала в ковдру міцно сплячу Швидконогу. Ось і світанок. Вона пережила цю ніч."
"Селена лягла й заплющила очі."
"Через кілька годин, коли стало відомо про зникнення Нокса, Селену повідомили, що сьогоднішнє випробування скасовується. Завтра відбудуться парні дуелі, де її суперниками будуть Могила, Ренальт і, звичайно, Кейн."
"Завтра — вирішальний день, від якого залежить її свобода."

#Епізод 24

"У лісі було морозно й тихо. Кінь Доріана ступав м’яко, і все одно з дерев злітали пухнасті пласти снігу. Принц вдивлявся в візерунки гілок, ніде не затримуючи погляду більше ніж на мить. Йому сьогодні обов’язково треба було вирватися на полювання — не стільки заради здобичі, скільки щоб просто освіжитися холодним повітрям."
"Але варто йому було заплющити очі, як перед ним одразу з’являлася Селена. Нею були наповнені всі думки принца. Йому хотілося на її честь творити великі й дивовижні справи. Йому хотілося стати чоловіком, гідним королівської корони."
"Що відчувала сама Селена — цього Доріан не знав. Так, уночі вона пристрасно й шалено цілувала його, однак точно так само поводилися всі жінки, яких він любив. І вони теж цілували його пристрасно й шалено. І все ж між ними й Селеною була одна суттєва відмінність. Ті жінки дивилися на нього з обожнюванням. Селена дивилася на нього, як кішка, що спостерігає за мишею."
"Почувши шелест у гілках, Доріан напружився й завмер. За десять ярдів від себе він побачив рослого оленя-самця, що обдирав кору. Доріан зупинив коня й навпомацки дістав із сагайдака стрілу. Потім опустив лук."
"Завтра — день поєдинків."
"Якщо її покалічать… Але чому її мусять покалічити? Вона вміє постояти за себе, а ці місяці зробили її набагато сильнішою. Вона спритна, швидко міркує. Це він зайшов занадто далеко. Йому взагалі не можна було її цілувати. Після неї Доріану не хотілося будувати своє майбутнє ні з якою іншою жінкою. Він не уявляв і не бажав уявляти поруч із собою когось іще. Тільки її."
"У мовчазному лісі непомітно пішов сніг. Доріан подивився на сірі небеса й повернув коня до замка."
"Селена стояла біля балконних дверей і дивилася на розстелений унизу Рафтхол. Покриті снігом дахи будинків, золотаві вогники у вікнах. Майже казкове місто, якщо не знати, скільки зла й бруду ховають тихі вулички й затишні доми. І головне зло виходило від самого короля. Селена сподівалася, що Нокс уже далеко звідси. Вона попросила вартових нікого до неї не пускати. Навіть Шаола й Доріана. Втім, її й не турбували. Тільки одного разу хтось постукав. Селена не відповіла."
"Вона притиснула руку до скла, насолоджуючись пекучим холодом. Годинник пробив північ."
"Завтра… ні, вже сьогодні вона зійдеться в поєдинку з Кейном. Вони жодного разу не зустрічалися в навчальних поєдинках. Брулло не ставив їх у пару, а сама вона, на відміну від багатьох претендентів, не рвалася вправлятися з улюбленцем герцога Перангона. Кейн вирізнявся силою, але програвав їй у швидкості й спритності. Однак Кейн був дуже витривалим, і їй доведеться попітніти, ухиляючись від його атак. Селена лише сподівалася, що Шаол не дарма ганяв її до знемоги, змушуючи бігати щоранку, і зараз вона набагато витриваліша, ніж восени. Але якщо вона програє…"
"‘Не смій ні секунди думати про програш!’ — наказала вона собі."
"Селена притулилася до скла лобом. Напевно, краще загинути в поєдинку, ніж повертатися в Ендов’єр. А що почесніше: бути вбитою противником чи стати королівською захисницею? Кого їй доведеться вбивати, виконуючи королівські накази?"
"Будучи Адарланським асасином, Селена могла ставити умови. Нехай Аробінн цілком керував її життям, але вона завжди виговаривала собі умови. Жодних дитовбивств і жодної жертви родом із Террасена. Але король — не Аробінн, і він може наказати їй убити кого завгодно. Невже Еліана сподівалася, що Селена, отримавши титул королівської захисниці, зможе заперечувати королеві? Від цих думок до горла підступала нудота. Зараз не час думати про королівські накази. Зараз усі її думки мусять зосередитися на поєдинку з Кейном."
"Мусять, але замість цього вона згадувала осінній вечір, коли її, напівголодну, втратившу всі надії, грубий капітан королівської гвардії тягнув коридорами скляної будівлі на зустріч із спадковим принцом. Тоді вона торгувалася з Доріаном, скорочуючи термін обов’язкової служби в короля, і думала тільки про себе. А що б вона сказала, якби знала, що в ніч перед вирішальним поєдинком її хвилюватиме не тільки власна свобода, а й долі інших людей?"
"Селена зітхнула. Виходило, завтра вона битиметься не тільки заради себе. Більше того, замок, із якого раніше вона була готова втекти за будь-яку ціну, чомусь перестав здаватися їй в’язницею. Селена раптом спіймала себе на тому, що їй… хочеться затриматися в замку, і справа не тільки в чотирьох роках обов’язкової королівської служби. Скажи вона це Селені-каторжниці, та б розсміялася їй в обличчя."
"Але зараз вона не лукавила з собою. Вона хотіла залишитися. І тому завтра їй буде набагато важче."
"Кальтена щільніше запахнула теплий червоний плащ і тугіше зав’язала пояс. Хто тільки придумав узимку влаштовувати поєдинки просто неба? І чому на веранді, що оточувала Часову вежу? Кальтена намацала в кишені пляшечку з отрутою й подивилася на чаші, які заздалегідь поставили на дерев’яний стіл. Права призначалася для Селени Сардотін. Головне, ні в якому разі їх не переплутати."
"Кальтена озирнулася на герцога Перангона, що стояв біля короля. Цей похітливий бик і не підозрював, що зробить вона, коли «поцілунок смерті» прибере Селену з її шляху й Доріан знову стане вільним. Від цих думок Кальтені стало гаряче."
"Герцог попрямував до неї. Кальтена одразу опустила очі, роздивляючись плитки на веранді. Перангон зупинився перед нею, загородивши її від поглядів решти королівських радників."
"— Холоднувато для поєдинків на веранді, — сказав герцог."
"Кальтена усміхнулася й стала так, щоб пишні складки її плаща заслоняли обидві чаші. Герцог узяв її руку, але цілувати не поспішав. Другою рукою Кальтена швидко дістала пляшечку, відкоркувала пробку й вилила вміст склянки в праву чашу. До того моменту, коли герцог поцілував їй руку й випростався, спорожніла пляшечка вже лежала в кишені плаща. Доза була не смертельною, але цілком достатньою, щоб викликати в Селени запаморочення й порушити узгодженість рухів."
"Із дверей замка вийшли двоє вартових. Між ними йшла Селена. Вона була в чоловічому одязі. Навіть Кальтена неохоче визнала собі, що чорний, розшитий золотом камзол виглядає вражаюче. Невже ця дівчинка й є Адарланський асасин?"
"‘Вона була Адарланським асасином, — подумки поправила себе Кальтена. — І ніколи вже більше не буде’."
"Пані Ромпір доторкнулася до ніжки чаші й усміхнулася."
"Із-за Часової вежі вийшов Кейн, претендент герцога Перангона. Невже хтось може думати, що одурманена отрутою Селена зуміє перемогти цього силача?"
"Кальтена відійшла від столика. Перангон повернувся туди, де стояли король, радники й вища придворна знать. Усі вони жадали кривавого видовища й з нетерпінням поглядали на останніх учасників сьогоднішнього спектаклю."
"Селена стояла на широкій веранді, крадькома поглядала на Часову вежу й старалася не тремтіти від холоду. Як і багато хто, вона зовсім не розуміла, чому заключні поєдинки раптом перенесли сюди. Швидше за все, королеві захотілося ускладнити умови, в яких битимуться претенденти. Руки Селени вже встигли задубіти. Вона засунула їх у обшиті хутром кишені й підійшла до Шаола. Капітан стояв біля величезного кола, начерченого крейдою на плитках веранди."
"— Ну й холоднеча, — сказала Селена."
"Комір і рукави її чорного камзола були з підкладкою з кролячого хутра, але хутро погано гріло."
"— Чому ти не попередив мене?"
"Шаол похитав головою, дивлячись на Могилу й Ренальта — найманця з містечка з жахливою назвою Бухта Черепів. Селена з задоволенням відзначила, що ця ехидна гадина мерзне ще сильніше, ніж вона."
"— Ми самі нічого не знали, — пошепки відповів Шаол. — Король в останню хвилину вирішив проводити поєдинки тут. Сподіваюся, вони не затягнуться, — додав він із легкою усмішкою."
"Він чекав, що усміхнеться й Селена, але вона залишилася серйозною."
"Над головою яскраво синів безхмарний небосхил. Кроляче хутро капітулювало перед вітром, і Селена від холоду скреготала зубами. Для іменитих глядачів поставили м’які стільці. Королеві принесли його скляний трон. Праворуч від короля сидів Перангон. За стільцем герцога стояла Кальтена в красивому червоному плащі, обшитому білим хутром. Їхні очі зустрілися, і Селену здивувало, що та їй усміхається. Невдовзі вона зрозуміла: усмішка цієї жеманниці була адресована не їй, а Кейну."
"Схоже, головний противник Селени зовсім не страждав від холоду. Його руки й торс перетворилися на гори м’язів, що випирали з-під мундира. Але це була чужа, вкрадена сила."
"‘А якби риддерак тоді мене роздер, Кейну перейшла б і моя сила’, — зовсім не до місця подумала Селена."
"На поєдинки Кейн явився в червоному, розшитому золотом мундирі королівської гвардії. На грудях вигиналася вишита виверна. Напевно, це було зроблено з дозволу Перангона. Селена одразу оцінила чудовий меч, що висів на поясі Кейна. І меч — явно подарунок герцога. А чи знає його світлість, яку силу встиг набути його претендент і яким чином? Говорити Перангону про це було марно: у погляді герцога завжди просвічувала ненависть до Селени. Він би й слухати не став, а якби й вислухав, то не повірив би жодному її слову."
"До горла підступала нудота. Шаол узяв Селену під лікоть і повів у дальній кінець веранди. Двоє немолодих придворних із числа іменитих глядачів з тривогою поглядали на неї. Вона кивнула їм, як старим знайомим."
"‘Що ж це ви так хвилюєтеся, панове Урізен і Гарнель? Це ж справа минула, і ви напевно сповна отримали те, заради чого пішли на вбивство. Моїми руками’."
"Два роки тому вони найняли Селену, щоб убити одну людину, що заважала обом. Кожен із них не знав, що він не єдиний замовник, а Селена не вважала за потрібне відкривати їм цю таємницю й узяла плату з обох. Вона підморгнула панові Гарнелю, і той ледь не поперхнувся, перекинувши красиву кружку з гарячим напоєм і зіпсувавши аркуші пергаменту, що лежали перед ним на столі. Даремно він турбувався: Селена вміла зберігати секрети, бо не бажала псувати собі репутацію. Але якщо її свобода залежатиме не тільки від королівського рішення, а ще й від голосування… Вона усміхнулася панові Урізену, і той поспішно відвернувся. І тут Селена побачила уважний погляд короля, спрямований прямо на неї."
"Король. Усередині в неї все тремтіло, але вона вклонилася, як того вимагав придворний етикет."
"— Ти готова? — запитав її Шаол."
"Селена здригнулася, згадавши, що він поруч."
"— Так, — сказала вона, хоча відчувала зовсім інше."
"Вітер крижаними пальцями скуйовдив їй волосся, і вона закинула вибиті пасма собі за вуха."
"— Як би не розвивалися події, я хочу тебе подякувати, — сказала вона Шаолу."
"— За що? — здивувався він і нахилив голову до плеча."
"У Селени сльозилися очі — звичайно ж, від вітру, що нещадно дув їй в обличчя."
"— За те, що я битимуся не тільки за свою свободу."
"Шаол мовчки стиснув її долоню, провівши великим пальцем по подарованому їй кільцю."
"— Начинаємо другий поєдинок! — гучно крикнув король."
"Капітан ще раз стиснув їй руку. Його пальці були дивовижно теплими."
"— Улаштуй йому пітьму кромішню."
"Могила ввійшов усередину кола й неквапливо витягнув меч із піхов. Селена розпрямила плечі й теж ступила всередину. Вона квапливо вклонилася королеві й своєму противнику."
"Він ухмилявся, дивлячись, як вона злегка зігнула коліна, стискаючи обома руками красиву, але явно марну чужоземну палицю."
"‘Рано усміхаєшся, коротунчику. Скоро від твоєї ухмилки не залишиться й сліду’."

#Епізод 25

"Як і очікувала Селена, Могила кинувся до неї, сподіваючись ударити мечем посеред посоха й зламати її зброю. Але Селена встигла відскочити, і меч Могили розсік повітря. У цей час вона другим кінцем посоха вдарила противника в спину. Могила похитнувся, однак устояв на ногах. Різко обернувшись, він приготувався до нової атаки."
"Цього разу Селена прийняла удар, нахиливши посох так, щоб меч зіткнувся з його нижньою половиною. Міцне дерево посоха затиснуло лезо, і тоді Селена стрибнула до противника. Могила забув, що в посоха є ще й верхня половина, і коли він ударив по нижній, верхня з тією ж силою в’їхала йому по обличчю. Могила поп’ятився назад, але тут його вже чекав кулак Селени. Від болю в неї зануло кісточки пальців. Судячи з хрусту, вона зламала Могилі ніс. Не бажаючи, щоб її забризкало кров’ю, Селена спритно відскочила. Могила перетворився на розлючену тварину, повністю втративши здатність думати."
"— Ах ти, дрянь! — прошипів він і знову кинувся до Селени."
"Вона зустріла його удар, тримаючи посох обома руками. Дерево було міцним, але все ж не міцніше металу, і посох видав жалісний, схожий на стогін, звук."
"Селена штовхнула Могилу й стрімко повернулася, ударивши його по голові металевим наконечником. Могила й цього разу устояв на ногах, хоча здавалося, він ось-ось звалиться. Він важко дихав, витираючи рукавом закривавлений ніс. Очі злісно блищали. Його конопате обличчя зараз нагадувало звірячу морду. Він і поводився як звір, якому нічого втрачати. Зібравши всі сили, Могила кинувся до неї, цілиться мечем прямо в серце. Він був занадто швидким і розлюченим, і пряме зіткнення не обіцяло Селені нічого доброго."
"І тоді вона припала до плит веранди. Меч просвистів у неї над головою, і в цей час Селена що є сили вдарила Могилу по ногах. Він не встиг навіть скрикнути, як уже валявся на підлозі. Селена ногою притиснула йому руку, що стискала меч, а сама схилилася над ним, тримаючи металевий кінець посоха біля самого його горла."
"— Мене звати Селена Сардотін, — прошепотіла вона, нахиляючись до вуха Могили. — Але це справи не змінює. Я все одно розправлюся з тобою, як би ти мене ні називав — Селеною, Ліліаною чи навіть дрянью."
"Усміхаючись, Селена випросталася. Могила очманіло дивився на неї. Кров із зламаного носа текла по щоці. Селена дістала з кишені носову хустку й кинула йому."
"— Це тобі мій прощальний подарунок, — сказала вона, покидаючи веранду."
"Вийшовши за межі кола, Селена повернулася туди, де стояв Шаол."
"— Скільки часу тривав поєдинок? — запитала вона й помітила усміхнену Нехемію."
"— Хвилини дві."
"Селена усміхнулася Нехемії, злегка хитнувши посохом, і кивнула капітану. Вона анітрохи не втомилася."
"— Я впоралася швидше, ніж Кейн."
"— І Могилі дісталося сильніше, ніж Ренальту, — усміхнувся Шаол. — А що це тебе потягнуло кинути йому хустку?"
"Селена вже збиралася відповісти, але король підвівся з трону, і всі замовкли."
"— Вина переможцям! — наказав король."
"Кейн наблизився до столу. Селена не ворухнулася, продовжуючи стояти поруч із Шаолом."
"Король махнув рукою Кальтені, і та взяла срібний піднос із двома чашами. Одну вона подала Кейну, другу піднесла Селені. Потім Кальтена повернулася до столу й, драматично піднявши руки, проголосила:"
"— На знак доброї віри й на честь великої Богині. Нехай вино в цих чашах стане вашим приношенням Матері, від якої ми всі народилися. Пийте, і нехай пребуде на вас її благословення, і нехай примножить вона вашу силу."
"Селені захотілося штовхнути її в бік. І хто тільки складав для неї цю дурнувату промову?"
"Кальтена вклонилася обом претендентам. Селена піднесла чашу до губ. Бачачи, як вона п’є, король чомусь усміхався. Потім Кальтена взяла в неї спорожнілу чашу, підійшла до Кейна, взяла його чашу, зробила реверанс і віддалилася."
"‘Переможи. Переможи. Переможи. Розправся з ним якомога швидше’, — твердила собі Селена."
"— Приготуватися! — гаркнув король. — За моїм знаком почнете поєдинок."
"Селена запитально подивилася на Шаола. Невже їй не дозволять хоч трохи відпочити? Доріан здивовано вигнув брови, звернувшись до батька з німим запитанням. Однак король нічого не бажав помічати."
"Кейн витягнув меч і, криво усміхаючись, вийшов на середину кола, де зайняв оборонну позицію."
"Якби зараз Шаол не торкнувся її плеча, Селена б точно наговорила йому гидот. Але він тільки провів рукою по плечу. Селена вперше побачила в його золотаво-карих очах тривогу й надію. Його грубувате обличчя випромінювало силу, і Селена мимоволі замилувалася знайомими рисами."
"— Не програй, — зовсім тихо прошепотів він. — Мені зовсім не хочеться супроводжувати тебе назад в Ендов’єр."
"Світ по краях підернувся туманом. Шаол відійшов із високо піднятою головою, не звертаючи уваги на сліпуче сяйво, що виходило від короля. Селену здивували незвичні відчуття, і вона віднесла їх на рахунок випитого вина."
"Кейн зробив кілька кроків у її напрямку. Широке лезо його меча блищало, відбиваючи сонячне світло. Селена глибоко вдихнула й увійшла в коло."
"— Починайте! — прорычав завойовник Ерілеї."
"Селена струснула головою, проганяючи туман перед очима. Вона тримала посох, як меч, і стежила за Кейном. Той почав ходити колами. Їй до нудоти був противний вигляд його м’язів. Що таке? Димка перед очима ніяк не бажала розсіюватися. Селена стиснула зуби й знову струснула головою. Нехай Кейн і сильніший за неї, вона зуміє обернути проти нього його ж силу."
"Кейн атакував швидше, ніж вона очікувала. Розуміючи, що меч Кейна може перерубати посох, Селена старалася обрати якнайщадніший кут, готуючись відскочити одразу, як почує тріск дерева."
"Але Кейн ударив занадто швидко, не залишивши їй часу для маневру. Лезо глибоко вп’ялося в дерево. У Селени зануло руки. Не давши їй отямитися, Кейн висмикнув меч і знову рушив в атаку. Селена була змушена відступати, відбиваючи удари металевим наконечником посоха. У всьому її тілі відчувалася незрозуміла важкість і повільність. Голова кружилася. Невже вона захворіла? Відчуття нудоти теж ніяк не зникало."
"Прикликавши на допомогу всю силу й уміння, Селена відірвалася від Кейна. Якщо вона й справді захворіла, треба закінчити поєдинок якомога швидше. Нічого красувався й хизуватися своїми навичками. Якщо та книга не бреше, Кейн забрав собі силу всіх убитих претендентів."
"Не можна без кінця відступати. Так недовго опинитися й за крейдяною межею. Селена перейшла в наступ. Без стрімкості, спокійно й послідовно. І так само спокійно й послідовно Кейн парирував усі її атаки. Кожне зіткнення меча з посохом зрізало все нові й нові стружки, що пахли лотосом."
"Її вуха глохли від ударів власного серця. Тріск посоха ставав усе нестерпнішим. І звідки ця противна в’язкість, наче вона б’ється не на повітрі, а в густому киселі?"
"На якийсь час Селені стало легше. Її атаки знову набули швидкості й сили. І все марно. Кейн сміявся їй в обличчя, а вона ледь не кричала від злості. Кілька разів Селена опинялася в дуже вигідному становищі, щоб підніжкою перекинути його на підлогу, але з незрозумілої причини її рухи втрачали швидкість і спритність. Якщо ж вона підбиралася до Кейна зовсім близько для безпосередньої атаки, він раптом з усмішкою вислизав, наче наперед знав її задуми. Вона відчувала себе мишею, з якою грається кіт. Поспішати йому нікуди. Гра його поки розважає, а коли набридне, він прикончить мишу одним ударом лапи."
"Селена махнула посохом у повітрі, сподіваючись ударити по незахищеній шиї Кейна. Але він в останню мить парирував удар, відщепивши ще шматочок від її зброї. Вона спробувала завдати удар у живіт — Кейн знову ухилився."
"— Ми погано себе почуваємо? — їдко запитав Кейн, сяючи білосніжними зубами. — Може, це покарання за надмірну цікавість?"
"БУМММ!"
"Нижній кінець її посоха вдарив Кейна в бік. Противник скривився, і тотчас же Селена додала удар ногою, перекинувши його. Кейн шумно повалився на підлогу. Усміхаючись, вона замахнулася посохом, але ледь не завила від судоми, що охопила все тіло. Коли судома минула, минули й сили."
"Удар вийшов млявим. Кейн граючись його відбив, змусивши Селену відступити. Він підвівся й неквапливо обтрусився. У цей час Селена почула сміх — неголосний злорадний жіночий сміх. Кальтена. У Селени підкосилися ноги. Вона прикусила губу, глибоко вдихнула й глянула туди, де на срібному підносі стояли дві порожні чаші. Ось воно що! Їй підмішали в вино «поцілунок смерті». Отрута, яку під час випробування вона ледь не вважала звичайною водою. Скільки ж їй влили? Якщо трохи… розузгодженість рухів уже настала. Втрата сил — теж. Залишилося чекати галюцинацій. А якщо Кальтена перестаралася…"
"Селені раптом стало важко утримувати посох. Кейн надвигався, і вона ледь встигала відповідати на його удари. І все-таки яку дозу їй підмішала ця жеманна гадина? Посох тріщав, загрожуючи розколотися. Від його чудової різьби залишилися лише крихітні острівці. Смертельну дозу їй дати не могли, інакше вона б уже валялася мертва."
"А такий кінець був явно не потрібен тим, хто поневолює Кальтену. Їм треба, щоб зберігалася видимість поєдинку. Селені було все важче зосереджуватися. Її кидало то в жар, то в холод. Кейн раптом перетворився на велетня заввишки з гору, а його удари… У порівнянні з ними удари Шаола під час їхніх поєдинків здавалися дитячою забавою."
"— Уже втомилася? — з фальшивою участю запитав Кейн. — Я ж казав, що твоє гавкання нічим добрим не закінчиться."
"Він же знав, що її отруїли. Напевно знав. Селена глухо заричала й кинулася на нього. Кейн відступив, і посох розсік повітря. Ще раз і ще, поки…"
"Кейн ударив її кулаком у спину. Підлога стала стрімко наближатися. Селена впала, уткнувшись обличчям у плитки веранди."
"— Як сумно."
"Його тінь нависла над нею, але Селена встигла відповзти. У роті було солоно від крові. Те, що з нею сталося, здавалося неймовірним. А чому? Вони ж боялися її перемоги."
"— На місці Могили я б вважав образою, що якась дівчинка мене перемогла, — прошепотів їй Кейн."
"Вона стояла на колінах, усе ще стискаючи в руках марний обломок посоха, і шумно дихала ротом. Із нижньої губи струменіла кров. Кейн роздивлявся її обличчя, наче читав там невидимі знаки й чув слова, недоступні Шаолу."
"— А що б сказав твій дорогий батько, якби побачив свою нікудишню донечку?"
"В очах Селени промайнув не то страх, не то замішання."
"— Заткни свою пащу, — огризнулася вона, тремтячим голосом вимовляючи кожне слово."
"Але Кейн продовжував дивитися на неї, і його ухмилка ставала все ширшою."
"— А це ж усе звідти тягнеться. Ти побудувала на цьому стіну й заспокоїлася. А воно лізе з-під стіни. Я це добре бачу."
"‘Що таке він каже?’ — думав Шаол."
"Він з труднощами стримувався, щоб не кинутися всередину кола й не вчепитися Кейну в горло. А торжествующий Кейн підняв меч і неквапливо провів пальцем по кромці леза, витираючи сліди крові. Її крові."
"— Розкажи-но, як тобі було прокинутися між батьками, коли обидва вони лежали холодненькі, а ти — вся в їхній крові. Перелякалася?"
"— Заткни свою пащу! — знову промовила Селена, дряпаючи пальцями підлогу."
"Її обличчя перекосилося від гніву й болю: тілесного й душевного. Є рани, які не загоюються, а лише покриваються кіркою. Схоже, Кейну вдалося здерти кірку."
"— Мамочка-то твоя була зовсім ще молода й навіть красива, — не вгамовувався Кейн."
"— Заткнись!"
"Вона спробувала встати, але покалічена нога не дозволила. Селена судомно хапала ротом повітря. Звідки Кейн міг знати такі подробиці про її минуле? Серце Шаола шалено калатало, але Селені він зараз нічим допомогти не міг."
"Із стогоном, що прорвався навіть крізь вітер, вона все-таки підвелася на ноги. Біль перелився в лють, і Селена кинулася на меч Кейна, розмахуючи обломком посоха."
"— Добре, — похвалив Кейн, вонзаючи меч у дерево. — Але мало."
"Із цими словами він відштовхнув Селену. Спотикаючись, вона поп’ятилася. Кейн ногою вдарив її по ребрах. Удар був настільки сильним, що Селена злетіла в повітря."
"Шаол не пам’ятав, щоб хтось падав із таким оглушливим гуркотом. Ударившись об плитки веранди, Селена кілька разів перекувирнулася. Можливо, її понесло б і далі, якби на шляху не опинилася Часова вежа. Селена вдарилася головою об чорний мармур. Шаол стискав зуби, щоб не заволати на повний голос. Йому залишалося лише дивитися, як Кейн знищує Селену по частинах. Але чому цей поєдинок майже одразу перетворився на бійню?"
"Тремтячи всім тілом, Селена підвелася на коліна. Однією рукою вона трималася за бік. Її рука по-старому стискала обломок посоха Нехемії, наче він був скелею посеред бурхливого моря."
"Немає нічого противнішого за смак власної крові. Ця думка майнула в Селени, коли Кейн знову схопив її й поволік по підлозі. Вона не намагалася відбиватися. Кейну зараз надавалася чудова можливість у будь-який момент приставити меч до її серця й закінчити поєдинок. Але це був не поєдинок, а страта. І ніхто не робив найменших спроб втрутитися й припинити повільне вбивство Селени. Вони боялися, що при повній силі вона переможе Кейна, і тому отруїли її. Це було нечесно, але кого в королівському оточенні турбує чесність?"
"Сонце сліпило очі. Переборюючи біль, Селена звивалася, намагаючись вирватися з хватки Кейна. А навколо перешіптувалися й пересміювалися глядачі. Ще б пак — такого видовища ніхто з них не очікував."
"Потім усе загородив підборіддя Кейна. Кейн ривком підняв її на ноги й буквально вдавив у холодний гладкий мармур. Першим удар прийняло її обличчя. Селену огорнула знайома темрява. Голова розколювалася від болю, але крик завмер у Селени на губах, коли вона розплющила очі й побачила перед собою… мерця."
"Це був чоловік, блідий, наполовину згнилий. Його очі горіли червоним вогнем. Скрючений палець вказував на неї. Гострі зуби мерця були настільки довгими, що стирчали з рота."
"Куди зник зовнішній світ? Мабуть, у неї почалися галюцинації. Потім її засліпила спалах світла. Кейн знову кудись її тягнув. Ні, не кудись, а до крейдяного кола."
"Чиясь тінь загородила сонце. Усе закінчено. Вона або помре прямо тут, або буде відправлена в Ендов’єр. Усе закінчено. Вона програла."
"Селена побачила пару чорних чобіт. Хтось присів над нею навпочіпки."
"— Вставай, — прошепотів Шаол."
"Вона не наважувалася глянути йому в обличчя. Усе закінчено."
"Кейн почав реготати. Він розхажував уздовж крейдяного кола, і кожен його крок молотом віддавався в неї в голові."
"— На цьому твої дивовижні здібності закінчилися? — крикнув він, передчуваючи швидку перемогу."
"Селену затрясло. Навколишній світ знову заволокло туманом, і в надвигаючійся темряві зазвучали голоси."
"— Вставай, — повторив Шаол, уже голосніше й вимогливіше."
"Селена тупо дивилася на крейдяну лінію, що позначала межу арени."
"Усе, що казав Кейн… звідки він міг це знати? Значить, він це побачив у її очах. А якщо він знає про її минуле… Селена схлипнула, ненавидячи себе за слабкість. Але їй було не втримати сліз, і вони полилися, змиваючи кров з обличчя й капаючи на підлогу. Усе закінчено."
"— Селено, — з незвичною ніжністю промовив Шаол."
"Вона побачила його пальці біля товстої крейдяної риски."
"— Селено, — шепотом повторив він, і в цьому шепоті сплелися біль і надія."
"Його простягнута рука й надія… обіцянка чогось кращого, що чекало її по той бік крейдяної риски. Усе, що в неї залишилося."
"Селена ворухнулася, і від болю з очей одразу посипалися іскри. Але вона простягнула свою руку назустріч його руці. Тепер їхні долоні розділяла лише товста смуга крейди."
"Подивившись на Шаола, Селена побачила, що його обличчя підернуте сріблястою димкою."
"— Вставай, — знову зажадав він."
"Його обличчя — тільки воно зараз ще мало для неї якийсь сенс. Селена хотіла приподнятися, і її тіло одразу ж відгукнулося хвилею болю, змушуючи лягти. Вона схлипувала від власного безсилля, але продовжувала дивитися в золотаво-карі очі Шаола. Його щільно стиснуті губи прошепотіли:"
"— Вставай."
"Селена відсунула руку від крейдяної риски, ведучи долонею по мерзлих плитках. Кожен рух — спалах болю. Перша спроба встати закінчилася нічим — її підвело покалічене плече. Тоді Селена підсунула здорову ногу під себе. Встаючи, вона почула кроки наближавшогося Кейна й побачила широко розплющені очі Шаола."
"Кейн схопив її й знову штовхнув на мармур Часової вежі. Навколишній світ кілька разів змінив свої фарби. Селена встигла прикріпити очі долонею, і основний удар прийшовся на її пальці… Коли вона знову розплющила очі, усе навколо змінилося. Темрява. У глибині душі Селена знала: це не просто галюцинація, викликана зіллям. Світ, який вона зараз бачила, існував за завісою, що розділяла її світ і цей. Підмішана Кальтеною отрута прибрала завісу."
"Перед нею застигли дві істоти. Та, що знаходилася ліворуч, мала крила. І ухмилялася зовсім як…"
"Селена не встигла навіть скрикнути. Демон махнув крилами, придавив її до землі й увонзив у неї кігті. Вона звивалася всім тілом. Куди зник звичний світ? Де вона тепер?"
"А мешканців цього світу ставало все більше. Мерці, демони, чудовиська — усі жадали її. Вони називали її на ім’я. Більшість із них була з крилами, а своїх безкрилих побратимів вони переносили в кігтистих лапах."
"Усім їм не терпілося якнайшвидше забрати її в свій світ. Часова вежа слугувала порталом, який зараз був відчинений навстіж. А там… там вони її поглинуть і, швидше за все, передеруться через шматки її тіла. У житті Селени бували миті жаху, але такого жаху — всеосяжного й безнадійного — вона ще не зазнавала. Прикривши голову руками, вона відбивалася, як могла. І все-таки куди зник звичний світ? Яку дозу отрути підмішала їй ця курка? Напевно, все-таки смертельну, але так, щоб смерть не була миттєвою."
"Однак Селена не збиралася здаватися. Жах змінився злістю й готовністю крушити все на своєму шляху. Вона махнула вільною рукою й ударила по примарному обличчю з двома палаючими вуглинками замість очей. Темрява розсіялася, і Селена побачила ухмиляючуся фізіономію Кейна. Над його головою сяяло сонце. Скільки вона протримається, перш ніж її накривить новою хвилею видінь?"
"Кейн потягнувся до її горла. Селена відсмикнулася, і йому вдалося схопити лише її амулет. Ланцюжок під його пальцями розірвався, наче тонка нитка, і «Око Еліани» зісковзнуло з її шиї."
"Сонце згасло. Її розумом знову повелівала отрута. Селену оточували десятки й сотні мерців. Чомусь серед них перебувала й похмура постать Кейна. Він підняв руку й з силою жбурнув амулет."
"Мерці прийшли за нею."
"Доріан у жаху дивився на Селену. Вона звивалася всім тілом, б’ючись не з Кейном, а з якимось невидимим противником."
"‘Що відбувається?’ — знову й знову подумки запитував себе Доріан."
"Принц уже не сумнівався в тому, що Селені підмішали в вино якусь отруту. Але не менше, ніж поведінка Селени, його дивувала поведінка Кейна. Той стояв і ухмилявся… Може, учасники поєдинку справді бачили щось, недоступне всім іншим?"
"Селена пронизливо закричала, і в Доріана все стиснулося всередині. Він сказав Шаолу, побачивши, що той підводиться зі свого місця:"
"— Зупини цю бійню."
"Але Шаол лише дивився, як Селена катається по підлозі, і його обличчя було зовсім блідим."
"Селена била й лягала повітря. Кейн нахилився над нею й з розмаху вдарив по губах. Хлинула кров. Це гидотне видовище продовжуватиметься, поки король не накаже його припинити або поки Селена після чергового удару Кейна не втратить свідомість. Або ж… Але трагічність того, що відбувалося, не застопорила принцу розум. Він ще раз нагадав собі: будь-яке втручання — навіть спроба сказати, що подане Селені вино було отруєне, — дасть протилежний результат. Селену тут же оголосять «порушницею правил», а перемога дістанеться Кейну."
"Селена прагнула відповзти подалі від Кейна. Із її напіввідкритого рота на стиглі плитки капала слина вперемішку з кров’ю."
"Поруч із Доріаном хтось стояв. Обернувшись, він побачив Нехемію. Принцеса промовила кілька ейлуейських слів і пройшла далі, до самого кола. Її пальці, майже повністю закриті складками плаща, швидко рухалися, чертівши в повітрі якісь знаки."
"Кейн, наче мисливець, почав підкрадатися до зблідлої, перепачканої власною кров’ю Селени. Вона важко дихала й дивилася невідомо куди, не помічаючи ні крейдяного кола, ні глядачів."
"Вона чекала Кейна. Чекала, коли він підійде, щоб… убити її."
"Селені не вистачало повітря. Їй було ніяк не вибратися з тенет галюцинацій у звичний світ. А тут її оточували мерці. Вони чекали. Поблизу стояв схожий на привида Кейн і теж чекав. Палаючі очі — єдине, що залишилося в ньому від колишнього Кейна. Темрява колихалася навколо нього, наче лахміття на вітрі."
"Незабаром її життя обірветься."
"‘Світло й темрява. Життя й смерть. А до чого належу я?’"
"Ця думка струснула її так сильно, що руки Селени почали шукати будь-яку підходящу зброю, яка згодилася б у битві з Кейном. Ні, так просто й безропотно вона не загине. Вона знайде спосіб, обов’язково знайде якийсь спосіб залишитися живою. ‘Я не буду боятися’. Ці слова вона щоранку шепотіла в Ендов’єрі, наче молитву. Але яка користь від них тут?"
"До Селени підлетів демон. Із її горла вирвався крик. Це не був крик жаху чи відчаю. Це була мольба. Заклик про допомогу."
"Демон відлетів, наче її крик налякав його. Кейн звелів демону наблизитися."
"А потім сталося дещо дуже дивне."
"Навколо з шумом почали відчинятися двері. Дерев’яні, залізні й зовсім уже незвичайні двері, зроблені з повітря й з магії."
"Невідомо звідки з’явилася Еліана, убрана в золотаве сяйво. Волосся давньої королеви сяяло, як хвіст комети в небі над Ерілеєю."
"Кейн, усміхаючись, підійшов до простертої Селени й підняв меч, цілиться їй у серце."
"Еліана махнула рукою, і золотавий вихор розметав сонм мерців, змусивши Кейна опустити меч."
"Вслід за вихором налетів справжній вітер. Він збив Кейна з ніг. Падаючи, Кейн випустив меч, і той зі звоном упав на іншому кінці веранди. Але Селена, замкнена в цьому темному, жахливому світі, бачила лише, як Еліана підскочила до Кейна й перекинула його на землю. Мерці кинулися в атаку, але було пізно. Навколо Еліани виник золотавий захисний кокон. Мерці поп’ятилися назад."
"А над верандою й головами глядачів вирував справжній ураган, що при безхмарному небі було більш ніж дивно. Люди закривалися плащами й просто руками, гадаючи про причини появи шаленого вітру."
"Демони з оглушливим ревом кинулися до Еліани."
"Зловісно усміхаючись, вона махнула мечем, і один із демонів знайшов свою смерть. Він упав, обливаючись густою чорною кров’ю. Еліана кидала їм виклик, пропонуючи хоробрим їхнього племені випробувати на своїх шкурах усю силу її гніву."
"У Селени заплющувалися очі. Переборюючи себе, вона дивилася на корону, що вінчала голову Еліани. Корона цілком складалася із зірок. Сріблясті обладунки королеви сяяли, як маяк, розганяючи темряву. Демони налякано завили. Еліана простягнула руку. Із її пальців вирвався золотавий світло й звів стіну між демонами, мерцями й Селеною. Давня королева схилилася над нею, узявши її обличчя в свої долоні."
"— Я не в силі тебе захистити, — сказала Еліана."
"Від її шкіри виходило сяйво. Обличчя Еліани теж стало іншим: більш суворим і прекрасним. Зараз вона була схожа на жінку народу фе."
"— І силу свою передати тобі я теж не можу, — продовжила Еліана, піднявши пальці над чолом Селени. — Але зате я можу вивести отруту з твого тіла."
"Кейн силкувався підвестися на ноги. Вітер хльостав по ньому з усіх боків, змушуючи лежати."
"Чергове порив вітру погнав до Селени залізний наконечник від посоха. Вона вже зраділа, але наконечник ткнувся в щербату плитку й завмер за кілька футів."
"Еліана торкнулася її лоба."
"— Візьми, — сказала вона, вказуючи на обломок посоха."
"Селена напружила сили, прагнучи дотягнутися до обломка. У очах у неї майоріли то залиті сонцем веранда, то кромішня темрява. Кожен рух відгукувався диким болем у плечі. Нарешті їй вдалося схопити обструганий мечем обломок посоха. Десь на ньому ще залишалися сліди різьби."
"— Коли отрута вийде з тіла, ти не побачиш ні мене, ні демонів, — сказала Еліана, чертівши якісь знаки на лобі Селени."
"Кейн потягнувся за мечем, запитально дивлячись на короля. Король кивнув."
"Еліана тримала обличчя Селени в своїх руках."
"— Не бійся."
"По інший бік золотавої стіни, наче голодні цуценята, скавчали мерці, промовляючи ім’я Селени. Але потім Кейн разом із темною істотою, що жила всередині нього, легко пройшов крізь стіну, і вона повністю обвалилася."
"— Жалюгідні фокуси, ваше величество, — усміхаючись, сказав він Еліані. — Дуже жалюгідні."
"Еліана скочила на ноги, перегородивши йому шлях до Селени. Навколо Кейна заклубочилися тіні. Його очі спалахнули. Дивлячись на Селену, він сказав:"
"— Я знаю, чому ви обидві тут. Ви — учасниці однієї давньої, але незакінченої гри. Мої друзі розповіли мені про це, — додав Кейн, киваючи на мерців."
"— Забирайся, — наказала йому Еліана, начертивши в повітрі знак."
"Із-під її пальців вирвався блакитний світло."
"Кейн завив, а світло, наче стрічка, почало оперізувати його тіло. Потім воно зникло. Мерці залишилися. Еліана — теж. Вони кинулися було в атаку, але давня королева прикривалася золотавим щитом, бурмочучи щось крізь стиснуті зуби. Потім вона опустилася на коліна й обхопила плечі Селени."
"— Отрута майже повністю вийшла з твого тіла."
"Навколишній світ помітно посвітлішав. З’явилися плями сонячного світла."
"Селена кивнула. Страх і відчай змінилися болем. Тіло стало відчувати зимовий холод, нестерпно пекучу ногу й липке тепло застигаючої крові. Чому тут Еліана? І що за дивні рухи робить Нехемія, стоячи біля самої межі крейдяного кола?"
"— Вставай, — звеліла їй Еліана."
"Королева ставала все більш прозорою. Вона прибрала руки зі щік Селени, і в небі спалахнуло біле світло. Отрута повністю покинула поранене тіло асасина."
"Противник підійшов до простертої Селени. Колишній Кейн, із плоті й крові."
"Біль. Усе тіло Селени складалося з болю. Відчайдушно боліли голова, плече, рука й ще…"
"— Вставай, — прошепотіла Еліана й зникла."
"Навколо знову був звичний світ. І в цьому світі, зовсім поруч, перебував Кейн без жодного ореолу тіней. Селена стиснула в руці спотворений обломок посоха. Її зір прояснився."
"Тремтячи й стискаючи зуби, Селена встала."

#Епізод 26

"Права нога зараз була кепською опорою, але Селена, стиснувши зуби, все-таки встала. Розправивши плечі, вона дивилася на зупинившогося Кейна."
"Вітер приємно обдував їй обличчя й золотавим віялом відкидав назад її волосся. «Я не буду боятися». На лобі Селени осліпливо сяяв блакитний «знак долі»."
"— Що це в неї на лобі? — насторожився Кейн."
"Король підвівся й насупив брови. Нехемія здивовано скрикнула."
"Відчайдушно болючою, майже марною рукою Селена витерла кров із губ. Кейн заревився й кинувся на неї з мечем, явно наміряючись відсікти їй голову."
"І тоді Селена, швидка, як стріла Денни, рвонулася йому назустріч."
"Гострий обломок посоха увонзився Кейну в правий бік, який той і не думав прикривати. Кейн здивовано вирячив очі, наче це відбувалося не з ним."
"Із рани хлинула кров, заливаючи Селені руку. Вона поспішно висмикнула обломок. Хитаючись, Кейн поп’ятився назад, тримаючись за ребра."
"Селена забула про біль, страх і навіть про темні очі тирана, сердито взиравші на її палаючий знак. Вона ринулася до Кейна й тим самим гострим обломком посоха розполосувала йому руку, пошкодивши м’язи й жили. Кейн спробував дістати її другою рукою, але Селена ухилилася, завдавши удару й по тій руці."
"Кейн зробив випад, однак Селена ухилилася й цього разу, а він, втративши рівновагу, розпластався на веранді. Здоровою ногою Селена припечатала його до підлоги. Піднявши голову, Кейн побачив гострий, як ніж, обломок дерева, приставлений до його шиї."
"— Тільки ворухнися, і я цією дерев’яшкою проткну тобі горло, — пообіцяла Селена."
"Кожне вимовлене слово відгукувалося болем у її щелепі."
"Противник затих. Селена могла поклястися: на мить очі Кейна стали двома яскраво-червоними вугликами. Може, убити його прямо тут? Тоді він уже нікому не розповість ні про неї, ні про її батьків, ні про силу «знаків долі». Якщо тільки король дізнається про все це… Селена ледь утримувалася, щоб не увонзити обломок у шию Кейна. І все ж щось її стримало. Вона підняла голову й повернула понівечене обличчя до короля."
"Радники неохоче зааплодували. Звичайно, найвеличніше видовище — всі мерці й демони — було приховано від них шаленими поривами вітру. Король глянув на неї. Переборюючи біль, Селена випросталася. Кожна секунда мовчання була для неї ударом у живіт. Невже король шукає спосіб викрутитися або, гірше того, поставити під сумнів результат поєдинку?"
"Минула ціла вічність, перш ніж король заговорив."
"— Переможницею стала претендентка мого сина, — не промовив, а прорычав він."
"У Селени під ногами закрутилася підлога."
"Вона перемогла. Перемогла! Вона звільнилася… ні, впритул наблизилася до своєї свободи. Тепер вона отримає титул королівської захисниці, а потім і свободу…"
"Селена відкинула залиту кров’ю обломок посоха й зняла ногу зі спини Кейна. Важко й хрипко дихаючи, припадуючи на одну ногу, вона попленталася за межі крейдяного кола. Врятована. Еліана її врятувала. І вона… вона перемогла."
"Нехемія стояла все там же й злегка усміхалася. І раптом принцеса похитнулася й почала осідати. Телохранителі стрімголов кинулися до своєї господині. Селена теж хотіла підбігти до Нехемії, але в неї підкосилися ноги, і вона повалилася на плити веранди. Доріан, наче очунявши від закляття, кинувся до неї й опустився на коліна, без кінця повторюючи її ім’я."
"Але Селена ледь чула його. Вона скрючилася. Гарячі сльози заливали її обличчя. Вона перемогла. Сльози ще продовжували капати, а вона раптом почала сміятися."
"Поки Селена тихо сміялася, Доріан уважно оглядав її тіло. Рана на правому стегні продовжувала кровоточити. Одна рука висіла, як батіг, а на обличчі й долонях проступав жахливий візерунок дрібних ран і саден. Кейн із перекошеним від люті обличчям стояв неподалік і закривавленими пальцями затискав поранений бік. Нехай помучиться."
"— Їй потрібен лікар, — сказав принц, звертаючись до батька."
"Король мовчав. Тоді Доріан підкликав хлопчика-пажа."
"— Біжи щосили за лікарем!"
"Доріану самому було важко дихати. Чому він не втрутився й не зупинив бійню набагато раніше, коли Кейн уперше її вдарив? Чому він тільки дивився, розуміючи, що Селену отруїли, підмішавши в вино отруту? Якби він опинився в такому становищі, вона б не вагаючись прийшла йому на допомогу. Навіть Шаол хоч якось підтримав її, підійшовши до крейдяного кола. Але хто насмілився її отруїти?"
"Обережно, щоб не завдати Селені додаткового болю, принц обійняв її й підняв їй голову. Він майже здогадувався, чиїх рук це діло. Він повернувся в бік Перангона й Кальтени й тому не бачив, як його батько й Кейн переглянулися, після чого програвший схопився за меч."
"Зате Шаол бачив і одразу зрозумів: король мовчки схвалив зрадницький удар у спину."
"Не встигнувши подумати, не розуміючи, що робить, Шаол стрибнув уперед і увонзив свій меч Кейну в серце."
"Фонтан крові забризкав Шаолу голову, руки й мундир. Кров Кейна чомусь пахла смертю й гниллю. Удар виявився смертельним. Кейн похитнувся й із важким гуркотом упав."
"Стало на диво тихо. Шаол дивився, як із цієї страшної людини йде життя. Кейн випустив останній подих. Коли його очі засклили, Шаол кинув меч і присів навпочіпки біля вбитого. Доторкнутися до нього капітан не наважувався."
"Шаолу було не відірвати погляду від своїх закривавлених рук. Що він накоїв? Він убив людину. Гидкого, огидного, але людину."
"— Шаоле, — тихо покликав його Доріан, що тримав на руках завмерлу Селену."
"— Що я накоїв? — тепер уже вголос промовив Шаол."
"Селена застогнала, і її затрясло."
"Двоє вартових обережно підняли Шаола й повели в замок. Капітан дивився тільки на свої закривавлені руки. Доріан деякий час дивився йому вслід, потім повернувся до Селени. Король уже щось кричав, але Доріану зараз були важливішими слова Селени."
"Її тремтіння не вщухало, а рани все так само кровоточили."
"— Не треба було його вбивати, — з труднощами видавлюючи з себе слова, сказала Селена. — Тепер Шаола… тепер його…"
"Вона протяжно, зі стогоном видихнула."
"— Вона мене врятувала, — продовжувала Селена, ховаючи обличчя в Доріана на грудях. — Доріане, вона вивела з мене всю отруту. Вона… вона… Я навіть не знаю, як усе сталося."
"Доріан не розумів безладних слів Селени й лише міцніше притискав її до себе."
"А радники уважно стежили за ними, ловлячи кожне її слово й кожен його рух. Плювати йому на радників! Доріан поцілував їй волосся. Дивний знак на її лобі потьмянів. Звідки він узявся? Що взагалі відбувалося в останні хвилини поєдинку? Говорячи про її батьків, Кейн ударив по дуже болючому місцю, і тоді Селена втратила всяке самовладання. Такої дикої й шаленої Доріан її ще не бачив."
"Принц зневажав себе за невтручання й боягузтво. Він чесно зізнається їй у цьому. Тепер він зробить усе, щоб Селена отримала свободу, а потім… Потім…"
"Селена не опиралася, коли Доріан на руках ніс її в покої, велівши лікареві йти слідом."
"Досить із нього політики й придворних інтриг. Він любить Селену, і жодна імперія, жодний король і жодні земні страхи не завадять йому бути разом із нею. А якщо хтось спробує їх розлучити, він голими руками розірве кожного. Раніше Доріан жахнувся б таким думкам. Зараз вони його не лякали."
"Кальтена в жаху й відчаї дивилася, як Доріан несе Селену в замок. Їй досі не вірилося в те, що сталося. Чому ця дівка зуміла перемогти Кейна? Невже отрута її не взяла? Чому взагалі вона залишилася жива?"
"Очі короля зловісно блищали. Перангон був поза собою від люті. Радники щось шкрябали на пергаменті. Кальтена дістала з кишені порожню пляшечку. Невже герцог наплутав із дозою? Чи здоров’я цієї чортової Селени виявилося міцнішим, ніж вони думали?"
"А адже зараз Доріан мав би ридати над трупом убитої негідниці, і Кальтена обіймала б його, шепочучи слова втіхи. Герцог обіцяв їй такий кінець. Чому він її обдурив?"
"Мігрень, що не нагадувала про себе весь ранок, тепер узяла реванш. В очах у Кальтени потемніло, і вона втратила здатність зв’язно мислити."
"— Чому ви мене обдурили? — прошипіла вона, схиляючись над вухом герцога. — Ви ж обіцяли, що отрута подіє!"
"Король і герцог з подивом подивилися на неї. Радники здивовано переглядалися. Кальтена випросталася. Її душила злість."
"Перангон повільно підвівся."
"— Що це у вас у руці? — голосніше, ніж слід було, запитав він."
"— А то ви не знаєте! — огризнулася Кальтена."
"У неї розколювалася голова. Думки плуталися. Десь у глибині душі вона розуміла, що даремно затіяла цю розмову, але зараз нею керував лише голос власної люті."
"— Не впізнаєте? Ваш пузірець з отрутою, яку я підлила їй у вино, — прошепотіла Кальтена."
"— Пузірець з отрутою? — заревився герцог, і в Кальтени очі вилізли на лоба. — Ви що, її отруїли? Як ви насмілилися це зробити?"
"Він махнув трьом гвардійцям, підкликаючи їх до столу."
"Але чому мовчить король? Чому не заступиться за неї? Перангон казав, що король погодився на такий розвиток подій. Невже й тут збрехав?"
"Радники перешіптувалися, осудливо поглядаючи на Кальтену."
"— Як я насмілилася? — вибухнула вона. — Ви ж дали мені цей проклятий пузірець!"
"— Що за маячня ллється з ваших уст? — підвищив голос Перангон, здивовано вигинаючи свої руді брови."
"— Шахрай! — заволала Кальтена, забувши про придворний етикет. — Сукин ти син!"
"— Прошу позбавити нас від її присутності, — твердим, спокійним голосом велів гвардійцям Перангон, наче Кальтена була якоюсь сварливою служницею. Наче вона була для нього порожнім місцем."
"— Я ж вам казав, — із колишнім спокоєм продовжив герцог, нахиляючись до короля, — що вона зробить усе, тільки б домогтися спад…"
"Гвардійці, не особливо церемонячись, повели Кальтену геть, і закінчення фрази вона вже не почула. Невже герцог спритно її обдурив?"
"— Ваше величество! — заволала Кальтена, намагаючись вирватися з рук гвардійців. — Допоможіть мені! Його світлість казав, що ви…"
"Герцог байдуже відвернувся."
"— Я вб’ю тебе! — крикнула вона Перангону, кидаючи благальні погляди на короля."
"Зневажливо кривячись, король теж відвернувся. І тоді Кальтена зрозуміла: король не стане її слухати. Йому не потрібна правда, яку він і так знає. Перангон уже давно замислив такий кінець змагань, а вона виявилася зручною пішкою в його грі. Його закоханість, пориви пристрасті — жалюгідний фарс. Гра не вдалася, і тепер герцог легко жертвує пішку. Навіщо йому зайві свідки?"
"Кальтена відбивалася від гвардійців, але ті мовчки волокли її до замка. А стіл, за яким сиділи король, Перангон і радники, невблаганно віддалявся. Коли Кальтену дотягли до дверей замка, герцог послав їй їдку усмішку. Ранок, який мав стати початком тріумфу Кальтени Ромпір, розтрощив усі її мрії."
"Наступного ранку Доріан стояв перед батьком, із усіх сил намагаючись не опускати голови. Тепер уже не буде як раніше. Він витримає батьківський погляд. Після того, як батько дозволив Кейну знущатися з Селени, перетворивши їхній поєдинок на криваву забаву… після того, як Селені віроломно подали отруєне вино… Це просто диво, що Доріан взагалі не зламався після вчорашнього й знайшов у собі сили з’явитися на розмову з батьком."
"— То навіщо ти прийшов? — нарешті запитав король."
"— Я бажаю знати, що буде Шаолу за вбивство Кейна."
"Очі короля спалахнули."
"— А що, на твою думку, має йому бути за це?"
"— Нічого, — відповів Доріан. — Це не було вбивство заради вбивства. Шаол захищав Сел… асасина."
"— І ти думаєш, життя якогось асасина коштує дорожче за життя хороброго, досвідченого солдата?"
"Сапфірові очі Доріана потемніли."
"— Хоробрий і досвідчений солдат не стане завдавати зрадницького удару в спину. Особливо після того, як противниця перемогла його. У справжнього солдата є поняття про честь."
"У вчорашній історії Кальтена була лише жалюгідною пішкою. Але якщо він виявить причетність Перангона чи батька до отруєння вина… Пальці Доріана стиснулися в кулаки."
"— Про честь? — повторив король, пощипуючи бороду. — А якби на місці Кейна був я, мене, на твою думку, теж належало б убити?"
"— По-перше, ви — мій батько, — ретельно підбираючи кожне слово, відповів Доріан. — А по-друге, я впевнений: ви б собі нічого подібного не дозволили."
"— Ну й викрученим же ти став! Наче виучку в Перангона пройшов."
"— Тож ви не каратимете Шаола?"
"— Не бачу причини позбавлятися вмілого капітана королівської гвардії."
"— Дякую вам, батьку, — сказав Доріан і полегшено зітхнув."
"Подяка в його очах була щирою."
"— Ще щось? — байдуже запитав король."
"— Я… — почав Доріан і запнувся."
"Він глянув у вікно, потім знову на батька й, зібравши всю свою волю, сказав:"
"— Так. Я хочу знати, як ви маєте намір вчинити з асасином."
"Король усміхнувся, і від його усмішки всередині Доріана все похололо."
"— Асасин, — промовив король, міркуючи вголос. — Вона вельми ганебно поводилася під час поєдинку. Отруїли там її чи ні, але що це за королівська захисниця, у якої очі на мокрому місці, як у розбещеної дівчинки? А потім, будь вона по-справжньому вправним асасином, вона б одразу дізналася, що вино отруєне, і не стала б його пити. Напевно, я накажу повернути її в Ендов’єр."
"Доріан відчув, як його самовладання зникає зі страшною швидкістю. Такого від батька він не очікував."
"— Ви неправильно судите про неї! — випалив принц, але тут же схаменувся. — Що б я вам зараз ні казав, ви все одно не глянете на неї іншими очима."
"— Якими це ще іншими очима я мушу на неї дивитися? Хто такий асасин? Чудовисько в людській подобі, навчений убивати без розбору. Я велів привезти її сюди, щоб вона виконувала мої повеління, а не втручалася в життя мого сина й у справи імперії."
"Доріан оскалив зуби. Раніше він ніколи не насмілився б так дивитися на батька. Але якщо він струснув учора, сьогоднішньої боягузтва він собі вже не простить. Король неквапливо опустився на трон. Доріану раптом подумалося: а може, батько навмисне каже йому такі речі, перевіряючи, наскільки дорога для нього Селена? І раптом він відчув, що йому не хочеться копирсатися в батьківських думках. Він явився сюди не для цього. Він мусить уберегти Селену від повернення в Ендов’єр."
"— Селена не чудовисько, — сказав Доріан. — Усе, що їй доводилося робити, вона робила заради власного виживання."
"— Виживання? Ти що, повторюєш мені її брехню, якою вона тебе годувала? Є чимало способів вижити, але вона чомусь обрала ремесло вбивці. І їй подобається це ремесло. Схоже, ти в неї наче на побігеньках? Що ж, розумна дівка! Родися вона чоловіком, була б чудовим радником!"
"Із грудей Доріана вирвалося придушене ричання."
"— Ви не знаєте, про що говорите! У мене до неї немає жодної прив’язаності!"
"Доріан одразу ж схаменувся, але вимовлену фразу назад у горло не запхаєш. Він сам відкрив батькові своє нове слабке місце. При думці, що їх можуть розлучити з Селеною, у принца опустилися руки."
"Адарланський король випробовуючи глянув на спадкового принца. Доріан з останніх сил витримав батьківський погляд."
"— Я підпишу наказ, коли в мене дійдуть до нього руки. А поки раджу тобі не базікати про це."
"Всередині Доріана піднімалася хвиля холодної люті. Несподівано він ясно побачив картину з вчорашнього дня: Нехемія віддає Селені свій посох, пропонуючи битися ним. Дурною принцесу не назвеш; вона знала, що в знаках ховається сила. Якщо Селена й стане королівською захисницею, виходить, що цей титул вона отримає завдяки ейлуейській зброї. Нехемія вела гру, майже не маючи шансів виграти. І водночас Доріана захоплювала її сміливість. Одна, серед ворожого оточення."
"Коли-небудь у нього вистачить сил і сміливості, і він зажадає, щоб батько визнав усе зло, заподіяне народові Ейлуе. Насамперед — свою провину за страту ейлуейських повстанців. Не сьогодні. Не в найближчому майбутньому. Але з чогось починати треба вже зараз."
"Доріан підняв голову й, дивлячись батькові в очі, сказав:"
"— У Перангона є замисел: зробити Нехемію нашою заручницею й тим самим змусити ейлуейських повстанців підкоритися Адарлану."
"— Справді? — оживившись, запитав король. — Цікава думка. Ти згоден?"
"У Доріана спітніли долоні, але він надав обличчю байдужий вираз і відповів:"
"— Ні, не згоден. Ми могли б діяти по-іншому."
"— Могли б? Ти впевнений? А знаєш, скільки солдатів, продовольства й іншого добра я втратив через цих повстанців?"
"— Знаю. Однак перетворювати Нехемію на заручницю — справа занадто ризикована. Це тільки розлютить ейлуейських повстанців, і вони почнуть шукати собі союзників в інших королівствах. А Нехемію її співвітчизники дуже люблять. Якщо прийняти замисел Перангона, це загрожує повстанням, яке повністю охопить Ейлуе. І тоді втрати наших солдатів багаторазово зростуть, та й адарланську казну це виснажить. Але всього цього можна уникнути, якщо ми спробуємо заручитися довірою Нехемії й через неї переконаємо повстанців скласти зброю. Принцесу ніяк не можна робити заручницею."
"Стало тихо. Доріан старався стояти не ворухнувшись, витримуючи батьківський погляд. Кожен удар серця гучно віддавався в нього в усьому тілі."
"Нарешті король кивнув:"
"— Гаразд, я накажу Перангону, щоб залишив свій замисел."
"Доріан ледь не підстрибнув від полегшення, але постарався зберегти вираз обличчя й говорити якомога спокійніше:"
"— Дякую, що вислухали мене."
"Король не відповів. Не чекаючи дозволу піти, принц повернувся й покинув батьківський кабінет."
"Прокинувшись, Селена прикусила губу, щоб не застогнати. У неї боліло все тіло, але сильніше за все — плече й нога. Уся перебинтована, укрита кількома ковдрами, вона ледве-ледве змогла повернути шию й глянути на годинник, що цокав на камінній полиці. Була майже перша пополудні."
"Вона спробувала відкрити рот — щелепа тут же відповіла гострим болем. Але Селена й без дзеркала знала, як виглядає її подряпане обличчя. Ні, у дзеркало вона ще довго не дивитиметься. Вона скривилася, і щелепа знову нагадала про удар Кейна. Селена спробувала сісти на постелі — і отримала нову порцію болю."
"Одна рука була в неї в лубку, а будь-яка спроба поворухнути ногами викликала пекучий біль у пораненому стегні. Того, що було після поєдинку, Селена майже не пам’ятала. Головне, вона жива всупереч усім спробам Кейна її вбити."
"Уночі їй снилися Нехемія й Еліана, але щойно вона намагалася з ними заговорити, як замість них бачила огидні морди демонів і застиглі очі мерців. А ще їй снилися жахи з минулого, про які насмілився заїкнутися Кейн. Кошмари йшли один за одним, змушуючи її прокидатися. Рани й утома вимагали сну, але задрімати Селена змогла лише тоді, коли зовсім розсвітило."
"Вона згадала про амулет Еліани. Кейн його не роздавив, а тільки зірвав у неї з шиї й кинув. Може, з амулетом ніч пройшла б спокійніше? Селена подумки просила богів повернути їй «Око Еліани». Навіть тепер, після вбивства Кейна, амулет додав би їй спокою й упевненості."
"Двері в спальню відчинилися. У прорізі стояла Нехемія. Принцеса з сумною усмішкою підійшла до постелі Селени. Прокинулася Швидконога й одразу привітно завиляла хвостом."
"— Здрастуй, — ейлуейською сказала Селена."
"— Як ти себе почуваєш? — на чудовій адарланській запитала Нехемія."
"Цуценя перелізло через болючу ногу господині, наміряючись лизнути гостю в ніс."
"— Так само, як виглядаю, — відповіла Селена, у якої кожне слово супроводжувалося болем у щелепі."
"Нехемія присіла на край постелі, і прогнутий матрац змусив Селену скривитися. Куди ні ткни — всюди болить. Скільки ж пройде часу, перш ніж вона остаточно одужає? Швидконога, за всіма правилами собачого етикету, знову лягла спати. Селена здоровою рукою почухувала їй за вухами й чекала, що скаже принцеса."
"— Я не стану відбирати в тебе сили на порожню балаканину, — почала пояснювати Нехемія. — І правду приховувати теж не збираюся. Поки ти билася з Кейном, я рятувала твоє життя. І як бачиш, врятувала."
"Селена невиразно пам’ятала дивну картину: пальці Нехемії, що чертять у повітрі якісь знаки."
"— Тож мені це не привиділося? І ти… ти теж усе бачила?"
"Селена спробувала сісти на постелі, але не змогла піднятися."
"— Тобі нічого не привиділося, — підтвердила Нехемія. — Я справді знаю те, що й ти. Мій дар дозволяє мені розрізняти недоступне звичайному зору. Учора Кальтена підлила тобі отрути у вино, і це тимчасово підняло завісу, яка відділяє наш світ від інших світів. Звичайно, ця дурочка навіть не припускала, як подіє отрута на твою кров. Магія притягується до магії."
"Останні слова змусили Селену здригнутися."
"— Навіщо ж ти всі ці місяці робила вигляд, що не розумієш нашої мови? — запитала Селена."
"Їй хотілося змінити тему. І потім, це запитання було не менш пекучим, ніж її рани."
"— Спочатку це слугувало мені захистом, — відповіла Нехемія, обережно торкаючись здорової руки Селени. — Ти здивуєшся, скільки всього вибовкують люди, коли вважають, що ти не розумієш їхньої мови."
"— А навіщо тобі знадобилися мої уроки адарланської?"
"— Бо мені хотілося з тобою подружитися, — дивлячись у стелю, відповіла Нехемія. — Ти мені одразу сподобалася."
"— Значить, тоді, в бібліотеці, мені не привиділося? Ти там була й читала ту книгу?"
"Нехемія кивнула."
"— Бачиш, я займалася… дослідженнями щодо «знаків долі». Це адарланська назва. У нас ці символи називаються по-іншому. Пробач, на початку нашого знайомства я збрехала тобі, сказавши, що нічого в них не розумію. Я знаю про них усе. Я вмію їх читати й користуватися їхньою силою. І не тільки я. У нашій родині це вміє кожен, але ми ретельно зберігаємо свою таємницю й передаємо її з покоління в покоління. Однак «знаки долі» — це не повсякденна магія. Їх застосовують лише як крайній засіб у боротьбі зі злом або коли треба допомогти тяжко хворому. «Знаки долі» навіть не можна вважати магією в її звичному розумінні. Це інший вид сили. І тим не менш я мушу оберігати свої знання від усіх. Уявляєш, якби це стало відомо королеві чи його радникам? Вони б не подивилися, що я спадкова принцеса."
"Селена знову спробувала сісти й ледь не втратила свідомість від гострого болю."
"— Тож ти… твоя родина… ви користуєтеся силою «знаків долі»?"
"Нехемія перестала усміхатися."
"— Так, але тримаємо це в глибокій таємниці. «Знаки долі» володіють неймовірною силою, і її можна обернути як на благо, так і на зло. Людська природа така, що силою знаків частіше користувалися для злих і порочних справ. Приїхавши в замок, я одразу зрозуміла: тут є хтось, обізнаний у «знаках долі», і за їхньою допомогою він викликає в наш світ демонів із темних світів. Кейн не розумів, що йому дісталися крихти знань. Він умів лише викликати демона, але зовсім не вмів ні керувати чудовиськом, ні відправити назад. Усе це час я без кінця повертала викликаних ним монстрів назад у їхні похмурі світи. Тих, кого не вдавалося повернути, знищувала. Тепер ти розумієш, чому інколи я здавалася такою розсіяною. Мені просто не вистачало сил."
"Щоки Селени знову спалахнули від сорому. Як вона могла подумати, що це Нехемія вбиває претендентів? Як таке взагалі могло прийти їй у голову? Селена підняла праву руку, щоб ще раз глянути на шрами."
"— Тож ось чому ти тоді не стала запитувати, хто мене вкусив. І ти… зцілила мене за допомогою «знаків долі»."
"— Я й зараз не знаю, де й як ти натрапила на риддерака. Думаю, потім ти мені все розкажеш. — Нехемія прицокнула язиком і усміхнулася. — А зараз я розповім тобі ще дещо. «Знаки долі» під твоїм ліжком малювала я."
"Селена навіть підскочила й тут же була знову прикута до постелі новим спалахом болю."
"— Ти думала, хтось начертив у тебе під ліжком «знаки долі», щоб приманити до тебе невідоме чудовисько? А вони, навпаки, оберігали тебе. Знала б ти, яких трудів мені коштувало заново чертити їх після твоїх «поломойних зусиль»!"
"Повні губи Нехемії торкнулася усмішка."
"— А без них риддерак явився б до тебе набагато раніше."
"— Але чому?"
"— Не здогадуєшся? Кейн ненавидів тебе й хотів якнайшвидше прибрати з числа своїх суперників. До того ж, крім тебе, йому ніхто не міг серйозно протистояти. Частково мені навіть шкода, що його вбили. Я б обов’язково розпитала його про те, де він навчився так грубо відкривати портали. Коли через отруту тебе почало хитати між світами, він одразу скористався твоїм станом і покликав різне відреб’я, сподіваючись швидко розправитися з тобою. Але я охоче поступлюся цікавістю. За всі свої гидотні справи Кейн заслужив смерть від меча Шаола."
"Почувши ім’я капітана, Селена озирнулася на двері спальні. Шаола вона не бачила з учорашнього дня. А раптом король покарав його не тільки за вбивство Кейна, а й за всю допомогу їй?"
"— Ця людина піклується про тебе більше, ніж ви обидва думаєте, — з усмішкою сказала Нехемія, знову змусивши Селену густо почервоніти."
"Давши їй трохи заспокоїтися, принцеса продовжила:"
"— Думаю, тобі буде цікаво дізнатися, як мені вдалося тебе врятувати."
"— Ну, якщо розкажеш…"
"— «Знаки долі» допомогли мені відкрити портал в інші області іншого світу. Звідти я покликала Еліану, першу королеву Адарлана."
"— Тож ти її знаєш? — здивувалася Селена."
"— Тільки з книг. Але вона відгукнулася на мій заклик про допомогу. Інший світ багатоликий. Не всі його межі заповнені темрявою й смертю. Є й такі, де мешкають добрі істоти. У разі крайньої потреби вони готові з’явитися в Ерілею й допомогти нам. До речі, Еліана в той момент перебувала в двох світах одразу. Точніше, в проміжку між ними. Вона не могла цілком з’явитися в нашому світі, як не могла там з’явитися й уся нечисть, яку ти бачила. Відкриття порталу вимагає чималої сили. До того ж портал дуже швидко закривається, і доводиться довго чекати, коли можна буде відкрити його знову. Кейн зумів відкрити портал і виманити звідти риддерака, після чого портал зачинився. Мені коштувало чималих сил знову відкрити портал і випхнути цю тварюку назад. Ми з Кейном не один місяць грали в кота й мишку."
"Нехемія потерла скроні, наче вони й зараз ще боліли від цієї гри."
"— Ти не уявляєш, скільки сил у мене це віднімало, — додала вона."
"— Значить, у поєдинку зі мною Кейн не покладався тільки на свою силу й викликав собі на підмогу демонів?"
"— Може, й так, — трохи подумавши, відповіла Нехемія. — А може, Кейн викликав їх раніше, і вони чекали свого часу."
"— А я їх побачила тільки через отруту, якою мене почастувала Кальтена?"
"— Важко сказати, Елентіє, — знизала плечима Нехемія. — Одне я знаю напевно: Кейну були відомі таємні сили, якими володіють ейлуейці. І ось це мене дуже тривожить."
"— Ти хотіла сказати, тривожило, — поправила її Селена, важко ковтнувши. — Кейн мертвий… нарешті. Але в тому проміжку між світами він не був схожим на себе. Там Кейн виглядав сущим демоном. Чому?"
"— Бо він постійно викликав сили зла. Вони просочувалися до нього в душу й накопичувалися там. У нашому світі його облік не змінювався, а там ти побачила його справжнє обличчя."
"— Кейн говорив про мене так, наче знав усе про моє минуле, — прошепотіла Селена, стискаючи кулак здорової руки."
"В очах Нехемії щось спалахнуло."
"— Це улюблена хитрість зла. Сили зла навмисне говорять нам найобразливіші речі, щоб ошелешити нас. Їм потрібно, щоб уся їхня брехня міцно застрягла в нас у думках. Кейн був би радий побачити, як його маячня досі хвилює твою свідомість."
"Принцеса погладила Селену по руці й порадила:"
"— Не доставляй його мерзенній душонці такого задоволення. Викинь ці думки з голови."
"— Добре, що король нічого про це не знає. Мені навіть страшно уявити, як би він розпорядився силою «знаків долі», май він до неї доступ."
"— Мені теж страшно, — зізналася Нехемія. — Скажи, тобі відомий знак, який учора сяяв у тебе на лобі?"
"— Ні. А тобі?"
"— Мені теж. Але я вже бачила такий знак. Схоже, він є частиною тебе. І мене дуже тривожить, як до цього поставить король. Просто диво, що він не влаштував тобі допит із пристрастю."
"У Селени все похололо всередині."
"— Не бійся, — заспокоїла її Нехемія. — Якби королеві знадобилося дізнатися, він би вже тебе допитав."
"Селена шумно видихнула."
"— Нехеміє, а навіщо ти взагалі сюди приїхала?"
"Принцеса відповіла не одразу."
"— Звичайно, не для того, щоб присягати адарланському королеві в союзницькій вірності. Та й навряд чи ти могла б запідозрити мене в подібному. Тобі я скажу правду: я приїхала в Рафтхол з єдиною метою — якомога раніше дізнаватися про задуми й маневри короля."
"— Виходить, ти приїхала сюди шпигувати? — пошепки запитала Селена."
"— Якщо хочеш, називай це так. Але для рідної країни я готова зробити що завгодно. Жодна жертва не буде для мене надмірною — тільки б зберегти мій народ, позбавити його адарланського рабства й, звичайно ж, не допустити нової бійні."
"У Селени завмерло серце."
"— Я ще не зустрічала таких сміливців, як ти."
"Нехемія задумливо гладила мирно сплячу Швидконогу."
"— Мабуть, справа тут не в сміливості. Мені теж знайомий страх. Але моя любов до Ейлуе витісняє страх перед адарланським королем. А ти не хвилюйся. Якими б не були мої задуми, тебе, Елентіє, я в них залучати не стану."
"Селена ледь утрималася, щоб не зітхнути з полегшенням, хоча їй і було соромно за себе."
"— Наші шляхи переплелися… але тобі треба й надалі йти своїм шляхом. Тепер у тебе нове становище. Звикай до нього."
"— Можеш бути спокійна: я нікому не розповім про твої здібності."
"Нехемія сумно усміхнулася."
"— І нехай між нами більше не буде таємниць. Коли ти зміцнієш, я дуже хочу почути, де й як ти вперше зустрілася з Еліаною."
"За розмовою обидві не помітили, що цуценя вже давно крутиться по підлозі й повискує."
"— Ти не заперечуєш, якщо я візьму твою чотирилапу подругу прогулятися? Мені хочеться підставити обличчя холодному вітру."
"— Я буду тільки вдячна. Вона й так, бідолашна, стільки терпіла."
"Зраділа Швидконога заплигала навколо Нехемії."
"— Елентіє, я дуже рада, що в мене є така подруга, як ти, — сказала принцеса."
"— А я ще більше рада, що ти весь час оберігала мою дурну спину, — зізналася Селена й позіхнула. — Ти двічі врятувала мені життя… Ні, напевно, більше ніж два рази. Скільки ж разів ти рятувала мене від чудовиськ Кейна?"
"— Цього я тобі не скажу, інакше ти спати не будеш."
"Нехемія поцілувала її в лоб і пішла до дверей, супроводжувана веселим гавкотом Швидконоги. Там вона зупинилася."
"— Забула тобі віддати, — сказала Нехемія, кидаючи Селені якийсь предмет. — Це ж твоє? Мій телохранитель знайшов після поєдинку."
"На ковдрі лежав «Око Еліани»."
"— Дякую, — прошепотіла Селена, стискаючи в руці амулет."
"Коли принцеса пішла, Селена, незважаючи на біль і на все, що дізналася, усміхнулася й заплющила очі. Стискаючи амулет у руці, вона заснула й спала набагато міцніше, ніж за всі місяці її життя в замку."

#Епізод 27

"Наступного дня Селена прокинулася й не одразу збагнула, яка зараз пора доби. Невдовзі почувся обережний стук у двері. Селена заморгала, проганяючи залишки сну. До спальні увійшов Доріан. Він зупинився на порозі й деякий час просто дивився на неї."
"— Привіт, — хрипко промовила Селена, змусивши себе усміхнутися."
"Їй згадалося, як принц ніс її сюди, як дбайливо підтримував, поки лікар накладав шви на поранену ногу."
"Доріан повільно, важкими кроками підійшов до її постелі."
"— А ти сьогодні виглядаєш навіть гірше, — прошепотів він."
"Його слова змусили Селену перебороти біль і сісти."
"— Це вам здається. Я чудово себе почуваю, — заперечила Селена."
"Звичайно ж, це була суцільна брехня. На додачу до інших ран Кейн зламав їй ребро, і тепер кожен вдих супроводжувався болем у грудях. Принц стиснув зуби й відвернувся до вікна."
"— Та що з вами? — здивувалася Селена."
"Вона хотіла схопити його за полу камзола, але принц стояв занадто далеко."
"— Зі мною… сам не знаю."
"Від порожнього, втраченого погляду Доріана в неї закалатало серце."
"— Після вашого поєдинку я втратив сон."
"— Ну що ви стоїте? Сідайте сюди, — покликала його Селена, показуючи на край постелі."
"Принц слухняно вмостився спиною до неї. Він обхопив руками голову й важко дихав. Селена обережно торкнулася його за плече. Доріан стиснувся, і вона відсмикнула руку. Потім спина принца злегка розпрямилася, однак його дихання легшим не стало."
"— Доріане, вам недобре?"
"— Ні, я цілком здоровий, — промимрив він."
"— Тоді що сталося?"
"— І ти ще запитуєш? — вигукнув принц, ховаючи обличчя в долонях. — Ти з безтурботною легкістю повалила Могилу, і раптом, через лічені хвилини, тебе ніби підмінили. Кейн не бився з тобою. Він тебе повільно вбивав."
"— І через це ви втратили сон?"
"— Я не можу… не можу, — застогнав Доріан."
"Селена мовчала, даючи йому час зібратися з думками."
"— Пробач мене. Я винен, — прошепотів принц, прибираючи долоні з обличчя."
"Вона кивнула. Не поспішала його й не ставила жодних запитань."
"— Як ти насправді себе почуваєш? — із помітним страхом у голосі запитав він."
"— Жахливо, — зізналася Селена. — Підозрюю, що й виглядаю я нітрохи не краще."
"Доріан злегка усміхнувся. Він уперто намагався вирватися з хватки почуттів, що володіли ним зараз."
"— Ти ніколи ще не була так прекрасна. — Він заздрісно глянув на постіль. — Не заперечуєш, якщо я приляжу поруч? Я зовсім знесилів."
"Селена не заперечувала. Принц зняв чоботи й розстебнув камзол. Потім ліг, склавши руки на животі. Селена стежила за його обличчям, яке поступово ставало схожим на обличчя колишнього Доріана."
"— Як Шаол? — запитала вона й знову напружилася."
"Їй згадався фонтан крові й охоплене жахом обличчя капітана."
"Доріан розплющив одне око."
"— Він одужає. Попросив пару днів відпочинку. Думаю, це йому не завадить."
"У Селени стиснулося серце."
"— Ти не повинна почуватися винною, — сказав принц, повертаючись на бік, обличчям до неї. — Він зробив те, що вважав за потрібне."
"— Так, але він…"
"— Шаол знав, що робить, — вперто повторив Доріан і провів пальцем по її щоці."
"Його палець був холодним, як крижинка, але Селена зуміла придушити дрож."
"— Пробач мене, — знову сказав Доріан, обережно прибираючи палець. — Я винен, бо не зумів тебе врятувати."
"— Про що ви говорите? Невже через це ви мучитеся й не можете спати?"
"— Я винен, що не втрутився й не зупинив Кейна. Це треба було зробити одразу, як тільки я помітив неладне. Я майже одразу здогадався, чиїх це рук діло. Кальтена отруїла тебе. Я мусив передбачити такий поворот. А коли я зрозумів, що в тебе почалися галюцинації, я… Я винен, що не знайшов способу припинити цю бійню."
"У Селени перед очима заплясали демони із зеленою шкірою й жовтими іклами. Її пальці, переборюючи біль, стиснулися в кулак."
"— Вам нема в чому себе дорікати, — сказала вона."
"Їй не хотілося зараз говорити ні про жахи, побачені на межі між світами, ні про зраду Кальтени. І вже тим більше вона не була налаштована розповідати йому про те, що дізналася від Нехемії."
"— Доріане, ви все зробили правильно, — повторила вона. — Своїм втручанням ви б тільки зіпсували справу. Мене б оголосили такою, що програла."
"— Я мусив був ізрубати Кейна на дрібні шматки, щойно він насмілився доторкнутися до тебе. А замість цього я сидів і дивився. Я навіть не підійшов до тебе, як Шаол. Це я мусив убити Кейна."
"Демони перед її очима почали тьмяніти."
"— Ви починаєте міркувати, як асасин, — мимоволі усміхнулася Селена."
"— Напевно, я проводжу забагато часу з тобою."
"Селена відірвала голову від подушки, щоб улягтися поруч із його плечем. Її захлеснула гаряча хвиля. Біль заважав рухатися, але Селена все-таки опустила свою поранену руку йому на живіт. Її волосся ловило тепле дихання принца. Вона усміхалася. Принц обережно обійняв її. Вони замовкли."
"— Доріане, — прошепотіла Селена, і він злегка клацнув її по носі. — Боляче, — ойкнула вона, кривлячи ніс."
"Дивно, але Кейн не спотворив їй обличчя. Була лише подряпини, які безслідно зникнуть. З раною на нозі справа стояла гірше. Схоже, до її шрамів додасться новий."
"— Ти про щось хотіла запитати? — поцікавився Доріан."
"Вона вслухалася в рівне биття його серця."
"— Коли ви забирали мене з Ендов’єра, ви справді вірили, що я виграю змагання?"
"— Звичайно. Інакше навіщо б я відправився в таку далечінь?"
"Селена хмикнула. Доріан обережно взяв її за підборіддя. Його очі були дуже знайомими. Просто вона їх дуже давно не бачила, а побачивши, одразу ж упізнала."
"— Щойно тебе привели тоді в зал, я одразу зрозумів: ти станеш переможницею, — прошепотів Доріан."
"У Селени приємно завмерло серце."
"— Але мушу тобі зізнатися: того, що сталося позавчора, я й передбачити не міг… Мені були противні ці змагання, але я вдячний долі, що вони привели тебе в моє життя. І поки я живий, я завжди буду дякувати долі за це."
"— Ти хочеш довести мене до сліз чи просто дурня валяєш?"
"Доріан нахилився й поцілував її. Селена не заперечувала, чого не можна було сказати про її щелепу."
"Король Адарлана сидів на скляному троні, постукуючи по підлозі ефесом Нотунга. Перед ним на колінах стояв Перангон і терпляче чекав. Нічого, нехай ще почекає."
"Селена Сардотін чесно виграла заключний поєдинок, але король поки не поспішав складати з нею договір і жаловати їй титул королівської захисниці. Ця дівчина звела близьку дружбу з його сином і принцесою Нехемією. Чи не ризикує він, призначаючи її на такий важливий пост?"
"Але капітан королівської гвардії довіряє цій дівчині, якщо не вагаючись врятував їй життя. Обличчя короля стало непроникним і нерухомим. Він і не збирався карати Шаола Естфола — хіба тільки щоб подивитися, як Доріан стане на захист свого дружка. Шкода, звичайно, що принц за натурою — книжковий черв’як, а не прирожденний солдат."
"І все ж він не безнадійний. У ньому відчувається чоловік, якого при належному старанні можна перетворити на воїна. Кілька місяців, проведених у бойових умовах, явно пішли б йому на користь. Шолом і меч здатні творити чудеса з найупертішими й непіддатливими. Зумів же Доріан показати свою силу й волю, коли вони говорили минулого разу… Якщо посильніше натиснути, з принца вийшов би чудовий генерал."
"Що ж стосується дівчини… щойно її рани заживуть… вона буде слухняно виконувати всі його накази. Вона прекрасно усвідомлює, чим ризикує. Тепер, коли Кейн убитий, Селена Сардотін — найкращий воїн, який у нього є."
"Король начертив знак на скляному підлокітнику трону. Він добре розбирався в «знаках долі», але такого, який спалахнув на лобі Селени, не бачив жодного разу. Він обов’язково дізнається, що це за знак. Якщо це вказівка на небезпечні справи чи здібності до пророцтва… повісити її він завжди встигне. Бачачи, як її трясло на арені, він майже схилявся до думки, що вона мусить померти. Але потім, коли він відчув злісні, повні люті очі мертвих… Вони б зробили це самі, і тут хтось втрутився й врятував її."
"Виходить, одні істоти іншого світу на неї нападали, а інші — оберігали."
"Поки що Селена йому потрібна. А коли він докопається до сенсу знака на її лобі… там видно буде. Зараз у нього є більш нагальні турботи."
"— Твоє поневолення Кальтени було цікавим, — порушив мовчання король."
"Перангон залишався на колінах."
"— Ти застосовував до неї особливу силу?"
"— Раніше. Зараз уже ні, як ви й веліли, — відповів герцог, крутячи на товстому пальці чорне обсидіанове кільце. — І потім, вона більше не потребує додаткового підхльостування. Бліда, знесилена. Додайте до цього мігрень, нападами якої вона страждає з отроцтва."
"Віроломна поведінка Кальтени була обурливою, але до її виплеску король нічого не знав про задуми Перангона. Виявляється, герцог замислив оголити її характер, щоб довести, з якою легкістю її можна пристосувати для їхніх цілей. Знай король заздалегідь, він би завадив цьому огидному лицедійству, що породило вельми неприємні запитання й ще неприємніші домисли."
"— Твої досліди над Кальтеною — розумний хід. З неї можна зробити сильну союзницю, причому вона й не здогадається про наш вплив. Я покладаю великі надії на особливу силу, — зізнався король, поглядаючи на своє чорне кільце. — Кейн показав цікаві властивості тілесних перетворень. Властивості Кальтени — іншого характеру. Вона здатна впливати на думки й почуття інших. Мені б хотілося в повній мірі перевірити дар Кальтени ще на кількох людях."
"— Частково я шкодую, що Кальтена виявилася такою податливою, — пробурмотів Перангон. — Вона хотіла скористатися мною, щоб зблизитися з вашим сином. Однак я не бажаю, щоб під дією особливої сили вона перетворилася на другого Кейна. Не приховую, я дуже сердитий на неї за гидотний спектакль, який вона собі дозволила. Навіть присутність вашої величності й радників її не втримала. І водночас мені б не хотілося занадто довго гноїти її у в’язниці."
"— Про це, мій друже, можеш не хвилюватися. Кальтена не залишиться в тюремній камері навічно. Коли скандал вщухне, а моя, так би мовити, захисниця займеться справою, ми дещо запропонуємо Кальтені. Відмовлятися в її становищі буде глупо, і вона погодиться. Але якщо ти сумніваєшся, чи заслуговує вона довіри, є способи керування нею."
"— Давайте спочатку переконаємося, що застінок вплинув на її умонастрій, — швидко вставив Перангон."
"— Звичайно, герцогу. Це всього лише моя пропозиція."
"Король замовк. Постоявши ще деякий час на колінах, Перангон підвівся."
"— Так, ось що ще…"
"Ехо рознесло королівські слова по тронній залі. Вогонь у величезному, схожому на розкриту пащу каміні спалахував і гас, і спалахи зеленого світла металися по похмурому простору."
"— Нам незабаром належить великі справи по всій Ерілеї. Готуйся. А свій замисел щодо ейлуейської принцеси залиш. Він привертає забагато уваги."
"Герцог мовчки кивнув, уклонився й вийшов із тронної зали."
"Селена вперлася в спинку стільця, поклала ноги на стіл і почала гойдатися, небезпечно балансуючи на задніх ніжках. Її м’язи за цей час встигли затвердіти, і гойдання слугувало їй чимось на кшталт вправи. Паралельно вона встигала читати книгу. Під столом мирно сопіла Швидконога. За вікнами яскраві сонячні промені частково розтопили сніг, і крапель наповнювала кімнату красивими переливами світла. Рани майже вже не турбували Селену, але ходила вона по-старому кульгаючи. Це не зменшувало в ній рішучості знову почати бігати щоранку."
"Від часу поєдинку минул тиждень. Фаліпа клопотала не покладаючи рук, звільняючи в гардеробній місце під нові вбрання. Ті самі, що Селена збиралася купити, коли зможе вільно виходити в місто й витрачати щедре жалування королівської захисниці. Але спочатку треба було підписати королівський договір… а це вже ніяк від неї не залежало."
"Оскільки Фаліпі було не до неї, більшу частину часу Селена проводила з Нехемією й Доріаном. Принц читав їй уголос, і читання затягувалися допізна. Засинала вона не одразу, а коли сон нарешті перемагав її, їй снилися слова давньої мови, давно забуті обличчя; снилися «знаки долі», що палають блакитним вогнем, адарланський король і скопище мерців, викликаних із глибин пекла. Прокинувшись, Селена старанно забувала сон і особливо все, що мало стосунок до магії."
"Ручка дверей зі скрипом повернулася. Селена завмерла. Невже її кличуть підписувати договір із королем? Але цього разу до неї прийшов не Доріан, не принцеса й навіть не хлопчик-паж. До спальні увійшов… Шаол."
"Швидконога радісно завиляла хвостом і кинулася йому назустріч. Селена ледь не перекинулася зі стільця. Ноги вона, звичайно, прибрала, і поривчастий рух нагадав їй про рану."
"Отримавши від Шаола дружнє почухування за вухами, цуценя повернулося під стіл, покрутилося там і знову лягло."
"Але чому капітан завмер біля дверей, наче вкопаний? Селена згадала, що весь її одяг складався з нічної сорочки, і почервоніла від його пильного погляду."
"— Як твої рани? — тихо запитав він."
"Тільки зараз до Селени дійшло, що капітан дивиться зовсім не на її ноги, а на пов’язки, що залишалися в неї на стегні."
"— Майже все зажило, — квапливо відповіла вона. — Пов’язки — це так, щоб мене жаліли."
"Селена спробувала усміхнутися, однак усмішки не вийшло."
"— Я тебе всього тиждень не бачив. А здається — ціла вічність минула… Ти-то сам як?"
"Карі очі Шаола зустрілися з її очима, і Селена миттєво перенеслася в часі назад. Вона відчувала під собою холодні плити веранди, чула регіт Кейна за спиною, але бачила Шаола, що опустився навпочіпки поруч із нею. У неї перехопило горло. Тоді її розум щось зрозумів, але сенс зрозумілого вислизнув від неї. Може, і це теж було галюцинацією."
"— Я… добре."
"Селена ступила до нього, лаючись на себе за те, що одягла занадто коротку сорочку."
"— Я хотів… вибачитися, що не зміг прийти раніше."
"Селена майже впритул підійшла до нього й здивовано вскинула голову. Уперше вона бачила Шаола без меча."
"— Тебе, напевно, справи не пускали."
"Шаол продовжував стояти, не роблячи жодного кроку вперед. Селена закинула за вуха вибиті пасма волосся. Потім зробила ще один маленький крок. Тепер, щоб бачити обличчя Шаола, їй довелося задерти голову. Очі в капітана були зовсім сумні."
"— Ти ж врятував мені життя. Двічі."
"— Я зробив те, що мусив зробити."
"— Я в тебе в боргу, — сказала Селена."
"— Не вигадуй. Нічого ти мені не винна, — напруженим, не своїм голосом відповів Шаол."
"Селена обережно взяла його руку в свої, але Шаол вирвався."
"— Я просто зайшов тебе провідати. Вибач, поспішаю, — пробурмотів він, і Селена одразу зрозуміла, що це брехня."
"— Дякую за те, що вбив Кейна, — сказала Селена й побачила, як він напружився всім тілом. — Я досі пам’ятаю своє перше вбивство. Мені воно важко далося."
"Шаол опустив очі."
"— Тому його вбивство й не виходить у мене з голови. Кажеш, важко? А мені це було легко. Розумієш? Вихопив меч і вбив його. Скажу тобі більше: я хотів його вбити. Він щось знав про твоїх батьків. Звідки?"
"— Сама не можу зрозуміти, — збрехала Селена."
"Але вона розуміла, прекрасно розуміла. Кейну були доступні області іншого світу й межа між світами. Він міг проникати в її розум, копирсатися в її спогадах і навіть у її душі. Можливо, Кейн знав про неї таке, про що вона й не підозрювала. Навіть зараз, знаючи, що Кейна більше немає, Селена похолола."
"Обличчя Шаола трохи відтаяло."
"— Жахливо, що вони загинули… ось так."
"Зусиллям волі Селена замкнула всі свої почуття, залишивши тільки голос."
"— Це було дуже давно. У вісім років багато що сприймається по-іншому… Вони любили спати з відчиненим вікном. А тієї ночі йшов дощ, і тому було дуже темно. Я відчула, що навколо мене мокро, але вирішила… це через дощ. Мені дуже хотілося спати, і я заснула. А вранці прокинулася й зрозуміла: ніякий це не дощ."
"Селена ковтнула повітря. Вона пам’ятала свої лікті й плечі, забризкані кров’ю батьків."
"— Невдовзі після цього мене знайшов Аробінн Хемел."
"— Усе одно це жахливо."
"— Кажу тобі, вже багато років минуло. Я й облич їх не пам’ятаю."
"Вона знову збрехала. Вона прекрасно пам’ятала кожну рисочку батьківських облич."
"— Іноді я навіть забуваю, що в мене були батьки."
"Його кивок більше означав, що він почув її слова. Їхній сенс залишався для Шаола незрозумілим."
"— Шаоле, ти дуже багато зробив для мене. Я не тільки про Кейна. Загалом. Коли ти…"
"— Мені треба йти, — глухо перебив її Шаол, повертаючись до дверей."
"— Зачекай!"
"Селена схопила його за руку й розвернула обличчям до себе. Його очі налякано блиснули. Вона обвила руками його шию й притиснулася до нього всім тілом. Капітан намагався відсторонитися, але вона не відпускала його, забувши про ниючі рани. Потім, наче отямившись, Шаол теж обійняв її й притягнув до себе. Селена заплющила очі й слухала його дихання, не розуміючи, де закінчується вона й починається він."
"Його дихання приємно зігрівало їй шию. Шаол нахилив голову й уткнувся щокою в її волосся. Серце в неї калатало дуже швидко, але душу охопило дивне спокій. Селена раптом відчула: вона готова стояти так цілу вічність, не помічаючи, як навколишній світ перетворюється на руїни, а потім і на попіл. Вона згадувала пальці Шаола, що тягнулися до неї крізь крейдяне коло арени."
"— Як ви тут? — почувся з дверей голос увійшовшого Доріана."
"Шаол поспішно відсмикнувся, ледь не впустивши Селену."
"— Ми? Чудово, — з неприродною бадьорістю відповів він."
"У повітрі одразу стало холодно. Селена зябко здригнулася. Їй стало неуютно, наче її з теплої постелі витягли на мороз. Шаол квапливо кивнув принцу й пішов, а з ним із душі Селени пішла й легкість."
"Доріан дивився на неї, але Селена продовжувала дивитися на двері, хоча й знала, що Шаола давно вже немає в її покоях."
"— Думаю, він ще нескоро оговтається після вбивства Кейна, — сказав Доріан."
"— Ще б пак, — досить різко відповіла Селена."
"Доріан запитально підняв брови."
"— Вибачте, — спохопилася Селена. — Уявила, як йому зараз."
"— По-моєму, я вас застав у самому розпалі… сам не знаю чого, — обережно зауважив принц."
"— Вам здалося, — в черговий раз збрехала Селена. — Просто мені захотілося підтримати Шаола."
"— Шкода, що він так поспішно пішов. Залишився б — дізнався б добру новину."
"У Селени звело живіт."
"— Батько завершив усі проволочки з твоїм договором. Завтра ти його підпишеш у залі засідань королівської ради."
"— Це означає… я офіційно стаю королівською захисницею?"
"— Так. Виходить, батько не так уже сильно тебе ненавидить, як могло здатися. Просто диво, що складання договору не затягнулося на місяці, — сказав Доріан і підморгнув."
"Чотири роки. Чотири роки підневільної служби, а потім вона буде вільна. Але чому Шаол утік, як хлопчисько? Селена глянула на двері, прикидаючи, вистачило б у неї зараз сил його догнати."
"Доріан обійняв її за талію."
"— А ще це означає, що ми будемо разом, принаймні цілих чотири роки."
"Він нахилився й поцілував її, але Селена обережно вирвалася з його обіймів."
"— Доріане, я ж тепер королівська захисниця, — давлячись від сміху, сказала вона."
"— З цим ніхто не сперечається, — відповів принц, знову наближаючись до неї."
"Але Селені не хотілося ні нових обіймів із ним, ні нових поцілунків. Вона повернулася до вікна, яскраво залитого сонцем. Світ знову був відкритий для неї. Вона зуміла переступити через ненависну крейдяну межу."
"— Селено, а хіба це щось змінює? — щиро недоумів Доріан. — Мабуть, тільки те, що тепер біля твоїх покоїв не будуть товпитися вартові."
"— Отримавши титул королівської захисниці, я вже не зможу бути з вами."
"— Селено, я розгадав твій жарт, — засміявся принц. — Тепер нам буде легше тримати все це в таємниці."
"— У мене й так вистачає таємниць, і ще одна мені не потрібна."
"— Не хвилюйся, я знайду спосіб розповісти про нас батькові. І матері, — не надто впевнено додав Доріан і скривився."
"— Доріане, навіщо нам усе це? У мене лише титул звучить красиво. Насправді я — підневільна вашого батька. А ви — спадковий принц."
"Вона говорила те, що думала. Якщо їхні стосунки перейдуть за межу обіймів і поцілунків, це тільки ускладнить справу, коли настане час покинути замок. Приймати ласки Доріана, будучи служницею його батька? У яке становище це її поставить? І Доріана теж. Як би він ні захоплювався нею, у спадкового принца — свої зобов’язання, ухилитися від яких він не вправі. Так, вона й зараз хотіла його, їй було добре з ним, але вона розуміла: їхні тривалі стосунки все одно погано закінчаться і насамперед — для неї."
"Сапфірові очі Доріана потемніли."
"— Значить, ти більше не хочеш бути зі мною?"
"— Доріане, давайте не закриватися від правди. Через чотири роки я все-таки покину замок. Я не знаю, яким буде кінець наших стосунків, якщо вони продовжаться. Думаю, вони лише ускладнять життя кожного з нас."
"Сонце приємно гріло їй спину. Селена відчувала, як починає йти тяжкість, що тиснула їй на плечі."
"— Зрозумійте мене правильно, Доріане. Через чотири роки я отримаю свободу. Спробуйте це зрозуміти. Я ж і до арешту не відчувала себе вільною. Я ніколи не була вільною й дуже хочу відчути, що ж це таке, коли ти по-справжньому вільна."
"Селена усміхалася. Принц розтулив було рот, але промовчав і лише дивився на її усмішку."
"— Як побажаєш, — тихо відповів він."
"Вона не шкодувала про зроблений вибір, однак ці два слова викликали в ній дивну досаду."
"— Але я хочу залишитися вашим другом."
"— Назавжди, — сказав Доріан, засовуючи руки в кишені."
"Селені стало трохи шкода його. Може, взяти його за руку? Чи поцілувати в щоку? Але слово «вільна» дзвоном дзвеніло в ній усередині, відгукуючись у всіх закутках її єства, і їй було не стримати усмішки."
"Доріан теж усміхнувся, однак його усмішка вийшла натягнутою."
"— Думаю, Нехемія вже поспішає сюди, щоб розповісти тобі про договір. Принцеса сильно розсердиться, коли дізнається, що я її випередив. Ти вже вибачся за мене, добре?"
"Доріан узявся за дверну ручку, але вагався йти."
"— Вітаю тебе, Селено, — тихо сказав він."
"Вона не встигла відповісти. Двері за принцом тихо зачинилися."
"Залишившись сама, Селена підійшла до вікна, притискаючи руку до шалено калатаючого серця."
"— Вільна, — шепотіла вона, без кінця повторюючи це дорогоцінне слово."

#Епізод 28

"Через кілька годин Шаол знову з’явився в покоях Селени й тепер стояв біля дверей у її їдальню. Він сам не до кінця розумів, навіщо прийшов сюди. Точніше, розумів, тільки не хотів собі зізнаватися. Шаол скрізь розшукував Доріана й ніде не міг знайти. Він відчував необхідність пояснитися щодо тієї дивної сцени, мимовільним свідком якої виявився принц. Адже все було не так, як Доріан міг подумати."
"За минулий тиждень король ледь удостоїв його парою слів. Ім’я Кейна взагалі не згадувалося. Це Шаола не дивувало. Хто такий Кейн? Пішак у грі. Розважив короля, і буде з нього. І нічого порівнювати якогось солдата з капітаном королівської гвардії."
"Але Кейн мертвий, бо Шаол убив його. Очі цього верзили ніколи вже не розплющаться й не подивляться на світ, бо Шаол убив його. Убив не просто так, не через дурну сварку. Убив за крайньої необхідності… але вбив."
"Рука капітана звично ковзнула до піхов. Потім він згадав, що всі ці дні ходив без меча. Тоді, добрівши до своїх кімнат, він жбурнув меч у кут. Дякувати, хтось змив із зброї всю кров. Напевно, гвардійці, які відвели його з веранди. Удома вони налили йому великий келих найміцнішого питва, яке змогли знайти, і мовчки посідали. Потім, переконавшись, що їхній командир не накоїть дурниць, пішли, не чекаючи, коли він їх подякує."
"Шаол провів рукою по коротко стриженому волоссю й увійшов."
"Селена ліниво розправлялася з обідом. Капітана вона явно не чекала."
"— Два візити за один день? — здивувалася Селена, опускаючи виделку. — Чим я зобов’язана такій увазі?"
"— Де Доріан? — похмуро запитав Шаол."
"— Цього я не знаю. Як бачиш, тут його немає."
"— А я думав, у цей час він завжди буває тут."
"— Раніше бував. Але тепер не буде."
"Шаол підійшов до столу й завмер із запитанням:"
"— Чому?"
"Селена скатала хлібну кульку й відправила собі в рот."
"— Бо я це припинила."
"— Що саме?"
"— Я тепер — королівська захисниця. Залишилося лише договір підписати. Думаю, ти розумієш, що мені було б вкрай непристойно перебувати в близьких стосунках із принцом."
"Її сині очі спалахнули. Від легкого наголосу, зробленого нею на слові «принц», у Шаола завмерло серце."
"Капітан з труднощами усміхнувся й сказав:"
"— А я все чекав, коли ти остаточно одужаєш."
"Він раптом подумав: які почуття відчувала Селена після чергового вбивства? Мучилася? Згадувала свої перепачкані кров’ю руки? Чи вона вміла вбивати, не пачкаючись у крові жертв?"
"Шаол знову, вкотре, здивувався, що доля зробила її асасином. При всій її браваді, при всьому її їдкості й гордовитих позах… її обличчя зберігало якусь ніжність. Надію на те, що вона не встигла перетворитися на живе знаряддя вбивства… Дівчина, що побувала в Ендов’єрі й не розучилася сміятися, не могла любити ремесло асасина."
"Селена дивилася на нього, крутячи між пальцями кінчик локона. Вона так і не переодяглася, і занадто коротка нічна сорочка при кожному русі задравалася вгору. Але капітан дивився не на її ноги, а на обличчя."
"— Чого ж ти стоїш? Сідай. Соромно святкувати одній."
"Селена лукаво усміхалася. Те, що було на поєдинку, те, що було незабаром після поєдинку… Кейн… це ще довго не відпустить його. Але зараз…"
"Шаол висмикнув стілець і сів навпроти неї. Селена простягнула йому келих вина."
"— За чотири роки, що залишилися до моєї повної свободи."
"— За тебе, Селено, — відповів Шаол, піднімаючи свій келих."
"Їхні очі зустрілися, і тепер йому не довелося змушувати себе усміхатися. Напевно, чотири роки поруч із нею — це занадто мало."
"Селена стояла в склепі. Вона знала, що спить. Їй часто снився цей склеп. Іноді уві сні Селена знову вбивала риддерака чи опинялася замкненою всередині саркофага Еліани. Іноді їй снилася золотоволоса молода жінка з розмитими рисами обличчя й важкою короною на голові. Але сьогодні… сьогодні вони були з Еліаною вдвох. Склеп був залитий місячним світлом. Рештки вбитого риддерака кудись зникли."
"— Бачу, ти швидко одужуєш, — сказала королева, спираючись на стінку свого саркофага."
"Селена зупинилася в дверях. Сьогодні на Еліані замість обладунків знову було її сяюче плаття. Риси обличчя втратили різкість."
"— Так, одужую, — відповіла Селена, але все ж оглянула себе."
"Уві сні вона була цілком здоровою — навіть слідів від ран не залишилося."
"— А я не знала, що ви воїтелька, — сказала Селена, кивком підборіддя вказуючи на поблискуючий у місячному світлі Дамаріс."
"— Занадто багато, пов’язане з моїм ім’ям, було забуто чи замінено дурними казками. — Сині очі Еліани блищали від гніву й смутку. — Я билася у війнах із демонами. Ми з Гавіном разом боролися проти Еравана. Там ми й полюбили одне одного. А ваші легенди уявляють мене зніженою дівою, яка сиділа в вежі й своїм магічним намистом допомагала принцу здобувати перемоги."
"— Пробачте. Я не знала, — прошепотіла Селена, торкаючись амулета."
"— Ти здатна бути іншою, — тихо сказала Еліана. — Великою. Ти здатна перевершити й мене, й будь-кого з нас."
"Селена розтулила рот, але слова не вимовлялися."
"Еліана ступила до неї."
"— Твоїх сил вистачить на те, щоб змусити тремтіти зірки, — продовжила королева. — Ти зможеш усе, якщо тільки насмілишся. У глибині душі ти й сама це знаєш і найбільше боїшся своєї сили."
"Селені раптом захотілося вискочити зі склепу й тікати без оглядки. Сяючі сині очі давньої королеви були такими ж примарними, як її прекрасне обличчя."
"— Кейн довгий час наповнював ваш світ злом. Ти зуміла знайти й перемогти це зло. Тепер ти королівська захисниця. Ти виконала моє повеління."
"— Я виконувала не ваше повеління, — заперечила осміліла Селена. — Я билася за свою свободу."
"Еліана зрозуміло усміхалася, і від цієї усмішки Селені хотілося кричати, але вона старалася нічим не видавати своїх почуттів."
"— Ти права, але лише частково. Пам’ятаєш, як Кейн зірвав із твоєї шиї амулет і ти відчула себе беззахисною? Пам’ятаєш свої заклики про допомогу? Ти ж кликала й знала, що тобі відповість. Що я тобі відповім."
"— Тож ви вирішили врятувати мене заради своїх цілей? — запитала Селена. — Скажіть, навіщо ще мені ставати королівською захисницею, як не заради власної свободи?"
"Еліана підставила обличчя місячному світлу й відповіла:"
"— Є люди, які дуже чекають, коли ти їх врятуєш. Їм це потрібно нітрохи не менше, ніж тобі під час поєдинку з Кейном. Можеш заперечувати. Можеш говорити, що ти не знаєш таких людей. Когось поки не знаєш, але тут, у замку, у тебе є друзі, і їм дуже потрібна твоя присутність. Насамперед вона потрібна Нехемії. Я перебувала в довгому, нескінченному сні, але мене розбудив голос."
"— Чий голос? — насторожилася Селена."
"— Це не був голос однієї людини. Це було безліч голосів, що злилися в один. Одні шепотіли, інші кричали, треті навіть не здогадувалися, що кличуть мене. Але всім їм потрібна твоя допомога."
"Еліана доторкнулася до лоба Селени, і там знову спалахнув блакитним вогнем «знак долі». Селена його не бачила, але помітила яскравий блакитний відблиск, що осяяв обличчя давньої королеви."
"— Коли будеш готова… коли й ти почнеш чути цей єдиний голос багатьох, тоді зрозумієш, чому я прийшла до тебе й чому залишалася поруч із тобою, незважаючи на всі твої спроби випхнути мене зі свого життя."
"У Селени защипало в очах. Вона наблизилася до королеви. Еліана сумно усміхалася."
"— Поки той день не настав, ти перебуваєш саме там, де й мусиш перебувати. Будучи поруч із королем, ти побачиш, у чому потребують люди й що потрібно робити. А поки — святкуй свою перемогу."
"Невже Еліана зажадає від неї чогось іще? Ця думка приводила у відчай, однак Селена кивнула. Більше нічого не тримало її в склепі, і вона вже приготувалася йти, але потім озирнулася через плече. Королева по-старому стояла в смузі місячного світла й сумно усміхалася."
"— Дякую вам, Еліано, що врятували мені життя, — подякувала Селена."
"Еліана схилила голову."
"— Кровні узи неможливо розірвати, — прошепотіла вона й зникла."
"Ехо кілька разів повторило її шепіт."
"Наступного дня Селена підходила до скляного трону, обережно поглядаючи на короля й зібраних. Кілька місяців тому вона, ще більше тремтячи, стояла тут разом із двадцятьма трьома іншими претендентами. Як і тоді, в каміні буяло зеленкувате полум’я, а за столом сиділи тринадцять королівських радників, і кожен дивився на неї. Однак зараз картина суттєво змінилася. Із претендентів залишилася вона одна; і то вже не претендентка, а переможниця."
"Стоявший біля трону Доріан усміхнувся їй. «Будемо сподіватися, що це добрий знак», — подумала Селена. Але усмішка принца й надія не могли подолати жаху, що стиснув серце Селени, коли король устремив на неї темний погляд і мовчки стежив, як вона йде до трону. Золотавий поділ її сукні м’яко шарудів по мармуру, і це був єдиний звук у залі. Селена йшла, щільно притиснувши руки до корсажу. Руки завжди видавали її хвилювання."
"Зупинившись на належній відстані, Селена вклонилася. Шаол, що стояв поруч із нею, теж уклонився. Мабуть, капітан перебував до неї ближче, ніж вимагали правила етикету."
"— Ти явилася сюди, щоб підписати договір, — сказав король, і від його голосу в неї затріщали кістки."
"«Чому ця звіроподібна людина володіє такою могутньою владою?»"
"— Так, ваше величество, — якомога смиреннішим тоном відповіла Селена, стараючись дивитися на королівські чоботи."
"— Становися моєю захисницею, і ти отримаєш свободу. Один рік ти скинула, сторгувавшись із моїм сином на чотирирічний термін. Хоча я досі не розумію, навіщо йому знадобилося торгуватися з тобою."
"Король сердито глянув на Доріана. Принц прикусив губу, але промовчав."
"Її серце смикалося, наче поплавець. Їй доведеться виконати будь-який наказ короля. Найогидніші, найвідразливіші доручення. Але через чотири роки вона звільниться й отримає право на власне життя, без страху бути покараною чи відправленою в рабство. Вона зможе почати життя з чистого аркуша, далеко від Адарлана. Вона покине це жахливе королівство."
"Селена поки не знала, як вона зустріне перший день своєї повної свободи. Може, просто усміхнеться, а може, розрегочеться на повний голос чи розридеться. Можливо, її потягне пуститися в танок. Чи просто стати біля вікна. Грошей, що вона накопичить за чотири роки служби, їй вистачить до старості. Їй більше не знадобиться вбивати. Вона зможе попрощатися з Аробінном і назавжди покинути межі Адарлана."
"— Ти що ж, навіть не збираєшся мене дякувати? — прорычав король."
"Селена відвела глибокий уклін, ледь стримуючи радість. А адже вона перемогла його. Вона, що вчинила злочин проти його імперії, не зникла в Ендов’єрі. Вона повернулася й стала переможницею."
"— Ваше величество, я сповнена глибокої вдячності за надану мені честь і цей дар. Я готова смиренно вам служити."
"— Брехня тобі не личить, — зневажливо хмикнув король. — Принесіть договір."
"Хтось із радників услужливо поклав на стіл аркуш пергаменту. Селена дивилася на перо, чорнильницю й порожнє місце в нижньому рядку, де їй належало вписати своє ім’я."
"Очі короля спалахнули, але Селена мовчки витримала його погляд. Знаючи характер короля, вона могла побоюватися будь-яких несподіванок. Один лише незадоволений жест, один рух, який він вважатиме загрозливим, і її прямо звідси поволокуть на шибеницю."
"— Умови договору не обговорюються. Коли я велю тобі щось зробити, ти це зробиш у точності, як я наказав. Мої накази теж не обговорюються. Мені нема чого пояснювати тобі свої задуми. Якщо ж тебе раптом схоплять, ти будеш зобов’язана до останнього подиху заперечувати, що перебуваєш у мене на службі. Це зрозуміло?"
"— Мені все зрозуміло, ваше величество."
"Король підвівся, зійшов із помосту. Доріан здригнувся, однак Шаол ледь помітно похитав головою."
"Селена вперлася поглядом у підлогу. У неї не вистачало сміливості дивитися на короля, коли він перебував поруч."
"— А тепер, асасине, слухай уважно й запам’ятовуй те, що я зараз скажу."
"Селена раптом відчула себе маленькою й крихкою, наче прутик."
"— Якщо ти раптом не виконаєш хоча б одне моє завдання чи раптом «забудеш» повернутися, тобі доведеться дорого заплатити за своє свавілля. — Король знизив голос майже до шепоту: — Якщо ти насмілишся не повернутися з завдання, на яке я тебе посилав, твого дружка-капітана… — король зробив паузу, — я накажу… стратити."
"Селена округлими очима дивилася на порожній трон."
"— Якщо ти й після цього не повернешся, я накажу стратити Нехемію. А потім, одного за одним, її братів. Слідом за ними я велю живцем закопати їхню матір. І не думай, що тобі вдасться мене обдурити чи перехитрити."
"Селена відчувала на собі його злорадну усмішку."
"— Картина тобі ясна? — запитав король, відсуваючись від столу. — Підписуй."
"Селена подивилася на пробіл у нижньому рядку, потім беззвучно зітхнула, подумки прочитала молитву про свою душу й вивела своє ім’я. Кожна наступна літера давалася їй важче попередньої. Підписавши договір, вона не дивлячись відкинула перо."
"— Добре. Тепер можеш іти, — сказав король, киваючи на двері. — Коли знадобишся, я дам знати."
"Він знову сів на трон. Селена вклонилася, цього разу навіть глибше, стараючись не відводити очей від його обличчя. Тільки одного разу вона крадькома глянула на Доріана й встигла помітити смуток у його сапфірових очах. Але вже в наступну мить на обличчі принца з’явилася усмішка. Селена відчула, як Шаол міцно схопив її за руку."
"Король виявився хитрішим, ніж вона думала. Тепер від її послуху його волі залежало не тільки її власне життя, а й життя Шаола, Нехемії та рідних принцеси… Коли вона разом із Шаолом виходила із зали, її ноги відчували дивну легкість і водночас — неймовірну тяжкість."
"А зовні виє й гуде вітер, норовлячи перекинути скляну вежу, але всі його зусилля були марними. Скляні стіни не поступалися міцністю кам’яним."
"Кожен крок, що віддаляв Селену від тронної зали, повертав їй життя. Шаол мовчав, доки вони не спустилися в кам’яний замок."
"— Ну що, захиснице? — запитав він."
"Меча на поясі в нього по-старому не було."
"— Слухаю, капітане."
"— Тепер ти щаслива? — запитав Шаол, усміхаючись кутиками рота."
"Селена теж усміхнулася."
"— Можливо, я щойно продала свою душу, і все-таки… так. Я щаслива, наскільки це можливо в моєму становищі."
"— Королівська захисниця Селена Сардотін, — задумливо промовив Шаол."
"— І як тобі?"
"— А що, звучить красиво, — відповів він, знизуючи плечима. — До речі, хочеш дізнатися про свою першу місію?"
"Селена зазирнула в його золотаво-карі очі, що таїли щось, у чому вона розбереться потім."
"— Завтра розкажеш, — усміхнулася Селена, беручи його під руку."

return
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

        if float((char_pos[0] + (char_pos[2] / 2))/config.screen_width) < 0.5:
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




image селена = At("images/Selena/селена.png", sprite_highlight("селена"))
image дорін = At("images/Dorin/Дорін.png",   sprite_highlight("дорін"))
image шаол = At("images/Shaol/Шаол.png", sprite_highlight("шаол"))
image кальтена = At("images/Kaltenna/Кальтена.png", sprite_highlight("кальтена"))
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
    scene коридорпалацу
    with fade

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
"Вони зупинилися перед високими дверима, прикрашеними золотими візерунками. Двері відчинилися, і світло тронної зали залило простір."#
"На підвищенні сидів принц Дорін. Його погляд був уважний, але сповнений цікавості — він розглядав ту, про кого чув легенди."
"Поруч стояв герцог Перрантгон, його усмішка була холодною, а очі — пильними, наче він оцінював здобич."
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
"Коли Селена нарешті впала на ліжко після зустрічі з принцом, сон не йшов. Тіло горіло від втоми, але біль і збудження не давали заснути."
"Гаряча вода й мило стали справжньою тортурою. Дві кремезні служниці терли її так, ніби мали зішкребти до кісток. Шрами на спині палали вогнем, обличчя здавалося стертим до черепа."
"Шаол зняв кайдани перед миттям. Ключ клацнув, залізо розімкнулося, окови гупнули на підлогу. Але примарні ланцюги залишилися — тепер у повітрі. Селена з насолодою крутила зап’ястями й ворушіла пальцями ніг, попри біль."
"Лежати на справжній перині з шовковими простирадлами було дивно. Під головою — подушка, а не власна рука."
"Шлунок відвик від нормальної їжі. Вечеря — смажена курка — не мала смаку. Після кількох шматочків Селену ледь не вивернуло. Вона вискочила з-за столу, тримаючись за живіт."
"Хотілося наїстися досхочу. Але шлунок розучився. Нічого. У Рафтхолі вона наздожене. Чисте тіло показало правду: форми зникли. Лише кістки, обтягнуті шкірою."
"Селена ледь не заплакала. Перевернулася на спину — шрами знову занили. У дзеркалі — чужа жінка: вилиці гострі, очі запалі, щелепа випирає. Вік не визначити."
"Селена закусила губу. Сльози не допоможуть. Завтра — не шахта, а Рафтхол. Вона буде їсти. Тренуватися. Стане сильною. Переможе всіх. Доведе, що досі — найкраща асасин Адарлану."
"З цими думками вона заснула."

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

"Ворота. Проїзд крізь товщу стіни — темний, гулкий. Потім зовнішні — з написом Ендов’єр."
"Ворота зачинилися. Пекло позаду. Селена смикнула ланцюг — перевірила. Шаол глянув пильно. Вона насмішкувато знизала плечима й відпустила."

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
"Караван зупинився на галявині. Шаол від’єднав ланцюг, різко смикнув — Селена змушена була зіскочити."
show селена at left, size_selena, appear_fade 
show шаол at right, size_shaol, appear_fade 
sh "Привал."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 

#Епізод 3

"Селена мотнула головою, відкидаючи з обличчя пасмо волосся, й рушила за капітаном. Якби вона зараз вирішила втекти, починати треба було б із Шаола. "
"Спокуса майнула, але кайдани й озброєні гвардійці стримували сильніше. Усі вони, як і вона, вміли вбивати без роздуму."
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
"На нічліг їй поставили маленький шатер, оточили охороною. Кайдани не зняли, але ланцюг тепер тримав гвардієць. Селена провалилася в сон без снів."
"Прокинулася — і не повірила очам. Біля ліжка лежали білі квіточки. На землі — сліди маленьких ніг. Селена швидко затерла сліди, квіти сховала в сумку."
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
"У розриві хмар блиснуло сонце. Між деревами з’явився скляний шпиль, потім три, потім ще півдюжини. Кожен прагнув проткнути небо."
"З вершини пагорба відкрився вид на головний шедевр Адарлану — скляний замок Рафтхолу."
"Величезне створіння. Місто зі скляних веж, мостів, сходів, переходів, залів, коридорів. Збудований поверх старого кам’яного замку."
"Селена згадала, як бачила його вперше — вісім років тому, десятирічною. Замок здавався без смаку. Гроші викинуті, таланти марно витрачені."
"Вона теребила бірюзовий плащ, боялася порвати чулки й забруднити червоні оксамитові черевички. Але думки були лише про людину, яку вона вбила три дні тому."
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
"Того вечора капітан більше не говорив — лише віддавав накази."
"Селена прокинулася від руки на горлі. Знову сон — вона в загальній могилі Ендов’єра, жива серед мертвих. Чіпляється за слизькі руки й ноги, але трупи тягнуть униз. Кричить — ніхто не чує."
"Вона сіла, обхопивши коліна. Сон. Лише сон. Дихала глибоко. Вдих-видих. Запрокинула голову, упершись підборіддям у коліна."
"Ніч тепла не по сезону — спали під відкритим небом. Замок світився зеленавим пульсуючим світлом над сплячим містом."
"Селена уявила: світ засинає в сяйві замку. Гори піднімаються й руйнуються. Рослини обвивають будинки, ховають місто під листям і колючками. Вона — єдина, хто прокинувся."
"Вона сиділа, закутана в плащ. Переможе в змаганнях. Послужить королю. Зникне. Не думатиме про замки, владарів, асасинів."
"Не правитиме містом. Магія мертва. Фе вигнані або вбиті. Більше ніяких державних справ. Ніяких казок про призначення. Вона з них виросла."

#Епізод 4

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
"Процесія в’їхала в торгову частину міста. Над дахами височів скляний замок — настільки високий, що верхні вежі видно лише задерши голову."
"Далі шлях пролягав набережною Авері. Біля причалів стояли кораблі, всюди валялися сплутані сіті й канати. Матроси голосно перегукувалися — їм було ніколи дивитися на процесію."
"Селена замилувалася парусниками, коли раптом почула знайомий звук хлиста."
"Вона повернула голову. З торгового корабля по сходнях зганяли рабів. Як завжди — скуті спільним ланцюгом, очі в землю, байдужі до всього."
"Такі обличчя вона надивилася в Ендов’єрі досхочу. Більшість — полонені з завойованих країн. Найупертіших карали показово, решту — в ланцюгах на користь королівства."
"У гавані рабів було повно — видавав погляд: у землю чи в небо, ніколи просто перед собою."
"Селені раптом захотілося зістрибнути з коня, кинутися до них і крикнути, що вона не має жодного стосунку до двору спадкоємного принца. Не так давно вона сама була рабинею соляних копалень, і по її спині гуляли батоги наглядачів."
"Можливо, в Ендов’єрі зараз рідні чи друзі цих нещасних. Хотілося сказати: два роки тому вона звільнила майже дві сотні рабів, що належали Предводителеві піратів. Нехай знають — вона не з породи адарланських чудовиськ."
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
"Спадкоємний принц стримав слово. Покої Селени справді були в кам’яній частині замку. Більші, ніж вона уявляла: спальня з умивальнею й гардеробною, затишна їдальня, кімната для ігор і музикування. Скрізь витончено розставлені кушетки й м’які стільці."
"Переважали два кольори: малиново-червоний і золотий. Спальню прикрашала величезна старовинна шпалера. З балкона відкривався вид на фонтан у саду."
"Все виглядало приємно — окрім стражників унизу."
"Селена нетерпляче чекала, коли Шаол нарешті піде. Поки він водив її кімнатами, вона встигла порахувати вікна — дванадцять."
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
"Капітан пройшов крізь скляні двері в сад."
show шаол at right, size_shaol, appear_fade 
show селена at left, size_selena, appear_fade 
sh "Це б’ють годиники на вежі."
show селена at left, size_selena, disappear_fade 
show шаол at right, size_shaol, disappear_fade 
"Селена подолала замішання, і, на щастя, скоро гуркіт припинився."
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
"Селена покосилася на важкі залізні ручки у формі кігтистих лап. Капітан неохоче штовхнув масивні двері. На стінах блищали канделябри — в деяких горіла по одній свічці. Підлога — чорно-білий мармуровий шаховий візерунок."
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
"Селену розбудив огидний бій годин на чорній вежі. Крізь сон вона порахувала удари. Полудень. Вона протерла очі й сіла на ліжку. Де ж Шаол? І коли почнуться змагання? А може, тому він і не прийшов її будити, що змагання перенесли на інший день?"
"Селена вистрибнула з ліжка, виглянула за двері, потім подивилася у саду з балкону."
"Думки перервалися появою трьох жінок, що вийшли з-за живої огорожі. Безтурботно балакаючи, вони йшли до фонтану. Жінки були майже її ровесницями, гарно вбрані, та, що йшла посередині — помітно вирізнялася вишуканістю вбрання. Обидві супутниці в скромніших блідо-блакитних сукнях скоріше за все були служницями."
"Красунька в червоному церемонно розправила поділ свого плаття."
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
"Коли всі троє зникли, «принцева блудниця» вбігла до спальні й через вартових покликала служниць, звелівши принести їй найгарніший наряд, який вони знайдуть."
"Декілька годин потому Селена стояла перед дзеркалом, дивилася на своє відображення й усміхалася. Під корсажем найгарнішого плаття сховано саморобний кинджал, зроблений напередодні з кістяних шпильок."
"Тихо відчинилися двері, і в дзеркалі з’явилося відображення Фаліпи. Селена спробувала надати обличчю байдужий вираз, але служниця одразу зрозуміла, чим займалася колишня в’язниця."
show фаліпа at right, appear_fade 
f "Шкода, що ти… у такому становищі. Тобі б нічого не коштувало вскружити голову якомусь молодому аристократу й вийти за нього. А якщо постаратися — то й його високості."
show селена at left, size_selena, appear_fade 
c "Здається, про це вже пліткують. Вранці я підслухала розмову в саду. Одна особа казала, що принц привіз мене сюди для забави. А я-то думала, весь двір уже знає про це дурне змагання."
f "Наберися терпіння, через тиждень усе забудеться. Варто принцу звернути увагу на якусь жінку — і двір почне шепотітися про неї. І не сприймай ці слова за образу, моя мила. Спадкоємного принца постійно оточують гарні жінки. Тобі має лестити, що тебе приймають за його коханку."
c "А мені це не лестить і не польстить."
f "Краще називатися коханкою, ніж асасином."
show фаліпа at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Селена хотіла насупитися, але, глянувши на Фаліпу, засміялася."
show фаліпа at right, appear_fade 
show селена at left, size_selena, appear_fade 
f "Усмішка тобі дуже пасує. Ти стаєш гарнішою. І навіть молодшою — хоч тобі зараз це навряд чи хочеться."
c "Можливо, ви маєте рацію."
show фаліпа at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Зітхнула Селена й плюхнулася на рожево-ліловий диван."
show фаліпа at right, appear_fade 
show селена at left, size_selena, appear_fade 
f "Негайно встань! Ти помнеш сукню."
c "Але я не можу годинами стояти. Особливо в такому взутті, я що, і їсти маю стоячи?"
f "Потерпи ще трохи. Я хочу почути від інших, яка ти прекрасна в цьому вбранні."
c "Хто вам це скаже? Ніхто не знає, що ви моя служниця."
f "Помиляєшся, люба. Усі знають, що мене призначили прислужувати новій коханці принца, яку він привіз до Рафтхолу."
show фаліпа at right, disappear_fade 
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
"Руки Селени налилися свинцем. Вона забула й про садна на ногах, і про ребра, нещадно стиснуті корсажем. Селена з капітаном опинилися на початку довгого коридору. Майбутня королівська захисниця ледь дихала."
"У Селени крутилася голова. Бажаючи зрозуміти, де вони, вона глянула в найближче вікно. Земля була далеко-далеко внизу. Вони прийшли в скляну частину замку — і це Селені дуже не сподобалося. Що завгодно, тільки не стояти в скляному замку."
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
"У кінці коридору, біля масивних скляних дверей, Селена помітила чотирьох гвардійців. Капітан повільно підвів її до дверей. У ту ж саму мить двері розчинилися. Капітан і Селена опинилися в людній залі."

#Епізод 6

"Відчуття сутінків тривало мить, бо зала освітлювалася безліччю канделябрів і люстр. Селена поквапливо озирнулася, намагаючись уявити розміри зали. Вікон у ній не було — лише скляні стіни."
"Ліворуч майже всю стіну займав гігантський камін. Селена старалася не дивитися на його палаючу зубасту пащу. Полум’я мало дивний зеленкуватий відтінок."
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
K " Питання є? – спитав король."
show король at right, disappear_fade 
"Сам його тон підказував, що будь-яке, навіть найневинніше питання може коштувати відправки на шибеницю. Претенденти мовчали. Знать — теж."
show король at right, appear_fade 
K "Ну, раз питань немає, дозволяю всім розійтися. І пам’ятайте: вас зібрали тут, аби примножити мою славу й славу моєї імперії. А тепер — ідіть. Усі геть."
show король at right, disappear_fade 
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
"Доріан усміхнувся."
show дорін at right, appear_fade 
show селена at left, size_selena, appear_fade 
pr "Радий, що споглядання твоїх майбутніх суперників не позбавило тебе зухвалості. До речі, як тобі Кейн?"
c "Спитайте у Перрантгона, чим він годує свого улюбленця, і нехай мені готують таку ж їжу."
show дорін at right, disappear_fade 
show селена at left, size_selena, disappear_fade 
"Доріан хотів почути серйозну оцінку."
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
sh "Доріан воліє сходитися з жінками більш знатного походження й більш гарними."
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
"Капітан відчинив двері в коридор. Караульні тут же витяглися по стійці «струнко»."
"У коридорах замку було по-ранковому холодно. Шаол провів Селену повз казарми. Караульні, одягнені в шкіряні й металеві обладунки, салютували їм обом. Крізь відчинені двері Селена побачила простору кімнату, де гвардійці снідали."
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
"У легенях Селени палав вогонь. Ноги налилися свинцем, але вона вперто продовжувала бігти, тримаючись у середині натовпу претендентів. Брулло, Шаол, наставники й три дюжини гвардійців рухалися верхи, супроводжуючи бігунів."
"Декого, включно з Могилою, Нідом і Окоїдом, змусили бігти на довгому ланцюгу. Але зараз Селену найбільше дивувало, що верзила Кейн біжить попереду, відірвавшись від усіх ярдів на десять."
"Досягнувши повороту, Кейн рушив у зворотний бік — до замку. Решта, ніби пташина зграя, поспішила за ним. Головне — дихати рівно; на рівному диханні можна бігти дуже довго. Нехай усі стежать за Кейном. Їй нема потреби перемагати в цьому змаганні."
"Дерева розступилися. За ними відкрилася широка галявина. Там був кінець шляху. У Селени крутилася голова, але вона не сміла розсіювати увагу."
"Вона не одразу відчула, що забіг закінчився. Ті, хто біг разом із нею, переходили на крок, ловлячи ротом повітря. Їй хотілося повалитися на килим пожовклого листя, але вона знала, що цього робити не можна. Треба іти й заспокоювати дихання, навіть якщо перед очима продовжують танцювати зірки."
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
"Наступного ранку Шаолу вже не довелося будити Селену. Увійшовши до її спальні, капітан застав колишню в’язницю Ендов’єра за дивним заняттям. Селена підтягувалася, вхопившись за дверний карниз і прагнучи дістати його підборіддям. Ці вправи тривали вже цілу годину. У Селени тремтіли руки, і кожен новий підхід давався їй дедалі важче."
"Поява Шаола не змусила Селену зупинитися. Вона підтягнулася ще кілька разів, усміхаючись йому крізь стиснуті зуби. На її здивування, у відповідь капітан теж усміхнувся."
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
n "Ми говорили про погоду. (ламана адарланська)"
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
"Селена, знову перейшла на ейлуейську. Нехемія повернулася до вікна."
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

return
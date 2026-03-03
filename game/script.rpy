testsuite global:
    setup:
        skip until "main_menu"
    before testsuite:
        if not screen "main_menu":
            run MainMenu(confirm=False)
    teardown:
        exit

    testcase smoke_test:
        assert screen "main_menu"
        click "Почати"
        assert screen "say"

    testcase e2e_test:
        click "Почати"
        skip until "main_menu"
        assert screen "main_menu"

    testcase nain_menu_ui_test:
        click "Завантажити"
        assert screen "load"
        click "Повернутися"
        assert screen "main_menu"
        
        click "Налаштування"
        assert screen "preferences"
        click "Повернутися"
        assert screen "main_menu"

        click "Про гру"
        assert screen "about"
        click "Повернутися"
        assert screen "main_menu"

        click "Довідка"
        assert screen "help"
        click "Повернутися"
        assert screen "main_menu"
        
    testcase game_ui_test:
        click "Почати"
        assert screen "say"

        click "Історія"
        assert screen "history"
        click "Повернутися"
        assert screen "say"

        click "Налаштування"
        assert screen "preferences"
        click "Повернутися"
        assert screen "say"

        click "Зберегти"
        assert screen "save"
        click "Повернутися"
        assert screen "say"

init python:

    renpy.register_shader("name.gradient", variables="""
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
    """)




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

define c  = Character("Селена")
define pr  = Character("Принц Дорін")
define g  = Character("Герцог Перрантон")
define ka = Character("Кальтена")
define sh  = Character("Капітан Єстфол")
define n  = Character("Нехемія")
define gv1  = Character("Гвардієць 1")
define gv2  = Character("Гвардієць 2")
define f  = Character("Фаліпа")
define ke  = Character("Кейн")
define b  = Character("Брулло")
define ks  = Character("Ксав'єр")
define K  = Character("Король")
define spk1  = Character("Спутниця 1")
define spk2  = Character("Спутниця 2")



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
                    text who style "name_grad_common" at grad_selena

                elif who == "Принц Дорін":
                    text who style "name_grad_common" at grad_dorin

                elif who == "Герцог Перрантон":
                    text who style "name_grad_common" at grad_duke

                elif who == "Кальтена":
                    text who style "name_grad_common" at grad_kalt

                elif who == "Капітан Єстфол":
                    text who style "name_grad_common" at grad_captain

                elif who == "Нехемія":
                    text who style "name_grad_common" at grad_nehemia


                elif who == "Гвардієць 1" or who == "Гвардієць 2":
                    text who style "name_grad_common" at grad_guard

                elif who == "Фаліпа":
                    text who style "name_grad_common" at grad_falipa

                elif who == "Король":
                    text who style "name_grad_common" at grad_king

                elif who == "Спутниця 1" or who == "Спутниця 2":
                    text who style "name_grad_common" at grad_companion

                elif who == "Кейн":
                    text who style "name_grad_common" at grad_kain

                elif who == "Брулло":
                    text who style "name_grad_common" at grad_brullo

                elif who == "Ксав'єр":
                    text who style "name_grad_common" at grad_xavier

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

    sh "Тримайся рівно. Принц не любить слабкості."
    show селена at right
    c "Я не слабка."
    sh "Побачимо."

    "Вони зупинилися перед високими дверима, прикрашеними золотими візерунками. Двері відчинилися, і світло тронної зали залило простір."

    "На підвищенні сидів принц Доріан. Його погляд був уважний, але сповнений цікавості — він розглядав ту, про кого чув легенди."
    "Поруч стояв герцог Перрантон, його усмішка була холодною, а очі — пильними, наче він оцінював здобич."

    pr "Отже, це й є Селена Сардотін."

    "Принц кинув короткий погляд на капітана Єстфола."

    pr "Я ж наказував привести її в належному вигляді. Чому вона досі в лахмітті?"

    sh "Вона відмовилася. До того ж я хотів привести її до вас якомога швидше."

    c "Я не річ, яку можна прикрасити для вашого задоволення."

    "Герцог Перрантон тихо засміявся, але його сміх був більше схожий на шипіння."

    pr "Герцогу Перрантону, ви вже зустрічалися з казначеєм Ендов’єра?"

    g "…"

    "На мить його усмішка зникла, і він нахмурився, але все ж кивнув."

    g "Так, Ваша Високість. Я виконаю те, що ви просите."

    "Перрантон зробив легкий уклін і, не приховуючи роздратування, покинув залу."

    "Коли двері зачинилися, Доріан відкинувся вперед, сперся ліктями на коліна й уважно подивився на Селену."

    pr "Ти виглядаєш молодшою, ніж я очікував."
    pr "Про тебе розповідають неймовірні історії."
    pr "Скажи, як тобі Ендов’єр після такої запаморочливої долі, яку ти мала в Рафтхолі?"

    "«Напищений індик», — подумала Селена."

    c "Неможливо уявити більше щастя."

    pr "Після року в копальнях ти не втратила живості. Це дивує. Зазвичай там витримують місяць."

    c "Сама дивуюся цій загадці."

    "Вона опустила погляд і поправила кайдани, наче це були мереживні рукавички."

    pr "У неї гострий язик, — усміхнувся принц до капітана. — І говорить правильно, не як простий сброд."

    c "Сподіваюся, — буркнула Селена."

    sh "При зверненні до принца додавай «ваше високість»."

    "Селена відповіла йому усмішкою й знову повернулася до Доріана. Той засміявся."

    pr "Ти знаєш, що тут рабиня. Приговор нічого тебе не навчив?"

    c "Копальня вчить лише тримати кирку."

    pr "І ти жодного разу не намагалась утекти?"

    c "Один раз."

    pr "Мені про це не казали."

    sh "Через чотири місяці вона спробувала втекти."

    c "Це не найкраща частина історії."

    pr "А яка ж найкраща?"

    sh "Ваше високість, втеча з Ендов’єра — самогубство. Але вона вижила."

    c "Так, — тихо сказала Селена."

    pr "Що ж тобі завадило?"

    c "Гілка хруснула під ногою."

    sh "Перед тим вона вбила наглядача й двадцять три стражники. Її перехопили біля стіни."

    c "Від моєї шахти до стіни — триста шістдесят три фути. Я рахувала."

    sh "Зазвичай втікач не проходить і трьох футів."

    pr "Тебе могли вбити. Чому ж залишили живою?"

    c "Король наказав, щоб я пройшла всі жахи Ендов’єра."
    c "Я й не збиралась тікати, — прошепотіла вона."

    pr "У тебе багато шрамів?"

    "Селена знизала плечима. Принц підійшов ближче."

    pr "Тут лише бруд. І запах жахливий!"

    c "А як інакше пахнути, якщо я забула, коли востаннє милася? Вибачте… ваше високість."

    "Принц обійшов її, розглядаючи. Стражники напружилися."

    pr "Я бачу кілька шрамів, але думав, що буде гірше. Це сховають сукні."

    c "Сукні? — перепитала вона."

    pr "У тебе чудові очі. І які ж вони злі!"

    "Селена ледь стримувалася, щоб не кинутися на нього. Капітан різко відтягнув її назад."

    return
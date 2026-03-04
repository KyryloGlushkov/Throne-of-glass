testsuite sasha:
    setup:
        skip until "main_menu"
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        skip until "main_menu"
        $ _preferences.reset()
    teardown:
        exit

    testcase smoke_test:
        assert screen "main_menu"
        click "Почати"
        assert screen "say"

    testcase pref_display_test:
        click "Налаштування"
        assert screen "preferences"

        click "У вікні"
        assert eval(preferences.fullscreen == False)
        click "На весь екран"
        assert eval(preferences.fullscreen == True)

        click "Повернутися"

    testcase fail_ui_test:
        xfail True

        click "Почати"
        assert screen "say"

        click "Завантажити"
        assert screen "load"

# -------------------------------------------------------------

testsuite kiril:
    setup:
        skip until "main_menu"
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        skip until "main_menu"
        $ _preferences.reset()
    teardown:
        exit

    testcase e2e_test:
        click "Почати"
        advance until screen "main_menu"
        assert screen "main_menu"

    testcase main_menu_ui_test:
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

    testcase fail_mute_test:
        xfail True

        click "Налаштування"
        click "Mute All"

        assert eval(preferences.get_mute("music") == True)

        click "Повернутися"

# -------------------------------------------------------------

testsuite nastya:
    setup:
        skip until "main_menu"
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        skip until "main_menu"
        $ _preferences.reset()
    teardown:
        exit

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

    testcase pref_skip_test:
        click "Налаштування"
        assert screen "preferences"

        click "After Choices"
        assert eval(preferences.skip_after_choices == True)

        click "Skip"
        assert eval(preferences.skip_unseen == True)

        click "Transitions"
        assert eval(preferences.transitions == 0)

        click "Повернутися"

    testcase fail_ui_test:
        xfail True
        click "Завантажити"
        assert screen "load"

        click "Налаштування"
        assert screen "preferences"

        click "Повернутися"
        assert screen "main_menu"

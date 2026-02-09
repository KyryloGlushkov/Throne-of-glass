## ──────────────────────────────
## Скляна кнопка з альфа-маскою
## ──────────────────────────────

screen glass_textbutton(txt, act):

    button:
        action act
        background None  # без фону

        fixed:
            xysize (340, 60)

            # текст
            text txt:
                xalign 0.5
                yalign 0.5
                style "menu_text"

            # скляна альфа-маска
            add "gui/frozen glass.png":
                xalign 0.5
                yalign 0.5
                alpha 0.7
                at glass_hover


## ──────────────────────────────
## Hover-ефект для скляної маски
## ──────────────────────────────

transform glass_hover:
    on idle:
        alpha 0.5
    on hover:
        alpha 1.0

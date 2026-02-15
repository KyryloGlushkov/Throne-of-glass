## =========================================================
## Скляні кнопки
## =========================================================


## ──────────────────────────────
## Стиль тексту
## ──────────────────────────────

style glass_text is default:
    font "gui/Monotype-Corsiva-Regular.ttf"      # ← твій шрифт
    size 46
    color "#e8f6ff"
    outlines [(1, "#88bbff55", 0, 0)]
    hover_color "#ffffff"
    selected_color "#cceeff"
    text_align 0.5


## ──────────────────────────────
## Hover ефект скла
## ──────────────────────────────

transform glass_hover:
    on idle:
        linear 0.15 alpha 0.55
    on hover:
        linear 0.15 alpha 1.0


## ──────────────────────────────
## Скляна кнопка
## ──────────────────────────────

screen glass_textbutton(txt, act):

    button:
        action act
        background None
        xysize (340, 60)

        fixed:

            add "gui/frozen glass.png":
                xalign 0.5
                yalign 0.5
                at glass_hover

            text txt:
                xalign 0.5
                yalign 0.5
                style "glass_text"

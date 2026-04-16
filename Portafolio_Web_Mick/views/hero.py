import reflex as rx

def hero() -> rx.Component:
    return rx.center(
        rx.vstack(

            rx.image(
                src="/HeadImageMisaelLogo.png",
                width="100%",
                max_width="1200px",
                alt="Mick Misael Logo",
                style={"filter": "drop-shadow(0px 0px 30px rgba(0, 112, 243, 0.4))"}
            ),

            rx.text(
                "COMPUTER SYSTEMS ENGINEER | SYSADMIN | CEO of StackTON",
                size="7",
                color="rgba(255, 255, 255, 0.9)",
                font_family="monospace",
                text_align="center",
                letter_spacing="2px",
            ),
            spacing="6",
            align="center",
        ),
        width="100%",
        height="100vh",
        margin_top="-5em",
        padding_bottom="5vh",
    )
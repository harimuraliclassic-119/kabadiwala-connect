"""
Kabadiwala Connect - Modern UI
Bringing the informal Collector to the Formal Recycling Chain
Pure Python UI with Flet (runs as Web + Mobile + Desktop)
Theme: Soft Green • Blue • White with subtle gradients & animations
"""

import flet as ft
from flet import (
    Page, Container, Column, Row, Text, Icon, IconButton,
    ElevatedButton, OutlinedButton, TextButton, Card,
    NavigationBar, NavigationBarDestination, Stack,
    LinearGradient, RadialGradient, BorderRadius, Border,
    BoxShadow, Offset, Animation, AnimationCurve, Margin, Padding,
    MainAxisAlignment, CrossAxisAlignment,
    ScrollMode, GestureDetector, Transform, Scale, Rotate,
    FontWeight, TextAlign, ClipBehavior, ProgressBar,
    CircleAvatar, Divider, Switch, ListTile
)


# ─── Color Palette (Green - Blue - White) ───────────────────────────────────
PRIMARY_GREEN = "#1B8A5A"
LIGHT_GREEN = "#2ECC71"
SOFT_GREEN = "#E8F8F0"
DEEP_BLUE = "#1A5F7A"
ACCENT_BLUE = "#3498DB"
SOFT_BLUE = "#EBF5FB"
WHITE = "#FFFFFF"
OFF_WHITE = "#F7FBFE"
DARK_TEXT = "#1A2B3C"
MUTED_TEXT = "#5A6A7A"
CARD_SHADOW = "#00000015"


def create_gradient_bg():
    """Soft multi-color background that feels airy, not heavy."""
    return LinearGradient(
        begin=ft.Alignment.TOP_LEFT,
        end=ft.Alignment.BOTTOM_RIGHT,
        colors=[
            "#F0F9F4",
            "#F5FAFF",
            "#FFFFFF",
            "#EAF6F0",
        ],
        stops=[0.0, 0.35, 0.7, 1.0],
    )


def animated_card(content, delay=0, on_click=None):
    return Container(
        content=content,
        bgcolor=WHITE,
        border_radius=18,
        padding=18,
        shadow=BoxShadow(
            spread_radius=0,
            blur_radius=18,
            color=CARD_SHADOW,
            offset=Offset(0, 6),
        ),
        animate=Animation(400, AnimationCurve.EASE_OUT),
        animate_scale=Animation(300, AnimationCurve.EASE_OUT),
        on_click=on_click,
        ink=True,
    )


def section_title(title: str, subtitle: str = None, icon=None):
    return Column(
        spacing=4,
        controls=[
            Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(icon, color=PRIMARY_GREEN, size=22) if icon else Container(),
                    Text(title, size=20, weight=FontWeight.W_700, color=DARK_TEXT),
                ],
            ),
            Text(subtitle, size=13, color=MUTED_TEXT) if subtitle else Container(),
        ],
    )


def collector_card(name, distance, rating, specialty, avatar_color, page):
    return animated_card(
        content=Column(
            spacing=12,
            controls=[
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Row(
                            spacing=12,
                            controls=[
                                CircleAvatar(
                                    content=Text(name[0], color=WHITE, weight=FontWeight.BOLD),
                                    bgcolor=avatar_color,
                                    radius=24,
                                ),
                                Column(
                                    spacing=2,
                                    controls=[
                                        Text(name, size=15, weight=FontWeight.W_600, color=DARK_TEXT),
                                        Text(specialty, size=12, color=MUTED_TEXT),
                                    ],
                                ),
                            ],
                        ),
                        Container(
                            content=Text(f"{distance}", size=12, weight=FontWeight.W_600, color=PRIMARY_GREEN),
                            bgcolor=SOFT_GREEN,
                            padding=Padding(10, 6, 10, 6),
                            border_radius=20,
                        ),
                    ],
                ),
                Row(
                    spacing=4,
                    controls=[
                        Icon(ft.Icons.STAR_ROUNDED, color="#F1C40F", size=16),
                        Text(f"{rating}", size=13, weight=FontWeight.W_600, color=DARK_TEXT),
                        Text(" • Available now", size=12, color=LIGHT_GREEN),
                    ],
                ),
                Row(
                    spacing=8,
                    controls=[
                        ElevatedButton(
                            content=Row(
                                spacing=6,
                                tight=True,
                                controls=[
                                    Icon(ft.Icons.HANDSHAKE_ROUNDED, size=16, color=WHITE),
                                    Text("Connect", size=13, color=WHITE, weight=FontWeight.W_600),
                                ],
                            ),
                            style=ft.ButtonStyle(
                                bgcolor=PRIMARY_GREEN,
                                shape=ft.RoundedRectangleBorder(radius=12),
                                padding=Padding(16, 10, 16, 10),
                            ),
                            on_click=lambda e: show_snack(page, f"Connecting you with {name}..."),
                        ),
                        OutlinedButton(
                            content=Row(
                                spacing=6,
                                tight=True,
                                controls=[
                                    Icon(ft.Icons.CHAT_BUBBLE_OUTLINE_ROUNDED, size=16, color=DEEP_BLUE),
                                    Text("Chat", size=13, color=DEEP_BLUE),
                                ],
                            ),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=12),
                                side=ft.BorderSide(1.5, DEEP_BLUE),
                                padding=Padding(14, 10, 14, 10),
                            ),
                            on_click=lambda e: show_snack(page, f"Opening chat with {name}"),
                        ),
                    ],
                ),
            ],
        )
    )


def show_snack(page: Page, message: str):
    page.snack_bar = ft.SnackBar(
        content=Text(message, color=WHITE),
        bgcolor=PRIMARY_GREEN,
        behavior=ft.SnackBarBehavior.FLOATING,
        shape=ft.RoundedRectangleBorder(radius=12),
        elevation=8,
        margin=Margin(20, 20, 20, 20),
    )
    page.snack_bar.open = True
    page.update()


def build_home_view(page: Page):
    hero = Container(
        content=Column(
            spacing=14,
            controls=[
                Text("Kabadiwala Connect", size=26, weight=FontWeight.W_800, color=WHITE),
                Text("Linking informal collectors to the formal recycling chain", size=14, color="#E0F2F1"),
                Container(height=8),
                ElevatedButton(
                    content=Row(
                        spacing=8,
                        tight=True,
                        controls=[
                            Icon(ft.Icons.LOCATION_ON_ROUNDED, color=PRIMARY_GREEN, size=18),
                            Text("Report Trash Location", size=14, weight=FontWeight.W_600, color=PRIMARY_GREEN),
                        ],
                    ),
                    style=ft.ButtonStyle(
                        bgcolor=WHITE,
                        shape=ft.RoundedRectangleBorder(radius=14),
                        padding=Padding(20, 14, 20, 14),
                        elevation=4,
                    ),
                    on_click=lambda e: page.go("/report"),
                ),
            ],
        ),
        gradient=LinearGradient(
            begin=ft.Alignment.TOP_LEFT,
            end=ft.Alignment.BOTTOM_RIGHT,
            colors=[PRIMARY_GREEN, DEEP_BLUE],
        ),
        border_radius=22,
        padding=24,
        shadow=BoxShadow(blur_radius=24, color="#1B8A5A40", offset=Offset(0, 8)),
        animate=Animation(500, AnimationCurve.EASE_OUT),
    )

    def stat_card(value, label, icon, color):
        return Container(
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=6,
                controls=[
                    Icon(icon, color=color, size=26),
                    Text(value, size=22, weight=FontWeight.W_800, color=DARK_TEXT),
                    Text(label, size=12, color=MUTED_TEXT, text_align=TextAlign.CENTER),
                ],
            ),
            bgcolor=WHITE,
            border_radius=16,
            padding=16,
            expand=True,
            shadow=BoxShadow(blur_radius=12, color=CARD_SHADOW, offset=Offset(0, 4)),
        )

    stats_row = Row(
        spacing=12,
        controls=[
            stat_card("12", "Nearby\nCollectors", ft.Icons.PEOPLE_ALT_ROUNDED, PRIMARY_GREEN),
            stat_card("3.2 km", "Closest\nKabadiwala", ft.Icons.NEAR_ME_ROUNDED, ACCENT_BLUE),
            stat_card("48 kg", "Recycled\nThis Month", ft.Icons.ECO_ROUNDED, LIGHT_GREEN),
        ],
    )

    collectors = [
        ("Ramesh Kumar", "1.2 km", "4.8", "Plastic & Metal", PRIMARY_GREEN),
        ("Sita Devi", "2.4 km", "4.9", "Paper & Cardboard", DEEP_BLUE),
        ("Imran Ali", "3.1 km", "4.7", "E-waste Specialist", ACCENT_BLUE),
        ("Lakshmi Bai", "4.0 km", "4.6", "Glass & Mixed", "#16A085"),
    ]

    collector_list = Column(
        spacing=14,
        controls=[collector_card(*c, page) for c in collectors],
    )

    impact = animated_card(
        content=Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Column(
                    spacing=4,
                    controls=[
                        Text("Your Eco Impact", size=15, weight=FontWeight.W_600, color=DARK_TEXT),
                        Text("You've helped divert 48 kg from landfills", size=12, color=MUTED_TEXT),
                    ],
                ),
                Container(
                    content=Icon(ft.Icons.FOREST_ROUNDED, color=PRIMARY_GREEN, size=32),
                    bgcolor=SOFT_GREEN,
                    padding=12,
                    border_radius=14,
                ),
            ],
        )
    )

    return Container(
        content=Column(
            spacing=22,
            scroll=ScrollMode.AUTO,
            controls=[
                hero,
                section_title("Live Overview", "Real-time snapshot around you", ft.Icons.DASHBOARD_ROUNDED),
                stats_row,
                impact,
                section_title("Nearest Collectors", "Connect instantly with verified kabadiwalas", ft.Icons.LOCATION_SEARCHING_ROUNDED),
                collector_list,
                Container(height=20),
            ],
        ),
        padding=Padding(18, 10, 18, 20),
        expand=True,
    )


def build_report_view(page: Page):
    location_field = ft.TextField(
        label="Trash Location / Landmark",
        hint_text="e.g. Near Park Gate, Sector 15",
        border_radius=14,
        filled=True,
        bgcolor=SOFT_BLUE,
        border_color=ACCENT_BLUE,
        focused_border_color=PRIMARY_GREEN,
        prefix_icon=ft.Icons.PLACE_ROUNDED,
        text_size=14,
    )

    waste_type = ft.Dropdown(
        label="Primary Waste Type",
        border_radius=14,
        filled=True,
        bgcolor=SOFT_BLUE,
        options=[
            ft.dropdown.Option("Plastic"),
            ft.dropdown.Option("Paper & Cardboard"),
            ft.dropdown.Option("Metal"),
            ft.dropdown.Option("Glass"),
            ft.dropdown.Option("E-waste"),
            ft.dropdown.Option("Mixed / Other"),
        ],
        value="Plastic",
    )

    quantity = ft.TextField(
        label="Estimated Quantity",
        hint_text="e.g. 2 bags / 5 kg",
        border_radius=14,
        filled=True,
        bgcolor=SOFT_BLUE,
        prefix_icon=ft.Icons.SCALE_ROUNDED,
    )

    notes = ft.TextField(
        label="Additional Notes (optional)",
        multiline=True,
        min_lines=2,
        max_lines=3,
        border_radius=14,
        filled=True,
        bgcolor=SOFT_BLUE,
    )

    def submit_report(e):
        show_snack(page, "Report submitted! Nearest collectors notified.")
        page.go("/")

    form = Column(
        spacing=16,
        controls=[
            section_title("Report Trash", "Pin the location so collectors can find it easily", ft.Icons.ADD_LOCATION_ALT_ROUNDED),
            Container(
                content=Column(
                    spacing=4,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Icon(ft.Icons.MAP_ROUNDED, size=48, color=PRIMARY_GREEN),
                        Text("Tap to open map & drop pin", size=13, color=MUTED_TEXT),
                        Text("(Mock map – location services ready)", size=11, color="#A0AEC0"),
                    ],
                ),
                bgcolor=SOFT_GREEN,
                border_radius=18,
                padding=28,
                alignment=ft.Alignment.CENTER,
                on_click=lambda e: show_snack(page, "Map picker would open here"),
                ink=True,
            ),
            location_field,
            waste_type,
            quantity,
            notes,
            Container(height=8),
            ElevatedButton(
                content=Row(
                    spacing=10,
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Icon(ft.Icons.SEND_ROUNDED, color=WHITE),
                        Text("Notify Collectors", size=15, weight=FontWeight.W_600, color=WHITE),
                    ],
                ),
                style=ft.ButtonStyle(
                    bgcolor=PRIMARY_GREEN,
                    shape=ft.RoundedRectangleBorder(radius=14),
                    padding=20,
                    elevation=6,
                ),
                width=page.width - 40 if page.width else 340,
                on_click=submit_report,
            ),
            Text(
                "Your report helps formalize the informal recycling network.",
                size=12,
                color=MUTED_TEXT,
                text_align=TextAlign.CENTER,
            ),
        ],
    )

    return Container(
        content=form,
        padding=Padding(18, 10, 18, 30),
        expand=True,
        scroll=ScrollMode.AUTO,
    )


def build_map_view(page: Page):
    return Container(
        content=Column(
            spacing=18,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                section_title("Live Map", "Trash spots & collectors near you", ft.Icons.MAP_ROUNDED),
                Container(
                    content=Stack(
                        controls=[
                            Container(
                                gradient=LinearGradient(
                                    begin=ft.Alignment.TOP_CENTER,
                                    end=ft.Alignment.BOTTOM_CENTER,
                                    colors=["#D5F5E3", "#D6EAF8", "#E8F6F3"],
                                ),
                                border_radius=20,
                                expand=True,
                            ),
                            Container(content=Icon(ft.Icons.LOCATION_ON, color="#E74C3C", size=36), left=80, top=90),
                            Container(content=Icon(ft.Icons.LOCATION_ON, color="#E74C3C", size=32), left=200, top=140),
                            Container(content=Icon(ft.Icons.PERSON_PIN_CIRCLE, color=PRIMARY_GREEN, size=40), left=140, top=60),
                            Container(content=Icon(ft.Icons.PERSON_PIN_CIRCLE, color=DEEP_BLUE, size=36), right=60, top=110),
                            Container(
                                content=Column(
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Text("Interactive Map View", size=16, weight=FontWeight.W_600, color=DARK_TEXT),
                                        Text("Real GPS + collector tracking would appear here", size=12, color=MUTED_TEXT),
                                    ],
                                ),
                                alignment=ft.Alignment.CENTER,
                            ),
                        ]
                    ),
                    height=320,
                    border_radius=20,
                    shadow=BoxShadow(blur_radius=16, color=CARD_SHADOW, offset=Offset(0, 6)),
                    clip_behavior=ClipBehavior.HARD_EDGE,
                ),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    spacing=24,
                    controls=[
                        Row(spacing=6, controls=[
                            Icon(ft.Icons.LOCATION_ON, color="#E74C3C", size=18),
                            Text("Trash Report", size=13, color=MUTED_TEXT),
                        ]),
                        Row(spacing=6, controls=[
                            Icon(ft.Icons.PERSON_PIN_CIRCLE, color=PRIMARY_GREEN, size=18),
                            Text("Collector", size=13, color=MUTED_TEXT),
                        ]),
                    ],
                ),
                animated_card(
                    content=Column(
                        spacing=10,
                        controls=[
                            Text("Quick Actions", size=15, weight=FontWeight.W_600),
                            Row(
                                spacing=10,
                                controls=[
                                    ElevatedButton(
                                        "Center on Me",
                                        icon=ft.Icons.MY_LOCATION,
                                        style=ft.ButtonStyle(
                                            bgcolor=SOFT_GREEN,
                                            color=PRIMARY_GREEN,
                                            shape=ft.RoundedRectangleBorder(radius=12),
                                        ),
                                        on_click=lambda e: show_snack(page, "Centering on your location..."),
                                    ),
                                    OutlinedButton(
                                        "Filter Collectors",
                                        icon=ft.Icons.FILTER_LIST,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=12),
                                            side=ft.BorderSide(1.5, DEEP_BLUE),
                                            color=DEEP_BLUE,
                                        ),
                                        on_click=lambda e: show_snack(page, "Filter options opened"),
                                    ),
                                ],
                            ),
                        ],
                    )
                ),
            ],
        ),
        padding=Padding(18, 10, 18, 20),
        expand=True,
        scroll=ScrollMode.AUTO,
    )


def build_messages_view(page: Page):
    chats = [
        ("Ramesh Kumar", "I can pick up the plastic by 4 PM today.", "10:24 AM", PRIMARY_GREEN, True),
        ("Sita Devi", "Thank you! Cardboard collected successfully.", "Yesterday", DEEP_BLUE, False),
        ("Imran Ali", "Is the e-waste still available?", "Mon", ACCENT_BLUE, True),
    ]

    chat_tiles = []
    for name, last_msg, time, color, unread in chats:
        chat_tiles.append(
            animated_card(
                content=ListTile(
                    leading=CircleAvatar(
                        content=Text(name[0], color=WHITE, weight=FontWeight.BOLD),
                        bgcolor=color,
                    ),
                    title=Text(name, weight=FontWeight.W_600, size=15),
                    subtitle=Text(last_msg, size=13, color=MUTED_TEXT, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                    trailing=Column(
                        horizontal_alignment=CrossAxisAlignment.END,
                        spacing=4,
                        controls=[
                            Text(time, size=11, color=MUTED_TEXT),
                            Container(
                                width=10,
                                height=10,
                                bgcolor=PRIMARY_GREEN if unread else None,
                                border_radius=5,
                            ) if unread else Container(),
                        ],
                    ),
                    on_click=lambda e, n=name: show_snack(page, f"Opening chat with {n}"),
                ),
            )
        )

    return Container(
        content=Column(
            spacing=14,
            controls=[
                section_title("Connections", "Your active chats with collectors", ft.Icons.CHAT_ROUNDED),
                *chat_tiles,
                Container(height=20),
            ],
        ),
        padding=Padding(18, 10, 18, 20),
        expand=True,
        scroll=ScrollMode.AUTO,
    )


def build_profile_view(page: Page):
    return Container(
        content=Column(
            spacing=18,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Container(height=10),
                CircleAvatar(
                    content=Icon(ft.Icons.PERSON, size=48, color=WHITE),
                    bgcolor=PRIMARY_GREEN,
                    radius=48,
                ),
                Text("Aarav Sharma", size=22, weight=FontWeight.W_700, color=DARK_TEXT),
                Text("Citizen Contributor • Delhi", size=13, color=MUTED_TEXT),
                Container(height=8),
                Row(
                    spacing=12,
                    controls=[
                        Container(
                            content=Column(
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                spacing=4,
                                controls=[
                                    Text("12", size=24, weight=FontWeight.W_800, color=PRIMARY_GREEN),
                                    Text("Reports", size=12, color=MUTED_TEXT),
                                ],
                            ),
                            bgcolor=SOFT_GREEN,
                            padding=16,
                            border_radius=16,
                            expand=True,
                        ),
                        Container(
                            content=Column(
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                spacing=4,
                                controls=[
                                    Text("48 kg", size=24, weight=FontWeight.W_800, color=DEEP_BLUE),
                                    Text("Diverted", size=12, color=MUTED_TEXT),
                                ],
                            ),
                            bgcolor=SOFT_BLUE,
                            padding=16,
                            border_radius=16,
                            expand=True,
                        ),
                    ],
                ),
                animated_card(
                    content=Column(
                        spacing=4,
                        controls=[
                            ListTile(
                                leading=Icon(ft.Icons.HISTORY, color=PRIMARY_GREEN),
                                title=Text("Pickup History"),
                                trailing=Icon(ft.Icons.CHEVRON_RIGHT),
                                on_click=lambda e: show_snack(page, "History coming soon"),
                            ),
                            Divider(height=1, color="#E8EEF2"),
                            ListTile(
                                leading=Icon(ft.Icons.EMOJI_EVENTS_ROUNDED, color="#F39C12"),
                                title=Text("Eco Rewards"),
                                trailing=Icon(ft.Icons.CHEVRON_RIGHT),
                                on_click=lambda e: show_snack(page, "Rewards unlocked!"),
                            ),
                            Divider(height=1, color="#E8EEF2"),
                            ListTile(
                                leading=Icon(ft.Icons.SETTINGS_ROUNDED, color=DEEP_BLUE),
                                title=Text("Preferences"),
                                trailing=Icon(ft.Icons.CHEVRON_RIGHT),
                            ),
                            Divider(height=1, color="#E8EEF2"),
                            ListTile(
                                leading=Icon(ft.Icons.HELP_OUTLINE_ROUNDED, color=MUTED_TEXT),
                                title=Text("Help & Support"),
                                trailing=Icon(ft.Icons.CHEVRON_RIGHT),
                            ),
                        ],
                    )
                ),
                Text("Kabadiwala Connect v1.0 • Formalizing the informal", size=11, color="#A0AEC0"),
            ],
        ),
        padding=Padding(18, 10, 18, 30),
        expand=True,
        scroll=ScrollMode.AUTO,
    )


def main(page: Page):
    page.title = "Kabadiwala Connect"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.bgcolor = OFF_WHITE
    page.theme = ft.Theme(
        color_scheme_seed=PRIMARY_GREEN,
        visual_density=ft.VisualDensity.COMFORTABLE,
    )
    page.window.width = 420
    page.window.height = 860

    content_area = Container(
        content=build_home_view(page),
        expand=True,
        animate=Animation(350, AnimationCurve.EASE_IN_OUT),
    )

    def change_view(e):
        idx = e.control.selected_index
        views = [
            build_home_view(page),
            build_report_view(page),
            build_map_view(page),
            build_messages_view(page),
            build_profile_view(page),
        ]
        content_area.content = views[idx]
        content_area.update()

    nav_bar = NavigationBar(
        bgcolor=WHITE,
        elevation=12,
        indicator_color=SOFT_GREEN,
        selected_index=0,
        on_change=change_view,
        destinations=[
            NavigationBarDestination(icon=ft.Icons.HOME_OUTLINED, selected_icon=ft.Icons.HOME_ROUNDED, label="Home"),
            NavigationBarDestination(icon=ft.Icons.ADD_LOCATION_ALT_OUTLINED, selected_icon=ft.Icons.ADD_LOCATION_ALT_ROUNDED, label="Report"),
            NavigationBarDestination(icon=ft.Icons.MAP_OUTLINED, selected_icon=ft.Icons.MAP_ROUNDED, label="Map"),
            NavigationBarDestination(icon=ft.Icons.CHAT_BUBBLE_OUTLINE, selected_icon=ft.Icons.CHAT_BUBBLE_ROUNDED, label="Connect"),
            NavigationBarDestination(icon=ft.Icons.PERSON_OUTLINE, selected_icon=ft.Icons.PERSON_ROUNDED, label="Profile"),
        ],
    )

    def build_appbar():
        return Container(
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Row(
                        spacing=10,
                        controls=[
                            Container(
                                content=Icon(ft.Icons.RECYCLING_ROUNDED, color=WHITE, size=22),
                                bgcolor=PRIMARY_GREEN,
                                padding=8,
                                border_radius=12,
                            ),
                            Column(
                                spacing=0,
                                controls=[
                                    Text("Kabadiwala", size=16, weight=FontWeight.W_700, color=DARK_TEXT),
                                    Text("Connect", size=11, color=MUTED_TEXT),
                                ],
                            ),
                        ],
                    ),
                    IconButton(
                        icon=ft.Icons.NOTIFICATIONS_NONE_ROUNDED,
                        icon_color=DARK_TEXT,
                        on_click=lambda e: show_snack(page, "No new notifications"),
                    ),
                ],
            ),
            padding=Padding(16, 12, 12, 12),
            bgcolor=WHITE,
            shadow=BoxShadow(blur_radius=10, color="#00000008", offset=Offset(0, 2)),
        )

    def route_change(e):
        if page.route == "/report":
            content_area.content = build_report_view(page)
            nav_bar.selected_index = 1
        else:
            content_area.content = build_home_view(page)
            nav_bar.selected_index = 0
        page.update()

    page.on_route_change = route_change

    page.add(
        Container(
            content=Column(
                spacing=0,
                controls=[
                    build_appbar(),
                    content_area,
                    nav_bar,
                ],
            ),
            gradient=create_gradient_bg(),
            expand=True,
        )
    )


if __name__ == "__main__":
    print("Starting Kabadiwala Connect...")
    ft.run(main, view=ft.AppView.WEB_BROWSER, port=8550)
import datetime
from flet import *
from weather import get_weather_details, get_forecast_details

current_date = datetime.datetime.now()
formatted_date = current_date.strftime("%A, %B %d")

weather_data = get_weather_details("mumbai")
forecast_data = get_forecast_details("mumbai")


def main(page: Page):
    page.title = "Weather Forecasts"
    page.padding = 0
    page.vertical_alignment = alignment.center
    page.horizontal_alignment = alignment.center
    page.window_width = 500
    page.window_height = 800
    page.colors = ["lightblue300", "lightblue900"]
    page.fonts = {
        "Comfortaa-Bold": "fonts/Comfortaa-Bold.ttf",
        "Comfortaa-Light": "fonts/Comfortaa-Light.ttf",
        "Comfortaa-Medium": "fonts/Comfortaa-Medium.ttf",
        "Comfortaa-Regular": "fonts/Comfortaa-Regular.ttf",
        "Comfortaa-SemiBold": "fonts/Comfortaa-SemiBold.ttf",
    }

    def hourly_items_report():
        items = []
        for k, v in forecast_data.items():
            time = k
            logo = v["logo"]
            temp = v["temp_c"]

            hourly_icon = Image(height=50)
            hourly_time = Text(
                font_family="Comfortaa-Medium",
                style=TextThemeStyle.TITLE_MEDIUM,
                color=colors.WHITE,
            )
            hourly_temp = Text(
                font_family="Comfortaa-Medium",
                style=TextThemeStyle.TITLE_MEDIUM,
                color=colors.WHITE,
            )
            hourly_container = Column(
                [hourly_icon, hourly_time, hourly_temp],
                horizontal_alignment=alignment.center,
            )

            hourly_icon.src = f"weather_icons/{logo}"
            hourly_temp.value = temp
            hourly_time.value = time

            items.append(
                Container(
                    content=hourly_container,
                    alignment=alignment.center,
                    width=150,
                    height=150,
                    border_radius=border_radius.all(5),
                )
            )
        return items

    homepage_data = Column(
        [
            Container(height=5),
            Row(
                [
                    Icon(name=icons.LOCATION_PIN, color=colors.WHITE),
                    Text(
                        value=weather_data["Location"],
                        font_family="Comfortaa-Bold",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                ],
                alignment="center",
            ),
            Row(
                [
                    Icon(name=icons.DATE_RANGE_SHARP, color=colors.WHITE),
                    Text(
                        value=formatted_date,
                        size=15,
                        font_family="Comfortaa-Bold",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                ],
                alignment="center",
            ),
            Container(height=25),
            Image(
                src=f"weather_icons/{weather_data['IconLocation']}",
                width=125,
            ),
            Container(height=10),
            Text(
                value=f"{weather_data['Climate']}",
                font_family="Comfortaa-Light",
                style="titleLarge",
                color=colors.WHITE,
            ),
            Text(
                value=f"{int(round(float(weather_data['Temperature (°C)'])))}°",
                font_family="Comfortaa-Light",
                style="displayLarge",
                color=colors.WHITE,
                size=80,
            ),
            Container(height=25),
            Divider(color=colors.WHITE),
            Row(spacing=10, controls=hourly_items_report(), scroll=ScrollMode.AUTO),
            Row(
                [
                    ElevatedButton(
                        width=115,
                        height=60,
                        content=Row(
                            [
                                Icon(
                                    name=icons.ARROW_BACK_ROUNDED,
                                    color=colors.BLUE_900,
                                ),
                                Text(
                                    value="Back",
                                    size=17.5,
                                    color=colors.BLUE_900,
                                    text_align=TextAlign.CENTER,
                                ),
                            ],
                        ),
                        on_click=lambda _: page.go("/"),
                    ),
                    ElevatedButton(
                        width=115,
                        height=60,
                        content=Row(
                            [
                                Text(
                                    value="Details",
                                    size=17.5,
                                    color=colors.BLUE_900,
                                    text_align=TextAlign.CENTER,
                                ),
                                Icon(
                                    name=icons.ARROW_FORWARD_ROUNDED,
                                    color=colors.BLUE_900,
                                ),
                            ],
                        ),
                        on_click=lambda _: page.go("/home/details"),
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
        ],
        horizontal_alignment='center'
    )

    homepage_body = Container(
        content=homepage_data,
        gradient=LinearGradient(
            begin=alignment.top_center,
            end=alignment.bottom_center,
            colors=["lightblue500", "lightblue900"],
        ),
        width=500,
        height=800,
        border_radius=5,
        padding=20,
    )

    splash_screen_data = Column(
        [
            Image(src="logo/logo.svg", width=200),
            Container(height=30),
            Text(
                value="Weather Forecasts",
                font_family="Comfortaa-Bold",
                style=TextThemeStyle.DISPLAY_LARGE,
                text_align=TextAlign.CENTER,
            ),
            Container(height=30),
            ElevatedButton(
                width=205,
                height=75,
                content=Row(
                    [
                        Text(value="Get Started", size=25),
                        Icon(name=icons.ARROW_FORWARD_IOS_ROUNDED),
                    ]
                ),
                on_click=lambda _: page.go("/home"),
            ),
            Container(height=30),
        ],
        alignment='center',
        horizontal_alignment='center'
    )

    splash_screen = Container(
        content=splash_screen_data,
        gradient=LinearGradient(
            begin=alignment.top_center,
            end=alignment.bottom_center,
            colors=[colors.LIGHT_BLUE_500, colors.LIGHT_BLUE_900],
        ),
        width=500,
        height=800,
        border_radius=5,
        padding=20,
    )

    weather_indepth_data = Column(
        [
            Container(height=5),
            Row(
                [
                    Icon(name=icons.LOCATION_PIN, color=colors.WHITE),
                    Text(
                        value=weather_data["Location"],
                        font_family="Comfortaa-Bold",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                ],
                alignment="center",
            ),
            Row(
                [
                    Icon(name=icons.DATE_RANGE_SHARP, color=colors.WHITE),
                    Text(
                        value=formatted_date,
                        size=15,
                        font_family="Comfortaa-Bold",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                ],
                alignment="center",
            ),
            Container(height=15),
            Divider(color=colors.WHITE),
            Container(height=5),
            Row(
                [
                    Text(
                        value="Humidity",
                        font_family="Comfortaa-Light",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                    Text(
                        value=weather_data["Humidity"],
                        font_family="Comfortaa-Light",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            Container(height=5),
            Row(
                [
                    Text(
                        value="Wind Speed",
                        font_family="Comfortaa-Light",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                    Text(
                        value=weather_data["WindSpeed"],
                        font_family="Comfortaa-Light",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            Container(height=5),
            Row(
                [
                    Text(
                        value="Pressure",
                        font_family="Comfortaa-Light",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                    Text(
                        value=weather_data["Pressure"],
                        font_family="Comfortaa-Light",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            Container(height=5),
            Row(
                [
                    Text(
                        value="Precipitation",
                        font_family="Comfortaa-Light",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                    Text(
                        value=weather_data["Precipitation"],
                        font_family="Comfortaa-Light",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            Container(height=5),
            Row(
                [
                    Text(
                        value="Gust",
                        font_family="Comfortaa-Light",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                    Text(
                        value=weather_data["Gust"],
                        font_family="Comfortaa-Light",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            Container(height=5),
            Row(
                [
                    Text(
                        value="UV Index",
                        font_family="Comfortaa-Light",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                    Text(
                        value=weather_data["UVIndex"],
                        font_family="Comfortaa-Light",
                        style="titleLarge",
                        color=colors.WHITE,
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            Container(height=5),
            Divider(color=colors.WHITE),
            Container(height=15),
            Row(spacing=10, controls=hourly_items_report(), scroll=ScrollMode.AUTO),
            ElevatedButton(
                width=150,
                height=75,
                content=Row(
                    [
                        Icon(name=icons.ARROW_BACK_ROUNDED),
                        Text(value="Back", size=25),
                    ]
                ),
                on_click=lambda _: page.go("/home"),
            ),
        ],
        horizontal_alignment=alignment.center,
        alignment=alignment.center,
    )

    weather_indepth_body = Container(
        content=weather_indepth_data,
        gradient=LinearGradient(
            begin=alignment.top_center,
            end=alignment.bottom_center,
            colors=[colors.LIGHT_BLUE_600, colors.LIGHT_BLUE_900],
        ),
        width=500,
        height=800,
        border_radius=5,
        padding=20,
    )

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [splash_screen],
                scroll=ScrollMode.AUTO,
                vertical_alignment=alignment.center,
                horizontal_alignment=alignment.center,
                padding=0,
            )
        )

        if page.route == "/home" or page.route == "/home/details":
            page.views.append(
                View(
                    "/home",
                    [
                        homepage_body,
                    ],
                    scroll=ScrollMode.AUTO,
                    vertical_alignment=alignment.center,
                    horizontal_alignment=alignment.center,
                    padding=0,
                )
            )

        if page.route == "/home/details":
            page.views.append(
                View(
                    "/details",
                    [
                        weather_indepth_body,
                    ],
                    scroll=ScrollMode.ALWAYS,
                    vertical_alignment=alignment.center,
                    horizontal_alignment=alignment.center,
                    padding=0,
                )
            )

    page.update()

    def view_pop():
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


app(target=main, assets_dir="assets")

app = 'app'
htmx = 'htmx'

dz_array = {
    "public": {
        "favicon": f"{app}/images/favicon.png",
        "description": "W3CMS  : Django CMS With Dashboard & FrontEnd Template",
        "og_title": "W3CMS  : Django CMS With Dashboard & FrontEnd Template",
        "og_description": "W3CMS  : Django CMS With Dashboard & FrontEnd Template",
        "og_image": "https://w3cms.dexignzone.com/django/social-image.png",
        "title": "W3CMS  : Django CMS With Dashboard & FrontEnd Template",
    },

    "app": {
        "htmx": [
            f"{htmx}/htmx.min.js",
            # f"{htmx}/class-tools.js",
            f"{htmx}/preload.js",
            f"{htmx}/_hyperscript.js",
            f"{htmx}/ext/ws.js",
            # f"{htmx}/ext/event-header.js",
        ],
        "global_css": {
            "top": [
                f"{app}/js/theme-script.js",
                f"{app}/css/bootstrap.min.css",
                f"{app}/plugins/tabler-icons/tabler-icons.min.css",
                f"{app}/plugins/fontawesome/css/fontawesome.min.css",
                f"{app}/plugins/fontawesome/css/all.min.css",
                f"{app}/plugins/simplebar/simplebar.min.css",
            ],
            "down": [
                f"{app}/css/iconsax.css",
                f"{app}/css/style.css",
            ],
        },
        "global_js": {
            "top": [
                f"{app}/js/jquery-3.7.1.min.js",
                f"{app}/js/feather.min.js",
                f"{app}/js/bootstrap.bundle.min.js",
                f"{app}/plugins/simplebar/simplebar.min.js",

            ],
            "down": [
                f"{app}/js/script.js",
            ],
        },
        "page_level": {
            "css": {
                "view": [
                    f"{app}/css/bootstrap-datetimepicker.min.css",
                    f"{app}/plugins/select2/css/select2.min.css",
                    f"{app}/css/dataTables.bootstrap5.min.css",
                ],
            },
            "js": {
                "view": [
                    f"{app}/plugins/select2/js/select2.min.js",
                    f"{app}/js/moment.min.js",
                    f"{app}/plugins/daterangepicker/daterangepicker.js",
                    f"{app}s/js/bootstrap-datetimepicker.min.js",
                    f"{app}/js/jquery.dataTables.min.js",
                    f"{app}/js/dataTables.bootstrap5.min.js",
                ]
                # "pos_order": [
                    # f"{app}/plugins/interactjs/dist/interact.js",
                # ],   
            },
        },
        "auth": {
            "css": [
                    f"{app}/css/bootstrap.min.css",
                    f"{app}/plugins/tabler-icons/tabler-icons.min.css",
                    f"{app}/css/iconsax.css",
                    f"{app}/css/style.css",
                ],
            "js": [
                    f"{app}/js/jquery-3.7.1.min.js",
                    f"{app}/js/bootstrap.bundle.min.js",
                    f"{app}/js/script.js",
                ],
            },
    }
}

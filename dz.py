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
            # f"{htmx}/ext/event-header.js",
        ],
        "global_css": [

        ],
        "global_js": {
            "top": [

            ],
            "down": [
            ],
        },
        "page_level": {
            "css": {
                # "pos_home": [
                    # f"{app}/css/pos.css",
                # ],
            },
            "js": {
                # "pos_order": [
                    # f"{app}/plugins/interactjs/dist/interact.js",
                # ],   
            },
        }
    }
}

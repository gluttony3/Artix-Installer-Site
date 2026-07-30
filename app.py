from flask import Flask, make_response, redirect, render_template, request, url_for
from content import CONTENT, LANGUAGE_FLAGS, LANGUAGES, NAV

app = Flask(__name__)
DEFAULT_LANG = "en"


def get_lang() -> str:
    lang = request.cookies.get("lang", DEFAULT_LANG)
    return lang if lang in LANGUAGES else DEFAULT_LANG


@app.route("/")
def index():
    lang = get_lang()
    page = CONTENT["index"][lang]
    return render_template(
        "page.html",
        title=page["title"],
        body=page["body"],
        nav=NAV[lang],
        lang=lang,
        languages=LANGUAGES,
        language_flags=LANGUAGE_FLAGS,
    )


@app.route("/problems")
def problems():
    lang = get_lang()
    page = CONTENT["problems"][lang]
    return render_template(
        "page.html",
        title=page["title"],
        body=page["body"],
        nav=NAV[lang],
        lang=lang,
        languages=LANGUAGES,
        language_flags=LANGUAGE_FLAGS,
    )


@app.route("/set_lang/<lang>")
def set_lang(lang):
    if lang not in LANGUAGES:
        lang = DEFAULT_LANG
    next_page = request.args.get("next") or request.referrer or url_for("index")
    response = make_response(redirect(next_page))
    response.set_cookie("lang", lang, max_age=60 * 60 * 24 * 30)
    return response


@app.route("/artix")
def artix():
    return redirect("https://artixlinux.org")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

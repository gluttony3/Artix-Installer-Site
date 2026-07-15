from flask import Flask, make_response, redirect, render_template, request, url_for
from translations import CONTENT, LANGUAGE_FLAGS, LANGUAGES, NAV

app = Flask(__name__)
DEFAULT_LANG = "en"


def get_lang() -> str:
    lang = request.cookies.get("lang", DEFAULT_LANG)
    return lang if lang in LANGUAGES else DEFAULT_LANG


def get_content(page: str, lang: str) -> dict:
    page_content = CONTENT.get(page, {})
    if lang not in page_content:
        lang = DEFAULT_LANG
    return page_content.get(lang, page_content.get(DEFAULT_LANG, {"title": "", "body": ""}))


@app.context_processor
def inject_globals():
    lang = get_lang()
    return dict(
        lang=lang,
        languages=LANGUAGES,
        language_flags=LANGUAGE_FLAGS,
        nav=NAV.get(lang, NAV[DEFAULT_LANG]),
    )


@app.route("/")
def index():
    content = get_content("index", get_lang())
    return render_template("index.html", content=content)


@app.route("/problems")
def problems():
    content = get_content("problems", get_lang())
    return render_template("problems.html", content=content)


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

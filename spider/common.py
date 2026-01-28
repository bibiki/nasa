def story_div(link, headline_func):
    return f"""<div class="story">
        <a href="{link}">{headline_func(link)}</a>
    </div>"""
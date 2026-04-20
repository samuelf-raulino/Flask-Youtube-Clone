def youtube_embed(url):
    if "watch?v=" in url:
        return url.replace("watch?v=", "embed/")
    return url

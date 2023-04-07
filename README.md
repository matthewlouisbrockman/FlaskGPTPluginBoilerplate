# FlaskGPTPluginBoilerplate

This is a repo that contains some boilerplate for getting started with a chatGPT plugin using a flask app. It provides solutions for several problems although I don't know what I'm doing so there's probably a bit to improve. Going to look at nextjs next.

I was hoping that this would work on replit but for some reason chatGPT and replit don't play nice (it works on localhost/heroku fine but runnign the exact code on Replit leads to some timeouts I need to go mess with)

Anyway, this provides:

- the config stuff (json/openapi yamls)
- endpoints that do stuff
- display text
- display images (sometimes lol)

To use, you need to add an environmental variable `DOMAIN` to your environment; otherwise it defaults to localhost:5000. It should work out of the box after installing with requirements.txt

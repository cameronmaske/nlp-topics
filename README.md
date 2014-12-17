## Topics API for [TrackMaven's NLP Meetup!](http://www.meetup.com/TrackMaven-Monthly-Challenge/)

Uses Gensim.


Requires [Docker](https://docs.docker.com/installation/) + [Fig](http://fig.sh)

To boot up, run
```
fig up.
```

Run blocks of text against the API endpoint with...

```
curl -H "Content-type: application/json" -X POST http://localdocker:5000/api/analyze/ -d '{"text":"Gold is a soft, heavy, shiny metal. It has been used for many thousands of years by people all over the world, for jewelry, decoration, and as money. Gold is important because it is rare, but also easier to use than other rare metals. It is also used to repair teeth and in electronic equipment such as computers. The color of this metal is also called gold."}'
```

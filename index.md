---
title: Home
---

<section class="intro" markdown="1">
I study how neural systems, biological and artificial, represent information and implement computations. After a PhD in systems and computational neuroscience, I now do mechanistic interpretability research on artificial neural networks, funded by Coefficient Giving.
</section>

<section class="news">
  <h2>Latest news</h2>
  <div class="news-scroll">
    {% for item in site.data.news %}
    <article class="news-item">
      <time datetime="{{ item.date }}">{{ item.label }}</time>
      <div>{{ item.text | markdownify }}</div>
    </article>
    {% endfor %}
  </div>
</section>

<section class="projects">
  <h2>Research</h2>
  <div class="card-grid">
    {% for p in site.data.projects %}
    <article class="card theme-{{ p.theme }}">
      <a class="card-image" href="{{ '/research' | relative_url }}#{{ p.id }}">
        {% if p.card_figure %}{% include {{ p.card_figure }} %}{% else %}<img src="{{ p.image | relative_url }}" alt="{{ p.alt }}" loading="lazy">{% endif %}
      </a>
      <div class="card-body">
        <p class="card-venue theme-{{ p.theme }}">{{ p.venue }}</p>
        <h3><a href="{{ '/research' | relative_url }}#{{ p.id }}">{{ p.title }}</a></h3>
        <p class="card-links">
          {% if p.paper %}<a href="{{ p.paper | relative_url }}">{{ p.paper_label | default: "Paper" }}</a>{% endif %}
          <a href="{{ '/research' | relative_url }}#{{ p.id }}">Read more →</a>
        </p>
      </div>
    </article>
    {% endfor %}
  </div>
</section>

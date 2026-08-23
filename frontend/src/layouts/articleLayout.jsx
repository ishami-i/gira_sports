import NewsArticleContent from "../content/newArticleContent";

/**
 * Wraps a single article's content with the shared masthead metadata
 * (kicker, headline, byline). Header/Footer come from SiteLayout, which
 * wraps every route — this component only concerns itself with the
 * article itself.
 */
const ArticleLayout = ({
  kicker = "Match Report",
  headline,
  byline,
  publishedOn,
  children,
}) => {
  return (
    <div className="w-full">
      {(headline || byline) && (
        <div className="max-w-3xl mx-auto px-4 pt-10 text-center">
          {kicker && (
            <span className="inline-block text-xs font-bold uppercase tracking-widest text-[var(--accent)] mb-3">
              {kicker}
            </span>
          )}
          {headline && (
            <h1 className="font-serif text-3xl md:text-5xl font-bold tracking-tight text-slate-950 leading-tight">
              {headline}
            </h1>
          )}
          {(byline || publishedOn) && (
            <p className="mt-4 text-sm text-slate-500">
              {byline}
              {byline && publishedOn && " · "}
              {publishedOn}
            </p>
          )}
        </div>
      )}
      <NewsArticleContent>{children}</NewsArticleContent>
    </div>
  );
};

export default ArticleLayout;

import { Link } from "react-router-dom";

const HEADLINES = [
  {
    kicker: "Match Report",
    title: "Late strike sends Gira City through to the final",
    blurb: "A stoppage-time header settled a tense semi-final on Saturday.",
    to: "/blog/demo",
  },
  {
    kicker: "Transfer News",
    title: "Three clubs circle as contract talks stall",
    blurb: "Sources close to the deal say a decision is expected this week.",
    to: "/blog",
  },
  {
    kicker: "Analysis",
    title: "How the back three finally clicked",
    blurb: "A tactical breakdown of the shift that turned the season around.",
    to: "/blog",
  },
];

const HomePage = () => {
  return (
    <div className="w-full">
      {/* Hero */}
      <section className="border-b border-[var(--border)]">
        <div className="max-w-5xl mx-auto px-6 py-16 md:py-24 text-center">
          <span className="inline-block text-xs font-bold uppercase tracking-widest text-[var(--accent)] mb-4">
            Gira Sports
          </span>
          <h1 className="font-serif text-4xl md:text-6xl font-bold tracking-tight text-slate-950 leading-tight max-w-3xl mx-auto">
            The whole match, told properly.
          </h1>
          <p className="mt-5 text-lg text-slate-600 max-w-xl mx-auto">
            Scores, fixtures, and reporting worth reading — updated as the
            action happens.
          </p>
          <div className="mt-8 flex items-center justify-center gap-3">
            <Link
              to="/scores"
              className="px-5 py-2.5 rounded-full text-sm font-semibold text-white bg-slate-900 hover:bg-slate-800 transition-colors"
            >
              See today's scores
            </Link>
            <Link
              to="/blog"
              className="px-5 py-2.5 rounded-full text-sm font-semibold text-slate-700 border border-slate-300 hover:border-slate-400 transition-colors"
            >
              Read the blog
            </Link>
          </div>
        </div>
      </section>

      {/* Headlines */}
      <section className="max-w-5xl mx-auto px-6 py-14">
        <h2 className="text-sm font-bold uppercase tracking-widest text-slate-400 mb-6">
          Top Stories
        </h2>
        <div className="grid gap-8 md:grid-cols-3">
          {HEADLINES.map((item) => (
            <Link
              key={item.title}
              to={item.to}
              className="group block border-t border-[var(--border)] pt-5"
            >
              <span className="text-xs font-bold uppercase tracking-widest text-[var(--accent)]">
                {item.kicker}
              </span>
              <h3 className="mt-2 font-serif text-xl font-bold text-slate-950 leading-snug group-hover:underline">
                {item.title}
              </h3>
              <p className="mt-2 text-sm text-slate-600">{item.blurb}</p>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
};

export default HomePage;

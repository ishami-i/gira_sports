
const PlaceholderPage = ({ title, description = "This section is coming soon." }) => {
  return (
    <div className="flex-1 flex flex-col items-center justify-center text-center px-6 py-24">
      <span className="text-xs font-bold uppercase tracking-widest text-[var(--accent)] mb-3">
        Gira Sports
      </span>
      <h1 className="font-serif text-3xl md:text-4xl font-bold text-slate-950 mb-3">
        {title}
      </h1>
      <p className="text-slate-500 max-w-md">{description}</p>
    </div>
  );
};

export default PlaceholderPage;

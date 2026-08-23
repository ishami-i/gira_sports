
const NewsArticleContent = ({ children }) => {
  return (
    <article className="max-w-3xl mx-auto px-4 py-8 bg-white text-slate-950 font-serif antialiased selection:bg-amber-100">
      {/* Article Typography Wrapper */}
      <div 
        className="
          text-lg md:text-xl 
          leading-relaxed md:leading-loose 
          text-slate-800 
          space-y-6 
          
          /* Drop Cap Styling (Applies to the very first letter of the first paragraph) */
          first-of-type:p:first-letter:text-6xl 
          first-of-type:p:first-letter:md:text-7xl 
          first-of-type:p:first-letter:font-black 
          first-of-type:p:first-letter:font-sans 
          first-of-type:p:first-letter:float-left 
          first-of-type:p:first-letter:mr-3 
          first-of-type:p:first-letter:mt-1 
          first-of-type:p:first-letter:text-slate-900
          first-of-type:p:first-letter:leading-none
        "
      >
        {children || (
          <>
            <p>
              The digital landscape is shifting rapidly as news platforms embrace micro-layouts 
              for cleaner reading experiences. By isolating the core article structure away from 
              cluttered sidebars, developers can focus purely on typographical legibility and user 
              engagement metrics.
            </p>
            <p>
              In modern web editorial design, the traditional drop cap serves as both an aesthetic 
              anchor and a visual signal to the reader where the narrative journey begins. Using 
              CSS utilities allows this to render dynamically without manual element splitting.
            </p>
          </>
        )}
      </div>
    </article>
  );
};

export default NewsArticleContent;
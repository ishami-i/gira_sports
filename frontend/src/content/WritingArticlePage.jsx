import React, { useState } from "react";

const EditorialWritingLayout = () => {
  const [headline, setHeadline] = useState("");
  const [bodyText, setBodyText] = useState("");
  const [wordCount, setWordCount] = useState(0);

  // Update text and automatically compute simple word metrics
  const handleTextChange = (e) => {
    const text = e.target.value;
    setBodyText(text);
    const words = text.trim() ? text.trim().split(/\s+/).length : 0;
    setWordCount(words);
  };

  return (
    <div className="h-screen flex flex-col bg-slate-50 text-slate-900 font-sans overflow-hidden">
      
      {/* 1. Global Editor Control Header */}
      <header className="h-14 border-b border-slate-200 bg-white px-4 flex items-center justify-between shrink-0 select-none">
        <div className="flex items-center space-x-3">
          <span className="bg-red-600 text-white font-serif tracking-tighter text-sm font-black px-2 py-0.5 rounded">NC</span>
          <h1 className="text-xs font-bold uppercase tracking-wider text-slate-500">Newsroom Composer v2.0</h1>
        </div>
        <div className="flex items-center space-x-2">
          <span className="text-xs text-slate-400 mr-2 font-mono">{wordCount} words</span>
          <button className="px-3 py-1.5 text-xs font-semibold text-slate-600 hover:bg-slate-100 rounded transition"> Save Draft </button>
          <button className="px-3 py-1.5 text-xs font-bold text-white bg-slate-900 hover:bg-slate-800 rounded shadow-sm transition"> Submit to Edit </button>
        </div>
      </header>

      {/* Main Multi-Pane Workspace Container */}
      <div className="flex flex-1 overflow-hidden w-full">
        
        {/* 2. Left Rail: Formatting Utilities & Elements Toolbar */}
        <nav className="w-16 border-r border-slate-200 bg-white flex flex-col items-center py-4 space-y-4 shrink-0 select-none">
          <button title="Bold text" className="p-2 text-slate-400 hover:text-slate-800 hover:bg-slate-100 rounded-lg transition">
            <span className="font-bold text-sm">B</span>
          </button>
          <button title="Italic text" className="p-2 text-slate-400 hover:text-slate-800 hover:bg-slate-100 rounded-lg transition">
            <span className="italic text-sm">I</span>
          </button>
          <button title="Insert Image block" className="p-2 text-slate-400 hover:text-slate-800 hover:bg-slate-100 rounded-lg transition">
            <span className="text-xs block">📷</span>
          </button>
          <button title="Insert Blockquote" className="p-2 text-slate-400 hover:text-slate-800 hover:bg-slate-100 rounded-lg transition">
            <span className="font-serif text-sm">“ ”</span>
          </button>
          <div className="w-8 border-b border-slate-200 my-2"></div>
          <button title="Layout Settings" className="p-2 text-slate-300 hover:text-slate-600 rounded-lg transition">
            <span className="text-sm">⚙️</span>
          </button>
        </nav>

        {/* 3. Center Column: Clean Writing Canvas */}
        <main className="flex-1 bg-white overflow-y-auto px-8 md:px-12 py-10 flex justify-center border-r border-slate-200">
          <div className="w-full max-w-2xl flex flex-col space-y-4 h-full">
            {/* Headline Entry Input */}
            <input 
              type="text"
              placeholder="Type your working headline here..."
              value={headline}
              onChange={(e) => setHeadline(e.target.value)}
              className="w-full text-3xl font-serif font-black border-none outline-none focus:ring-0 placeholder:text-slate-200 p-0 text-slate-900"
            />
            <hr className="border-slate-100" />
            {/* Main Text Content Entry Canvas */}
            <textarea
              placeholder="Compose your article story. Use double returns to separate paragraphs. Check out the live typography preview layout instantly on your right..."
              value={bodyText}
              onChange={handleTextChange}
              className="w-full flex-1 border-none outline-none focus:ring-0 font-serif text-base leading-relaxed text-slate-800 placeholder:text-slate-300 resize-none p-0"
            />
          </div>
        </main>

        {/* 4. Right Rail: Live Drop-Cap Desktop Editorial Preview */}
        <aside className="hidden lg:block w-96 bg-slate-50 overflow-y-auto p-6 shrink-0 select-none">
          <h2 className="text-[10px] font-bold uppercase tracking-widest text-slate-400 mb-3 block">Live Production Layout</h2>
          
          <div className="bg-white border border-slate-200/60 rounded-lg p-5 shadow-sm min-h-[400px]">
            {/* Meta Tags */}
            <span className="inline-block border border-red-500 text-red-600 text-[9px] font-extrabold uppercase tracking-widest px-1.5 py-0.5 rounded mb-3">
              LIVE PREVIEW
            </span>

            {/* Dynamic Headline Render */}
            <h3 className="font-serif text-xl font-bold tracking-tight text-slate-950 leading-tight mb-4 break-words">
              {headline || "Untitled Working Draft"}
            </h3>

            {/* Structured Article Preview Canvas with Drop-Cap Logic */}
            <div 
              className="
                font-serif text-sm leading-relaxed text-slate-800 space-y-4 break-words whitespace-pre-wrap
                first-of-type:p:first-letter:text-5xl 
                first-of-type:p:first-letter:font-black 
                first-of-type:p:first-letter:font-sans 
                first-of-type:p:first-letter:float-left 
                first-of-type:p:first-letter:mr-2 
                first-of-type:p:first-letter:mt-0.5 
                first-of-type:p:first-letter:text-slate-900
                first-of-type:p:first-letter:leading-none
              "
            >
              {bodyText ? (
                bodyText.split("\n\n").map((paragraph, index) => <p key={index}>{paragraph}</p>)
              ) : (
                <p className="text-slate-400 font-sans text-xs italic">Your editorial drop-cap typography layout generates instantly here as soon as text is provided into the central drafting column.</p>
              )}
            </div>
          </div>
        </aside>

      </div>
    </div>
  );
};

export default EditorialWritingLayout;
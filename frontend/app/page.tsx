import React from 'react';

export default function Home() {
  return (
    <div className="min-h-screen bg-white text-slate-900 font-sans selection:bg-blue-100">
      {/* 상단 네비게이션 */}
      <nav className="flex justify-between items-center py-6 px-10 sticky top-0 bg-white/80 backdrop-blur-md z-50 border-b border-slate-50">
        <div className="text-2xl font-black text-blue-600 tracking-tighter cursor-pointer">GONY LABS</div>
        <div className="hidden md:flex space-x-10 font-semibold text-slate-500">
          <a href="#projects" className="hover:text-blue-600 transition-colors">Projects</a>
          <a href="#tech" className="hover:text-blue-600 transition-colors">Tech Stack</a>
          <a href="#blog" className="hover:text-blue-600 transition-colors">Blog</a>
        </div>
        <button className="bg-slate-900 text-white px-6 py-2.5 rounded-full font-bold hover:bg-blue-600 transition-all shadow-xl shadow-slate-200">
          Contact Me
        </button>
      </nav>

      {/* 히어로 섹션 */}
      <section className="pt-24 pb-32 px-10">
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row items-center gap-16">
          <div className="flex-[1.2] text-left">
            <div className="inline-block px-4 py-1.5 bg-blue-50 text-blue-600 rounded-full text-sm font-bold mb-6">
              Next Step: AI Full-Stack Developer
            </div>
            <h1 className="text-7xl font-extrabold leading-[1.1] mb-8 tracking-tight">
              유지보수를 넘어 <br />
              <span className="text-blue-600 italic">지능형 서비스</span>로
            </h1>
            <p className="text-xl text-slate-500 mb-10 leading-relaxed max-w-xl font-medium">
              1인 개발팀의 실무 역량과 <br />
              최신 AI 기술을 결합하여 가치를 만듭니다.
            </p>
            <div className="flex gap-4">
              <button className="bg-blue-600 text-white px-10 py-4 rounded-2xl font-bold text-lg hover:bg-blue-700 transition-all shadow-lg shadow-blue-200">
                Explore Projects
              </button>
              <button className="border border-slate-200 text-slate-600 px-10 py-4 rounded-2xl font-bold text-lg hover:bg-slate-50 transition-all">
                Github
              </button>
            </div>
          </div>
          
          {/* Gony 캐릭터가 들어갈 자리 */}
          <div className="flex-1 w-full aspect-square bg-gradient-to-br from-blue-50 to-indigo-50 rounded-[4rem] relative flex items-center justify-center overflow-hidden border-8 border-white shadow-2xl">
            <div className="text-slate-300 text-center">
              <div className="text-8xl mb-4 animate-bounce">🎨</div>
              <p className="font-bold text-lg text-slate-400 tracking-widest uppercase">Gony Visual Space</p>
            </div>
          </div>
        </div>
      </section>

      {/* 푸터 */}
      <footer className="py-20 border-t border-slate-100 text-center">
        <p className="text-slate-400 font-medium italic">"The best way to predict the future is to invent it."</p>
      </footer>
    </div>
  );
}
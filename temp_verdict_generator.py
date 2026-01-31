
import base64

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2030 Sovereign Engine Verdict</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&family=Syncopate:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body { background-color: #020617; color: #fff; font-family: 'Rajdhani', sans-serif; overflow: hidden; }
        .font-cyber { font-family: 'Syncopate', sans-serif; text-transform: uppercase; }
        .glass-panel {
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .glow-text { text-shadow: 0 0 20px rgba(56, 189, 248, 0.5); }
        .glow-amber { text-shadow: 0 0 20px rgba(245, 158, 11, 0.5); }
        
        @keyframes scanline {
            0% { top: 0%; }
            100% { top: 100%; }
        }
        .scan-line {
            position: fixed; top: 0; left: 0; width: 100%; height: 2px;
            background: rgba(56, 189, 248, 0.3);
            box-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
            animation: scanline 3s linear infinite;
            pointer-events: none;
            z-index: 50;
        }

        /* Barbell Visuals */
        .sphere {
            box-shadow: inset -10px -10px 40px rgba(0,0,0,0.8), 0 0 30px rgba(255,255,255,0.1);
        }
        .middle-ground {
            background: repeating-linear-gradient(45deg, #ef4444, #ef4444 10px, #b91c1c 10px, #b91c1c 20px);
            opacity: 0.2;
        }
    </style>
</head>
<body class="w-full h-screen flex flex-col items-center justify-center relative p-8">
    <div class="scan-line"></div>
    
    <!-- Background Grid -->
    <div class="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)] bg-[size:40px_40px] pointer-events-none"></div>

    <!-- Header -->
    <header class="text-center mb-12 relative z-10">
        <div class="text-blue-500 font-bold tracking-[0.5em] text-xs mb-2 animate-pulse">SYSTEM FINALIZATION</div>
        <h1 class="text-5xl md:text-7xl font-black font-cyber glow-text mb-4">2030 Sovereign Engine</h1>
        <div class="w-24 h-1 bg-blue-500 mx-auto"></div>
    </header>

    <!-- Main Content Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 w-full max-w-7xl relative z-10 items-center">
        
        <!-- LEFT: SCALE -->
        <div class="glass-panel p-8 rounded-3xl border-l-4 border-blue-500 transform hover:scale-105 transition-all duration-500 group">
            <h2 class="text-4xl font-black mb-2 font-cyber text-blue-400">SCALE</h2>
            <div class="text-xs text-slate-400 tracking-widest mb-6">INFRASTRUCTURE DOMINANCE</div>
            <div class="space-y-4">
                <div class="flex justify-between items-center border-b border-white/10 pb-2">
                    <span class="opacity-60">Entity</span>
                    <span class="font-bold">JPM Chase</span>
                </div>
                <div class="flex justify-between items-center border-b border-white/10 pb-2">
                    <span class="opacity-60">Valuation</span>
                    <span class="font-bold text-blue-400">1.45x Premium</span>
                </div>
                <div class="flex justify-between items-center border-b border-white/10 pb-2">
                    <span class="opacity-60">Status</span>
                    <span class="font-bold text-green-400">OPTIMIZED</span>
                </div>
            </div>
            <div class="mt-6 text-sm text-slate-300 leading-relaxed">
                "The Vault." Massive balance sheets providing the secure rails for global liquidity.
            </div>
            <div class="mt-6 w-full h-32 bg-blue-900/20 rounded-full sphere relative overflow-hidden flex items-center justify-center">
                <div class="absolute w-full h-full bg-blue-500 blur-[80px] opacity-40 animate-pulse"></div>
                <span class="text-6xl">🏛️</span>
            </div>
        </div>

        <!-- CENTER: THE VOID (QUOTES) -->
        <div class="text-center relative">
            <!-- Warning Tape -->
            <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[120%] h-24 middle-ground -skew-y-6 z-0 border-y border-red-500/50"></div>
            
            <div class="relative z-10 bg-black/80 backdrop-blur-xl p-8 rounded-2xl border border-red-500/30 shadow-[0_0_50px_rgba(239,68,68,0.2)]">
                <div class="text-red-500 font-bold tracking-[0.3em] text-xs mb-4 animate-pulse">WARNING: MIDDLE GROUND COLLAPSE</div>
                <h3 class="text-2xl font-bold italic text-white mb-6 leading-relaxed font-cyber">
                    "The Barbell Market concludes."
                </h3>
                <p class="text-lg text-slate-300 mb-2">Scale vs Experience.</p>
                <div class="text-4xl font-black text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-white to-amber-400">
                    NO MIDDLE GROUND
                </div>
            </div>
        </div>

        <!-- RIGHT: EXPERIENCE -->
        <div class="glass-panel p-8 rounded-3xl border-r-4 border-amber-500 transform hover:scale-105 transition-all duration-500 group text-right">
            <h2 class="text-4xl font-black mb-2 font-cyber text-amber-400">EXPERIENCE</h2>
            <div class="text-xs text-slate-400 tracking-widest mb-6">LOGIC VELOCITY</div>
            <div class="space-y-4">
                <div class="flex justify-between items-center border-b border-white/10 pb-2 flex-row-reverse">
                    <span class="opacity-60">Entity</span>
                    <span class="font-bold">India Stack</span>
                </div>
                <div class="flex justify-between items-center border-b border-white/10 pb-2 flex-row-reverse">
                    <span class="opacity-60">Coverage</span>
                    <span class="font-bold text-amber-400">99% Population</span>
                </div>
                <div class="flex justify-between items-center border-b border-white/10 pb-2 flex-row-reverse">
                    <span class="opacity-60">Cost</span>
                    <span class="font-bold text-green-400">Near Zero</span>
                </div>
            </div>
            <div class="mt-6 text-sm text-slate-300 leading-relaxed">
                "The Brain." Agentic AI orchestration moving value at the speed of thought.
            </div>
            <div class="mt-6 w-full h-32 bg-amber-900/20 rounded-full sphere relative overflow-hidden flex items-center justify-center">
                <div class="absolute w-full h-full bg-amber-500 blur-[80px] opacity-40 animate-pulse" style="animation-delay: 1s;"></div>
                <span class="text-6xl">🧠</span>
            </div>
        </div>

    </div>

    <!-- Footer Stats -->
    <div class="mt-16 grid grid-cols-2 md:grid-cols-4 gap-4 w-full max-w-5xl">
        <div class="glass-panel p-4 rounded-xl text-center">
            <div class="text-xs text-slate-500 uppercase tracking-widest">Valuation Delta</div>
            <div class="text-2xl font-bold text-green-400">1.45x</div>
        </div>
        <div class="glass-panel p-4 rounded-xl text-center">
            <div class="text-xs text-slate-500 uppercase tracking-widest">API Calls (Mo)</div>
            <div class="text-2xl font-bold text-blue-400">1.2B</div>
        </div>
        <div class="glass-panel p-4 rounded-xl text-center">
            <div class="text-xs text-slate-500 uppercase tracking-widest">Unit Cost</div>
            <div class="text-2xl font-bold text-amber-400">$0.02</div>
        </div>
        <div class="glass-panel p-4 rounded-xl text-center">
            <div class="text-xs text-slate-500 uppercase tracking-widest">System Status</div>
            <div class="text-2xl font-bold text-white animate-pulse">ALIVE</div>
        </div>
    </div>

</body>
</html>"""

encoded_html = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
print(encoded_html)

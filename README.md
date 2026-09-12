# 💫 About Me:
<svg width="1200" height="420" viewBox="0 0 1200 420"
     xmlns="http://www.w3.org/2000/svg">

  <defs>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#163322" stroke-width="1"/>
    </pattern>

    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1200" height="420" rx="22" fill="#07100b"/>
  <rect x="1" y="1" width="1198" height="418" rx="21"
        fill="none" stroke="#16a35a" stroke-width="2"/>

  <!-- Grid -->
  <rect x="610" y="75" width="550" height="275" fill="url(#grid)" opacity=".75"/>

  <!-- Terminal header -->
  <line x1="1" y1="62" x2="1199" y2="62" stroke="#16a35a" opacity=".7"/>
  <circle cx="30" cy="31" r="7" fill="#ff5f56"/>
  <circle cx="54" cy="31" r="7" fill="#ffbd2e"/>
  <circle cx="78" cy="31" r="7" fill="#27c93f"/>

  <text x="105" y="38"
        fill="#b8d8c3" font-family="monospace" font-size="18">
    vatsal@github:~
  </text>

  <text x="1015" y="38"
        fill="#20d878" font-family="monospace" font-size="15">
    BUILD / LEARN / SOLVE
  </text>

  <!-- Main terminal -->
  <text x="55" y="105"
        fill="#20d878" font-family="monospace" font-size="20">
    $ ./whoami
  </text>

  <text x="55" y="155"
        fill="#39f28a" font-family="monospace"
        font-size="42" font-weight="700">
    VATSAL BHARDWAJ
  </text>

  <text x="55" y="190"
        fill="#d7e7dc" font-family="monospace" font-size="18">
    Backend • ML • Systems • Simulation
  </text>

  <text x="55" y="225"
        fill="#8fb69d" font-family="monospace" font-size="15">
    "Turning complex ideas into working systems."
  </text>

  <!-- Animated terminal lines -->
  <g fill="#20d878" font-family="monospace" font-size="15">
    <text x="55" y="260">&gt; building scalable backend systems</text>
    <text x="55" y="285">&gt; exploring machine learning</text>
    <text x="55" y="310">&gt; understanding systems under the hood</text>
    <text x="55" y="335">&gt; always learning. always building.</text>
  </g>

  <!-- Blinking cursor -->
  <rect x="55" y="352" width="10" height="19" fill="#39f28a" filter="url(#glow)">
    <animate attributeName="opacity"
             values="1;0;1"
             dur="1s"
             repeatCount="indefinite"/>
  </rect>

  <!-- Animated status panel -->
  <rect x="720" y="95" width="390" height="105" rx="12"
        fill="#091810" stroke="#166b3e"/>

  <text x="745" y="125"
        fill="#6e9a7b" font-family="monospace" font-size="13">
    SYSTEM STATUS
  </text>

  <circle cx="750" cy="158" r="7" fill="#20d878" filter="url(#glow)">
    <animate attributeName="opacity"
             values=".35;1;.35"
             dur="1.6s"
             repeatCount="indefinite"/>
  </circle>

  <text x="770" y="164"
        fill="#20d878" font-family="monospace" font-size="17">
    ONLINE
  </text>

  <text x="745" y="188"
        fill="#9bbca5" font-family="monospace" font-size="13">
    learning / building / exploring
  </text>

  <!-- Animated signal bars -->
  <g fill="#20d878">
    <rect x="730" y="285" width="10" height="20">
      <animate attributeName="height" values="20;42;20" dur="1.2s" repeatCount="indefinite"/>
      <animate attributeName="y" values="285;263;285" dur="1.2s" repeatCount="indefinite"/>
    </rect>
    <rect x="750" y="275" width="10" height="30">
      <animate attributeName="height" values="30;55;30" dur="1.4s" repeatCount="indefinite"/>
      <animate attributeName="y" values="275;250;275" dur="1.4s" repeatCount="indefinite"/>
    </rect>
    <rect x="770" y="260" width="10" height="45">
      <animate attributeName="height" values="45;70;45" dur="1.1s" repeatCount="indefinite"/>
      <animate attributeName="y" values="260;235;260" dur="1.1s" repeatCount="indefinite"/>
    </rect>
    <rect x="790" y="245" width="10" height="60">
      <animate attributeName="height" values="60;82;60" dur="1.5s" repeatCount="indefinite"/>
      <animate attributeName="y" values="245;223;245" dur="1.5s" repeatCount="indefinite"/>
    </rect>
  </g>

  <text x="830" y="275"
        fill="#6e9a7b" font-family="monospace" font-size="13">
    CURRENT PROCESS
  </text>
  <text x="830" y="300"
        fill="#d7e7dc" font-family="monospace" font-size="14">
    learn → build → break
  </text>
  <text x="830" y="322"
        fill="#d7e7dc" font-family="monospace" font-size="14">
    debug → improve → repeat
  </text>

  <!-- Footer -->
  <line x1="1" y1="390" x2="1199" y2="390" stroke="#16a35a" opacity=".7"/>
  <text x="55" y="410"
        fill="#467257" font-family="monospace" font-size="12">
    01100010 01110101 01101001 01101100 01100100
  </text>

</svg>

<div align="center">
  <img src="assets/vatsal_animated_header.svg"
       width="100%"
       alt="Vatsal Bhardwaj">
</div>
## `~/` whoami<br><br>```console<br>$ ./whoami<br>```<br><br>```text<br>Vatsal Bhardwaj<br>────────────────────────────────────────────<br>Backend Engineer in progress.<br>Problem solver by habit.<br>Builder by choice.<br>```<br><br>I like taking complicated ideas, pulling them apart, and figuring out how to make them work.<br><br>My interests sit around **backend engineering, machine learning, system design, and simulation** — especially projects where there's more happening underneath than what you see on the screen.<br><br>```console<br>$ cat interests.txt<br><br>→ Backend & APIs<br>→ Machine Learning<br>→ System Design<br>→ Simulation & Modeling<br>→ Competitive Programming<br>→ Building things that shouldn't exist yet<br>```<br><br>```console<br>$ git status<br><br>On branch: learning<br>Status: constantly experimenting<br><br>Things I believe:<br>  • Good software starts with understanding the problem.<br>  • The best way to learn a system is to build one.<br>  • "It works" is the beginning, not the end.<br>  • Debugging is just detective work with better error messages.<br>```<br><br>```console<br>$ ./current_process<br><br>Learn → Build → Break → Debug → Improve → Repeat<br>```<br><br><sub>01100010 01110101 01101001 01101100 01100100 00101110 01100100 01100101 01100010 01110101 01100111 00101110 01110010 01100101 01110000 01100101 01100001 01110100</sub><br>


## 🌐 Socials:
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/vatsalbhardwaj._) [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/vatsalbhardwaj007) [![Pinterest](https://img.shields.io/badge/Pinterest-%23E60023.svg?logo=Pinterest&logoColor=white)](https://pinterest.com/vatsalbhardwaj007) [![Reddit](https://img.shields.io/badge/Reddit-%23FF4500.svg?logo=Reddit&logoColor=white)](https://reddit.com/user/u/vb2802) [![X](https://img.shields.io/badge/X-black.svg?logo=X&logoColor=white)](https://x.com/VatsalBhardwaj7) [![email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:abhilav.bhardwaj007@gmail.com) 

# 💻 Tech Stack:
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=plastic&logo=c%2B%2B&logoColor=white) ![C](https://img.shields.io/badge/c-%2300599C.svg?style=plastic&logo=c&logoColor=white) ![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=plastic&logo=openjdk&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=plastic&logo=html5&logoColor=white) ![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=plastic&logo=markdown&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54) ![PowerShell](https://img.shields.io/badge/PowerShell-%235391FE.svg?style=plastic&logo=powershell&logoColor=white) ![Windows Terminal](https://img.shields.io/badge/Windows%20Terminal-%234D4D4D.svg?style=plastic&logo=windows-terminal&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=plastic&logo=css3&logoColor=white) ![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=plastic&logo=Cloudflare&logoColor=white) ![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=plastic&logo=google-cloud&logoColor=white) ![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=plastic&logo=vercel&logoColor=white) ![Netlify](https://img.shields.io/badge/netlify-%23000000.svg?style=plastic&logo=netlify&logoColor=#00C7B7) ![Firebase](https://img.shields.io/badge/firebase-%23039BE5.svg?style=plastic&logo=firebase) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=plastic&logo=amazon-aws&logoColor=white) ![.Net](https://img.shields.io/badge/.NET-5C2D91?style=plastic&logo=.net&logoColor=white) ![Angular.js](https://img.shields.io/badge/angular.js-%23E23237.svg?style=plastic&logo=angularjs&logoColor=white) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=plastic&logo=react&logoColor=%2361DAFB) ![PNPM](https://img.shields.io/badge/pnpm-%234a4a4a.svg?style=plastic&logo=pnpm&logoColor=f69220) ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=plastic&logo=node.js&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=plastic&logo=fastapi) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=plastic&logo=postgresql&logoColor=white) ![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=plastic&logo=supabase&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=plastic&logo=mysql&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=plastic&logo=mongodb&logoColor=white) ![Adobe Acrobat Reader](https://img.shields.io/badge/Adobe%20Acrobat%20Reader-EC1C24.svg?style=plastic&logo=Adobe%20Acrobat%20Reader&logoColor=white) ![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=plastic&logo=Canva&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=plastic&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=plastic&logo=pandas&logoColor=white) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=plastic&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=plastic&logo=github&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=plastic&logo=nginx&logoColor=white) ![Three js](https://img.shields.io/badge/threejs-black?style=plastic&logo=three.js&logoColor=white) ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=plastic&logo=opencv&logoColor=white) ![NPM](https://img.shields.io/badge/NPM-%23CB3837.svg?style=plastic&logo=npm&logoColor=white) ![Next JS](https://img.shields.io/badge/Next-black?style=plastic&logo=next.js&logoColor=white) ![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-FFFFFF?&style=plastic&logo=opentelemetry&logoColor=black) ![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=plastic&logo=notion&logoColor=white) ![Portfolio](https://img.shields.io/badge/Portfolio-%23000000.svg?style=plastic&logo=firefox&logoColor=#FF7139)
# 📊 GitHub Stats:
![](https://github-readme-stats.shion.dev/api?username=vatsalbhardwaj007&theme=merko&hide_border=false&include_all_commits=true&count_private=true)<br/>
![](https://streak-stats.demolab.com/?user=vatsalbhardwaj007&theme=merko&hide_border=false)<br/>
![](https://github-readme-stats.shion.dev/api/top-langs/?username=vatsalbhardwaj007&theme=merko&hide_border=false&include_all_commits=true&count_private=true&layout=compact)

## 🏆 GitHub Trophies
![](https://github-profile-trophy.vercel.app/?username=vatsalbhardwaj007&theme=radical&no-frame=false&no-bg=false&margin-w=4)

### ✍️ Random Dev Quote
![](https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical)

### 🔝 Top Contributed Repo
![](https://github-contributor-stats.vercel.app/api?username=vatsalbhardwaj007&limit=5&theme=merko&combine_all_yearly_contributions=true)

---
[![](https://komarev.com/ghpvc/?username=vatsalbhardwaj007&icon=2&color=1)](https://visitcount.itsvg.in)

<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->

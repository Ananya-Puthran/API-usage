const modules = {

"concept-explainer": {
title: "AI Concept Explainer",
description: "Explain AI topics in different personalities.",
themes: ["Academic", "Beginner", "Pirate", "Bandit"]
},

"structured-generator": {
title: "Structured Answer Generator",
description: "Generate clear structured answers for questions.",
themes: []
},

"rag-assistant": {
title: "RAG Academic Assistant",
description: "Ask questions based on retrieved knowledge.",
themes: ["Academic"]
},

"resume-agent": {
title: "Resume Review Agent",
description: "Analyze resumes and suggest improvements.",
themes: []
},

"prompt-lab": {
title: "Prompt Engineering Lab",
description: "Experiment with different prompt styles.",
themes: ["Creative", "Formal"]
},

"ai-tools": {
title: "AI Tools Assistant",
description: "Understand which AI tools to use for tasks.",
themes: []
}

}

const params = new URLSearchParams(window.location.search)
const moduleKey = params.get("module")

const moduleData = modules[moduleKey]

document.getElementById("moduleTitle").innerText = moduleData.title
document.getElementById("moduleDescription").innerText = moduleData.description

const themeContainer = document.getElementById("themeButtons")

if(moduleData.themes.length > 0){

moduleData.themes.forEach(theme => {

const btn = document.createElement("button")
btn.innerText = theme
btn.onclick = () => setTheme(theme)

themeContainer.appendChild(btn)

})

}
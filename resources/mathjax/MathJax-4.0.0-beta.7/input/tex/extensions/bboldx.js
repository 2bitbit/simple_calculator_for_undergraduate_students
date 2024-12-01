(()=>{"use strict";var b={d:(t,a)=>{for(var o in a)b.o(a,o)&&!b.o(t,o)&&Object.defineProperty(t,o,{enumerable:!0,get:a[o]})},o:(b,t)=>Object.prototype.hasOwnProperty.call(b,t),r:b=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(b,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(b,"__esModule",{value:!0})}},t={};b.r(t),b.d(t,{BboldxMethods:()=>g});var a={};b.r(a),b.d(a,{BboldxConfiguration:()=>B});const o=("undefined"!=typeof window?window:global).MathJax._.components.global,e=(o.GLOBAL,o.isObject,o.combineConfig,o.combineDefaults),l=o.combineWithMathJax,x=(o.MathJax,MathJax._.input.tex.HandlerTypes),i=x.ConfigurationType,d=x.HandlerType,n=MathJax._.input.tex.Configuration,r=n.Configuration,m=(n.ConfigurationHandler,n.ParserConfiguration,MathJax._.input.tex.TokenMap),f=(m.parseResult,m.AbstractTokenMap,m.RegExpMap,m.AbstractParseMap,m.CharacterMap),s=m.DelimiterMap,h=(m.MacroMap,m.CommandMap),c=(m.EnvironmentMap,MathJax._.input.tex.textmacros.TextMacrosMethods.TextMacrosMethods),p=MathJax._.input.tex.base.BaseMethods,u=(p.splitAlignArray,p.default),g={Macro:u.Macro,ChooseFont:function(b,t,a,o,e){const l=M(b,a,o,e);u.MathFont(b,t,l)},ChooseTextFont:function(b,t,a,o,e){const l=M(b,a,o,e);c.TextFont(b,t,l)},mathchar0miNormal:function(b,t){const a=M(b,"-bboldx","-bboldx-light","-bboldx-bold"),o=b.create("token","mi",{mathvariant:a},t.char);b.Push(o)},delimiterNormal:function(b,t){const a={fence:!1,stretchy:!1,mathvariant:M(b,"-bboldx","-bboldx-light","-bboldx-bold")},o=b.create("token","mo",a,t.char);b.Push(o)},mathchar0miBold:function(b,t){const a=M(b,"-bboldx-bold","-bboldx","-bboldx-bold"),o=b.create("token","mi",{mathvariant:a},t.char);b.Push(o)},delimiterBold:function(b,t){const a={fence:!1,stretchy:!1,mathvariant:M(b,"-bboldx-bold","-bboldx","-bboldx-bold")},o=b.create("token","mo",a,t.char);b.Push(o)}};function M(b,t,a,o){var e,l;if(!(null===(e=b.options)||void 0===e?void 0:e.bboldx))return t;const x=null===(l=b.options)||void 0===l?void 0:l.bboldx;return x.bfbb?o:x.light?a:t}new f("bboldx-mathchar0miNormal",g.mathchar0miNormal,{bbGamma:"\u0393",bbDelta:"\u2206",bbTheta:"\u0398",bbLambda:"\u039b",bbXi:"\u039e",bbPi:"\u03a0",bbSigma:"\u03a3",bbUpsilon:"\u03a5",bbPhi:"\u03a6",bbPsi:"\u03a8",bbOmega:"\u2126",bbalpha:"\u03b1",bbbeta:"\u03b2",bbgamma:"\u03b3",bbdelta:"\u03b4",bbepsilon:"\u03b5",bbzeta:"\u03b6",bbeta:"\u03b7",bbtheta:"\u03b8",bbiota:"\u03b9",bbkappa:"\u03ba",bblambda:"\u03bb",bbmu:"\xb5",bbnu:"\u03bd",bbxi:"\u03be",bbpi:"\u03c0",bbrho:"\u03c1",bbsigma:"\u03c3",bbtau:"\u03c4",bbupsilon:"\u03c5",bbphi:"\u03c6",bbchi:"\u03c7",bbpsi:"\u03c8",bbomega:"\u03c9",bbdotlessi:"\u0131",bbdotlessj:"\u0237"}),new s("bboldx-delimiterNormal",g.delimiterNormal,{"\\bbLparen":"(","\\bbRparen":")","\\bbLbrack":"[","\\bbRbrack":"]","\\bbLangle":"\u2329","\\bbRangle":"\u232a"}),new f("bboldx-mathchar0miBold",g.mathchar0miBold,{bfbbGamma:"\u0393",bfbbDelta:"\u2206",bfbbTheta:"\u0398",bfbbLambda:"\u039b",bfbbXi:"\u039e",bfbbPi:"\u03a0",bfbbSigma:"\u03a3",bfbbUpsilon:"\u03a5",bfbbPhi:"\u03a6",bfbbPsi:"\u03a8",bfbbOmega:"\u2126",bfbbalpha:"\u03b1",bfbbbeta:"\u03b2",bfbbgamma:"\u03b3",bfbbdelta:"\u03b4",bfbbepsilon:"\u03b5",bfbbzeta:"\u03b6",bfbbeta:"\u03b7",bfbbtheta:"\u03b8",bfbbiota:"\u03b9",bfbbkappa:"\u03ba",bfbblambda:"\u03bfBB",bfbbmu:"\xb5",bfbbnu:"\u03bd",bfbbxi:"\u03be",bfbbpi:"\u03c0",bfbbrho:"\u03c1",bfbbsigma:"\u03c3",bfbbtau:"\u03c4",bfbbupsilon:"\u03c5",bfbbphi:"\u03c6",bfbbchi:"\u03c7",bfbbpsi:"\u03c8",bfbbomega:"\u03c9",bfbbdotlessi:"\u0131",bfbbdotlessj:"\u0237"}),new s("bboldx-delimiterBold",g.delimiterBold,{"\\bfbbLparen":"(","\\bfbbRparen":")","\\bfbbLbrack":"[","\\bfbbRbrack":"]","\\bfbbLangle":"\u2329","\\bfbbRangle":"\u232a"}),new h("bboldx",{mathbb:[g.ChooseFont,"-bboldx","-bboldx-light","-bboldx-bold"],mathbfbb:[g.ChooseFont,"-bboldx-bold","-bboldx","-bboldx-bold"],imathbb:[g.Macro,"\\bbdotlessi"],jmathbb:[g.Macro,"\\bbdotlessj"],imathbfbb:[g.Macro,"\\bfbbdotlessi"],jmathbfbb:[g.Macro,"\\bfbbdotlessj"]}),new f("text-bboldx-mathchar0miNormal",g.mathchar0miNormal,{txtbbGamma:"\u0393",txtbbDelta:"\u2206",txtbbTheta:"\u0398",txtbbLambda:"\u039b",txtbbXi:"\u039e",txtbbPi:"\u03a0",txtbbSigma:"\u03a3",txtbbUpsilon:"\u03a5",txtbbPhi:"\u03a6",txtbbPsi:"\u03a8",txtbbOmega:"\u2126",txtbbalpha:"\u03b1",txtbbbeta:"\u03b2",txtbbgamma:"\u03b3",txtbbdelta:"\u03b4",txtbbepsilon:"\u03b5",txtbbzeta:"\u03b6",txtbbeta:"\u03b7",txtbbtheta:"\u03b8",txtbbiota:"\u03b9",txtbbkappa:"\u03ba",txtbblambda:"\u03bb",txtbbmu:"\xb5",txtbbnu:"\u03bd",txtbbxi:"\u03be",txtbbpi:"\u03c0",txtbbrho:"\u03c1",txtbbsigma:"\u03c3",txtbbtau:"\u03c4",txtbbupsilon:"\u03c5",txtbbphi:"\u03c6",txtbbchi:"\u03c7",txtbbpsi:"\u03c8",txtbbomega:"\u03c9",txtbbdotlessi:"\u0131",txtbbdotlessj:"\u0237"}),new s("text-bboldx-delimiterNormal",g.delimiterNormal,{"\\txtbbLparen":"(","\\txtbbRparen":")","\\txtbbLbrack":"[","\\txtbbRbrack":"]","\\txtbbLangle":"\u2329","\\txtbbRangle":"\u232a"}),new f("text-bboldx-mathchar0miBold",g.mathchar0miBold,{txtbfbbGamma:"\u0393",txtbfbbDelta:"\u2206",txtbfbbTheta:"\u0398",txtbfbbLambda:"\u039b",txtbfbbXi:"\u039e",txtbfbbPi:"\u03a0",txtbfbbSigma:"\u03a3",txtbfbbUpsilon:"\u03a5",txtbfbbPhi:"\u03a6",txtbfbbPsi:"\u03a8",txtbfbbOmega:"\u2126",txtbfbbalpha:"\u03b1",txtbfbbbeta:"\u03b2",txtbfbbgamma:"\u03b3",txtbfbbdelta:"\u03b4",txtbfbbepsilon:"\u03b5",txtbfbbzeta:"\u03b6",txtbfbbeta:"\u03b7",txtbfbbtheta:"\u03b8",txtbfbbiota:"\u03b9",txtbfbbkappa:"\u03ba",txtbfbblambda:"\u03bb",txtbfbbmu:"\xb5",txtbfbbnu:"\u03bd",txtbfbbxi:"\u03be",txtbfbbpi:"\u03c0",txtbfbbrho:"\u03c1",txtbfbbsigma:"\u03c3",txtbfbbtau:"\u03c4",txtbfbbupsilon:"\u03c5",txtbfbbphi:"\u03c6",txtbfbbchi:"\u03c7",txtbfbbpsi:"\u03c8",txtbfbbomega:"\u03c9",txtbfbbdotlessi:"\u0131",txtbfbbdotlessj:"\u0237"}),new s("text-bboldx-delimiterBold",g.delimiterBold,{"\\txtbfbbLparen":"(","\\txtbfbbRparen":")","\\txtbfbbLbrack":"[","\\txtbfbbRbrack":"]","\\txtbfbbLangle":"\u2329","\\txtbfbbRangle":"\u232a"}),new h("text-bboldx",{textbb:[g.ChooseTextFont,"-bboldx","-bboldx-light","-bboldx-bold"],textbfbb:[g.ChooseTextFont,"-bboldx-bold","-bboldx","-bboldx-bold"],itextbb:[g.Macro,"\\txtbbdotlessi"],jtextbb:[g.Macro,"\\txtbbdotlessj"],itextbfbb:[g.Macro,"\\txtbfbbdotlessi"],jtextbfbb:[g.Macro,"\\txtbfbbdotlessj"]}),r.create("text-bboldx",{parser:"text",handler:{macro:["text-bboldx","text-bboldx-mathchar0miNormal","text-bboldx-delimiterNormal","text-bboldx-mathchar0miBold","text-bboldx-delimiterBold"],[d.DELIMITER]:["text-bboldx-delimiterNormal","text-bboldx-delimiterBold"]}});const B=r.create("bboldx",{[i.HANDLER]:{[d.MACRO]:["bboldx","bboldx-mathchar0miNormal","bboldx-delimiterNormal","bboldx-mathchar0miBold","bboldx-delimiterBold"],[d.DELIMITER]:["bboldx-delimiterNormal","bboldx-delimiterBold"]},[i.OPTIONS]:{bboldx:{bfbb:!1,light:!1}},config(b,t){const a=t.parseOptions.packageData.get("textmacros");a&&(a.parseOptions.options.textmacros.packages.push("text-bboldx"),a.textConf.add("text-bboldx",t,{}))},priority:3});MathJax.loader&&MathJax.loader.checkVersion("[tex]/bboldx","4.0.0-beta.7","tex-extension"),l({_:{input:{tex:{bboldx:{BboldxConfiguration:a,BboldxMethods:t}}}}}),function(b,t,a=`@mathjax/${t}`){if(MathJax.loader){const o="undefined"==typeof document?a:`https://cdn.jsdelivr.net/npm/${t}`,l=t.replace(/-font-extension$/,"-extension"),x=(t.replace(/-font-extension$/,""),MathJax.config?.startup?.output||"chtml");e(MathJax.config.loader,"paths",{[l]:o}),e(MathJax.config.loader,"dependencies",{[`[${l}]/${x}`]:[`output/${x}`]}),MathJax.loader.addPackageData(b,{extraLoads:[`[${l}]/${x}`],rendererExtensions:[l]})}}("[tex]/bboldx","mathjax-bboldx-font-extension")})();
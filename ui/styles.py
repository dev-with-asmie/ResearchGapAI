def load_css():
    return """
<style>

/* -----------------------------
Google Font
------------------------------*/

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* -----------------------------
Hide Streamlit Elements
------------------------------*/

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

/* -----------------------------
Background
------------------------------*/

.stApp{

    background:linear-gradient(
        135deg,
        #0B1220,
        #111827
    );

    color:white;

}

/* -----------------------------
Hero Section
------------------------------*/

.hero{

    padding:40px;

    border-radius:25px;

    background:linear-gradient(
        135deg,
        #0F172A,
        #1E293B
    );

    border:1px solid #2E3B4E;

    margin-bottom:30px;

    box-shadow:0px 8px 30px rgba(0,0,0,.35);

}

.hero-title{

    font-size:48px;

    font-weight:700;

    color:white;

}

.hero-sub{

    font-size:18px;

    color:#CBD5E1;

    margin-top:10px;

}

/* -----------------------------
Metric Cards
------------------------------*/

.metric-card{

    background:#1E293B;

    border-radius:18px;

    padding:25px;

    text-align:center;

    border:1px solid #334155;

    transition:.3s;

}

.metric-card:hover{

    transform:translateY(-4px);

    box-shadow:0px 10px 25px rgba(0,255,180,.15);

}

.metric-value{

    font-size:34px;

    color:#00E6A7;

    font-weight:700;

}

.metric-label{

    color:#CBD5E1;

    margin-top:5px;

}

/* -----------------------------
Paper Card
------------------------------*/

.paper-card{

    background:#172033;

    padding:22px;

    border-radius:18px;

    border-left:6px solid #00E6A7;

    margin-bottom:18px;

    box-shadow:0px 5px 18px rgba(0,0,0,.25);

}

/* -----------------------------
Gap Card
------------------------------*/

.gap-card{

    background:#1F2937;

    padding:18px;

    border-radius:15px;

    border-left:5px solid orange;

    margin-bottom:15px;

}

/* -----------------------------
Project Card
------------------------------*/

.project-card{

    background:#16213E;

    padding:22px;

    border-radius:20px;

    border:1px solid #324763;

    margin-bottom:20px;

    box-shadow:0px 8px 18px rgba(0,0,0,.3);

}

/* -----------------------------
Ranking Card
------------------------------*/

.rank-card{

    background:#172033;

    padding:18px;

    border-radius:15px;

    border-left:5px solid gold;

    margin-bottom:15px;

}

/* -----------------------------
Buttons
------------------------------*/

.stButton>button{

    width:100%;

    height:58px;

    border-radius:14px;

    background:linear-gradient(
        90deg,
        #00C896,
        #00E6A7
    );

    color:white;

    font-size:20px;

    font-weight:600;

    border:none;

}

.stButton>button:hover{

    background:linear-gradient(
        90deg,
        #00E6A7,
        #00C896
    );

}

/* -----------------------------
Expander
------------------------------*/

.streamlit-expanderHeader{

    font-size:18px;

    font-weight:600;

}

/* -----------------------------
Tabs
------------------------------*/

.stTabs [data-baseweb="tab"]{

    font-size:17px;

    padding:12px 20px;

}

/* -----------------------------
Sidebar
------------------------------*/

section[data-testid="stSidebar"]{

    background:#111827;

}

/* -----------------------------
Success / Warning
------------------------------*/

.stSuccess{

    border-radius:12px;

}

.stWarning{

    border-radius:12px;

}

.stInfo{

    border-radius:12px;

}

</style>
""" 
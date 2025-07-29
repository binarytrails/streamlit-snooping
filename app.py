import streamlit as st
import streamlit.components.v1 as components

st.title("🕷️ Streamlit Snooping")

url = st.text_input("Enter the target URL", "https://your-react-app.com/api/test")

# Dynamic Content-Type selection
content_type = st.selectbox(
    "Select Content-Type for the request header",
    options=["application/json", "text/plain", "application/x-www-form-urlencoded"],
    index=0
)

if st.button("Fetch"):
    if url:
        st.markdown(f"### JavaScript is now fetching this from your browser with `{content_type}`")

        components.html(f"""
            <script>
            async function fetchFromBrowser() {{
                const resBox = document.getElementById("result");
                if (!resBox) return;
                resBox.textContent = "⏳ Fetching from: {url}";
                try {{
                    const response = await fetch("{url}", {{
                        method: "GET",
                        mode: "cors",
                        redirect: "follow",
                        headers: {{
                            "Content-Type": "{content_type}"
                        }}
                    }});
                    const data = await response.text();
                    resBox.textContent = "✅ Response from {url}:" + "\\n\\n" + data;
                }} catch (err) {{
                    resBox.textContent = "❌ Error: " + err;
                }}
            }}
            window.addEventListener('DOMContentLoaded', fetchFromBrowser);
            </script>
            <pre id="result" style="white-space: pre-wrap; font-size: 0.85em;">Waiting for browser to fetch...</pre>
        """, height=400)
    else:
        st.warning("Please enter a valid URL.")


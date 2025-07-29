import streamlit as st
import streamlit.components.v1 as components

st.title("🕷️ Streamlit Snooping")

url = st.text_input("Enter the Streamlit app URL", "https://your-react-app.com/api/test")

if st.button("Fetch"):
    if url:
        st.markdown("### JavaScript is now fetching this from your browser:")

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
                        redirect: "follow"
                        // no custom headers here
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

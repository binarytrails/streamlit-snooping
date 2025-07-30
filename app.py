import streamlit as st
import streamlit.components.v1 as components

st.title("🕷️ Streamlit Snooping")

url = st.text_input("Enter the target URL", "https://your-react-app.com/api/test")

# Dynamic Content-Type selection
content_type = st.selectbox(
    "Select Content-Type for the request header",
    options=["text/plain", "application/json", "application/x-www-form-urlencoded"],
    index=0
)

if st.button("Fetch"):
    if url:
        st.markdown("### Embedded Page Render:")

        components.html(f"""
            <div style="padding: 1rem; background-color: #f9f9f9; border-radius: 8px;">
              <iframe
                id="targetFrame"
                src="{url}"
                width="100%"
                onload="resizeIframe(this)"
                frameborder="0"
                style="min-height: 800px; width: 100%; border: 1px solid #ccc; border-radius: 6px;"
                sandbox=""
                onerror="document.getElementById('fallback').style.display = 'block';"
              ></iframe>

              <div id="fallback" style="display: none; margin-top: 1em;">
                <p><b>⚠️ Failed to load via iframe — showing raw HTML instead.</b></p>
                <script>
                fetch("{url}")
                  .then(res => res.text())
                  .then(html => {{
                    document.getElementById("fallback").innerHTML += `<pre style='white-space: pre-wrap; font-size: 0.85em; padding: 1em; background: #fff; border: 1px solid #ddd;'>` + html + `</pre>`;
                  }})
                  .catch(err => {{
                    document.getElementById("fallback").innerHTML += "<pre style='color:red;'>Error: " + err + "</pre>";
                  }});
                </script>
              </div>

              <script>
              function resizeIframe(iframe) {{
                // Try to auto-grow to content height (works only for same-origin if allowed)
                try {{
                  const doc = iframe.contentDocument || iframe.contentWindow.document;
                  const height = doc.body.scrollHeight;
                  iframe.style.height = height + "px";
                }} catch (e) {{
                  // Cross-origin frames can't be resized reliably
                  iframe.style.height = "1200px";
                }}
              }}
              </script>
            </div>
        """, height=1500)
    else:
        st.warning("Please enter a valid URL.")


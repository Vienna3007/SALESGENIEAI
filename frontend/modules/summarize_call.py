import streamlit as st

def show():
    st.subheader("Summarize Call")

    st.write("Paste your call/meeting notes below to extract key points and action items.")
    notes = st.text_area("Call Notes / Transcript", height=200)

    if st.button("Summarize"):
        if not notes.strip():
            st.error("Please paste some call notes first.")
        else:
            lines = [l.strip() for l in notes.split("\n") if l.strip()]

            st.markdown("### Key Discussion Points")
            for line in lines[:5]:
                st.write(f"- {line}")

            st.markdown("### Action Items")
            action_lines = [l for l in lines if any(
                kw in l.lower() for kw in ["follow up", "send", "schedule", "need to", "action"]
            )]
            if action_lines:
                for line in action_lines:
                    st.write(f"☐ {line}")
            else:
                st.write("No explicit action items detected.")
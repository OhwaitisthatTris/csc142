# Browser tab data from the session
edge_all_open_tabs = [
    {
        "pageTitle": "<WebsiteContent_eYr62xf8d1bXGb6F6wArD>Solo Code 9 - Simple Blackjack Redux</WebsiteContent_eYr62xf8d1bXGb6F6wArD>",
        "pageUrl": "<WebsiteContent_eYr62xf8d1bXGb6F6wArD>https://albright.instructure.com/courses/8983/assignments/236823?return_to=https%3A%2F%2Falbright.instructure.com%2Fcalendar%23view_name%3Dmonth%26view_start%3D2026-04-14</WebsiteContent_eYr62xf8d1bXGb6F6wArD>",
        "tabId": 108487041,
        "isCurrent": True
    }
]

def get_active_tab(tabs):
    for tab in tabs:
        if tab.get("isCurrent"):
            return tab
    return None

def summarize_tabs(tabs):
    summary = []
    for t in tabs:
        summary.append({
            "id": t.get("tabId"),
            "title": t.get("pageTitle"),
            "url": t.get("pageUrl"),
            "active": t.get("isCurrent")
        })
    return summary

def format_active_tab(tab):
    if tab is None:
        return "No active tab found."

    text = []
    text.append("Active Tab:")
    text.append(f"- Title: {tab['pageTitle']}")
    text.append(f"- URL: {tab['pageUrl']}")
    text.append(f"- Tab ID: {tab['tabId']}")
    return "\n".join(text)

# Run the helpers
active = get_active_tab(edge_all_open_tabs)
all_tabs = summarize_tabs(edge_all_open_tabs)

print("All Tabs:")
print(all_tabs)
print()
print(format_active_tab(active))

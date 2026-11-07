# Read business data

Choose the narrowest available tool that answers the question. Sales summary,
catalog, pricing, marketing and other domain tools preserve Imans semantics.
Use `discover` to find domains or fields beyond the tools already in context.
`search` and `fetch` cover their advertised record types; they are not a global
search over every Imans business fact.

For metrics, establish period, time zone, company/channel filters, currency,
grain and comparison basis. Use Imans canonical definitions and returned
freshness. Label any calculation made by the Bot as derived analysis; keep
forecasts, assumptions and observed facts distinct. Report withheld values as
unavailable rather than zero.

For questions needing a governed query, discover its entity, fields,
relationships, metric definitions and accepted filters before `run_query`.
Use the returned pagination/cursor and budget. A partial page is not the whole
dataset. Use an export for a complete file when the query supports it.
The interface is a governed business query contract, not direct SQL access.

When the user needs provider data now, use `tunnel_accounts` and the discovered
registered operation with `tunnel_read` if available. Report live provenance
separately from synchronized Imans records. A registered live read does not
authorize arbitrary provider URLs, credentials or mutations.

Memory sharing and record visibility are enforced per user and workspace.
Respect withheld data and the reason returned by the server. For an unavailable
operation, explain its discovery reason and suggested setup/consent step.

On throttling, honor the returned retry interval and bounded query budget.
For a persistent upstream failure, report what remains missing. Use the text
and structured payload if the host cannot display Imans widgets.

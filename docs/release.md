# Release and submission

## Validate and package

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s scripts -p "test_*.py"
python scripts/package.py
```

Keep `plugin.json` and `.cursor-plugin/plugin.json` metadata aligned. Bump both
versions together. Record release acceptance using the
[reviewer guide](reviewer-guide.md). The ZIP contains public plugin assets only,
with no Git history, backend source, CI scripts or environment files.

Create a release from a reviewed feature commit, attach the ZIP and SHA-256
sidecar, and retain the source commit. Runtime server changes do not require
inventing a client tool list; the plugin discovers the full authorized surface.
Update skills when the business contract changes, and request re-indexing from
the marketplace for listing updates as required by its publisher process.

## Listing information

Submit at https://x.ai/bot/marketplace/submit-a-plugin and select **Grok Bot**.

- Organization: **Imans AI**; organization handle: **imans-ai**.
- Website: https://imans.ai
- Repository: https://github.com/imans-ai/imans-grok-plugin
- MCP endpoint: https://mcp.imans.ai/mcp
- Logo: use a public, commit-pinned raw URL for `assets/logo.svg`.
- Description: “Connect Grok Bot to Imans business data and supported actions:
  sales, catalog, stock, pricing, finance, marketing, tasks, process drafts,
  reporting and connected integrations. Uses Imans OAuth, workspace permissions
  and approval controls.”
- Testing instructions: use the public reviewer guide in this repository.
- Privacy: https://imans.ai/privacy-policy
- Account support: inside https://app.imans.ai
- Plugin support: https://github.com/imans-ai/imans-grok-plugin/issues

The form also requires the publisher's first/last name, work email, confirmation
of local and in-app testing, and acceptance of Publisher Terms by an authorized
representative. Supply real details at submission time. Do not put review
credentials in the public repository or form's public listing text.

## Publisher decision

The form links to https://cursor.com/marketplace-publisher-terms. Before
acceptance, the authorized publisher needs to settle whether the marketplace's
free-plugin provision covers this free connector to the paid Imans service,
including applicable Usage Credit operations. No exception is assumed by this
package. Approval and listing time depend on marketplace review.

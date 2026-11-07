# Reviewer guide

## Prerequisites

Use a Grok Bot account and an Imans account with a workspace you are allowed to
test. Any private review credentials must be supplied through the review team's
approved private channel. No demo password or privileged token is included.

MCP endpoint: `https://mcp.imans.ai/mcp`. OAuth is discovered from the service;
no API key or client secret needs to be entered into this plugin. Consent
controls workspaces, scopes and connection mode.

## Acceptance run

1. Validate the package locally with `python scripts/validate.py` after
   installing `requirements-dev.txt`. Verify the root manifest, MCP definition,
   logo and skill are discovered by the host's supported plugin importer.
2. Add/authenticate the MCP connection in Grok Bot. Select one test workspace.
   An existing working Imans connection may be reused.
3. Ask: “List my authorized Imans workspaces.” Confirm only consented workspaces
   appear. Ask what operations are available for that workspace; discovery
   should distinguish available, permission-denied and setup-required items.
4. Ask for a sales summary over a period with known data. Compare workspace,
   filters, currency and metric definitions with Imans. An empty workspace
   should report no matching data, not fabricate a result.
5. Ask about another domain your account has, such as catalog, stock, finance,
   marketing or reporting. Use current discovery to choose the operation.
6. With a read-only connection, request a change to a disposable test task.
   The server must refuse the write. With a deliberately authorized writable
   test connection, preview and create a disposable task, then inspect its
   returned operation status and link. Repeat the same intended request only
   using its original idempotency key if testing retry behavior.
7. For process drafts or price publication, inspect a preview in a safe test
   workspace. Price publication's exact-batch approval belongs in Imans.
   Do not approve or publish live prices as part of a general listing review.
8. Request a small export if query access is available. Follow the receipt,
   manifest and download link. Report unavailable scopes explicitly.
9. Revoke the connection in Imans and verify subsequent calls fail. Reconnect
   to restore access. Test a shared Bot separately if team usage is in scope,
   checking the actual Imans identity rather than assuming the chat identity.

Text and structured data are sufficient. Widget rendering is optional and is
not a prerequisite for a successful data query.

## Evidence status

- The Imans maintainer reports the existing remote MCP working in Grok Bot
  (2026-11-06). This is the accepted integration baseline.
- Automated checks validate the package and distribution boundaries; they do
  not log in to Grok Bot or create Imans business records.
- The first marketplace-ready package needs a recorded in-app acceptance run
  for this release. Record host version, plugin commit, tested cases and result;
  keep account identifiers and secrets out of public evidence.

Installing the full plugin does not mean every operation is permitted to every
account. Unsupported, missing-consent and setup-required results are expected
when the corresponding prerequisites are absent.

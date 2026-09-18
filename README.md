# Tester Data Store

This is the first Hermes-only implementation of the Tester data contract.

## Files

- `journals/<run-id>.jsonl`: append-only action/evidence events
- `artifacts/<run-id>/`: screenshots and evidence files
- `findings.jsonl`: findings, status changes, recurrence, escalation
- `questions.jsonl`: questions requiring human clarification
- `decisions.jsonl`: explicit human decisions
- `knowledge.jsonl`: reviewed knowledge that influences future runs
- `index.md`: compact run history
- `reports/<run-id>.md`: final reports

## Design choice
JSONL is used initially instead of DuckDB or a vector database because it is portable, inspectable, append-friendly, and compatible with Hermes' file tools. A query projection can be added later after real runs establish access patterns.

## Required event fields
Journal events should include `type`, `run_id`, `timestamp`, and event-specific fields. Findings should include a stable `fingerprint`, `status`, `severity`, `confidence`, `run_id`, and evidence references. Human decisions must include explicit scope and source.

## Security
Never store passwords, tokens, private keys, or unrelated personal data. Use relative evidence paths.

## Validation
Before finishing a run, validate every journal/findings line as JSON and verify every cited artifact exists.

## Gateway delivery
Mention an absolute `.md` path in the final Hermes response to trigger supported native file attachment delivery. Also provide a short Markdown summary for chat preview.

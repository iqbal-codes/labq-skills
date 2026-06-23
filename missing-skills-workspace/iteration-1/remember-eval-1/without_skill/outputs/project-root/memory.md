# Session Memory

## Last updated
2026-06-23

## What was built
- OAuth login pages added to the application

## Decisions made
- Chose server-side sessions for authentication (over client-side JWT or cookies-only approach)

## Problems solved
- Fixed a callback URL bug in the OAuth flow

## Current state
- OAuth login pages are in place and functional
- All tests are passing
- No secrets, tokens, or credentials stored in this memory

## Next session starting points
- Wire account linking: connect OAuth accounts to existing user accounts

## Open questions
- How should account linking handle users who sign up with multiple OAuth providers?
- What happens if a user has an existing local account and also authenticates via OAuth?

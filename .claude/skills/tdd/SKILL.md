---
name: tdd
description: Follow Test-Driven Development workflow. Use when the user wants to develop a feature or fix using TDD methodology - write failing tests first, then implement.
argument-hint: "[feature or test to write]"
---

# Test-Driven Development Workflow

Follow the TDD cycle for implementing changes.

## The TDD Cycle

### 1. Write a Failing Test

Create an integration test that describes the expected behavior:

```typescript
describe('Feature Name', () => {
  describe('Success Cases', () => {
    test('should do expected thing', async () => {
      const response = await request(app).get('/api/endpoint')
      expect(response.status).toBe(200)
      expect(response.body).toMatchObject(expectedData)
    })
  })

  describe('Failure Cases', () => {
    test('should fail when invalid input', async () => {
      const response = await request(app).get('/api/endpoint?invalid=true')
      expect(response.status).toBe(400)
    })
  })
})
```

### 2. Verify It Fails

Run the test to confirm it fails for the right reason:
```bash
npm test -- --testPathPattern="test-file-name"
```

### 3. Write Minimum Code to Pass

Implement only what's needed to make the test pass. No more.

### 4. Verify It Passes

Run the test again to confirm it passes.

### 5. Repeat

Continue the cycle for the next piece of functionality.

## Guidelines

- Follow testing guidelines at `.claude/guidelines/testing.md`
- Use Minimum Sufficient Testing (MST) - don't over-test
- Integration tests with real HTTP requests (Jest + Supertest)
- Test success cases and all expected failure scenarios
- Favour editing existing tests over creating new ones
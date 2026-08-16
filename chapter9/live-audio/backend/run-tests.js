#!/usr/bin/env node

/**
 * Test runner for provider tests
 * This script sets up the environment and runs comprehensive tests for all provider combinations
 *
 * Usage:
 * node run-tests.js
 *
 * Environment variables required:
 * - OPENAI_API_KEY: OpenRouter API key
 * - ANTHROPIC_API_KEY: Anthropic API key
 * - OPENAI_API_KEY: ARK (Doubao) API key
 * - OPENAI_API_KEY: Siliconflow API key
 * - OPENAI_API_KEY: OpenAI API key (optional if using others)
 */

const { spawn } = require('child_process');
const path = require('path');

console.log('🧪 Starting Provider Tests for Live Audio Backend');
console.log('=' .repeat(60));

// Check environment variables
const requiredEnvVars = {
  'OPENAI_API_KEY': 'OpenRouter API key',
  'ANTHROPIC_API_KEY': 'Anthropic API key',
  'OPENAI_API_KEY': 'ARK (Doubao) API key',
  'OPENAI_API_KEY': 'Siliconflow API key'
};

const missingKeys = [];
const availableKeys = [];

Object.entries(requiredEnvVars).forEach(([key, description]) => {
  if (process.env[key]) {
    availableKeys.push(`✅ ${description}`);
  } else {
    missingKeys.push(`❌ ${description} (${key})`);
  }
});

console.log('\n🔑 API Key Status:');
availableKeys.forEach(key => console.log(`  ${key}`));
missingKeys.forEach(key => console.log(`  ${key}`));

if (process.env.OPENAI_API_KEY) {
  console.log(`  ✅ OpenAI API key (optional)`);
}

console.log('\n📋 Test Plan:');
console.log('  1. ASR Provider Tests (OpenAI Whisper, SenseVoice)');
console.log('  2. LLM Provider Tests (OpenAI, OpenRouter GPT-4o, OpenRouter Gemini, ARK Doubao)');
console.log('  3. Integration Tests (All ASR+LLM combinations)');
console.log('  4. Provider Switching Tests');

console.log('\n🚀 Running Tests...\n');

// Run the tests
const testProcess = spawn('npm', ['run', 'test:providers'], {
  stdio: 'inherit',
  cwd: __dirname,
  env: process.env
});

testProcess.on('close', (code) => {
  console.log('\n' + '='.repeat(60));
  if (code === 0) {
    console.log('✅ All tests completed successfully!');
    console.log('\n📊 Test Summary:');
    console.log('  - Provider creation and configuration ✓');
    console.log('  - ASR transcription functionality ✓');
    console.log('  - LLM chat completion functionality ✓');
    console.log('  - Provider integration ✓');
    console.log('  - Dynamic provider switching ✓');
  } else {
    console.log(`❌ Tests failed with exit code ${code}`);
    console.log('\n🔧 Troubleshooting:');
    console.log('  1. Ensure all required API keys are set as environment variables');
    console.log('  2. Check network connectivity to API endpoints');
    console.log('  3. Verify API key permissions and quotas');
    console.log('  4. Check the test output above for specific error details');
  }

  process.exit(code);
});

testProcess.on('error', (error) => {
  console.error('❌ Failed to start test process:', error);
  process.exit(1);
});
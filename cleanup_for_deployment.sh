# Files to remove before deployment

# These are Next.js/React files that are not needed for Flask app
rm -rf app/
rm -rf components/
rm -rf hooks/
rm -rf lib/
rm -rf public/
rm -rf styles/
rm components.json
rm next.config.mjs
rm package.json
rm pnpm-lock.yaml
rm postcss.config.mjs
rm tsconfig.json

# Test files (optional - can keep for local testing)
# rm test_registration.py
# rm add_sample_data.py
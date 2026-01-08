function helm-login --wraps='aws ecr get-login-password --region eu-central-1 | helm registry login --username AWS --password-stdin 970044563259.dkr.ecr.eu-central-1.amazonaws.com'
    aws ecr get-login-password --region eu-central-1 | helm registry login --username AWS --password-stdin 970044563259.dkr.ecr.eu-central-1.amazonaws.com $argv
end

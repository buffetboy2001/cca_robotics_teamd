# <<branch>> = branch you are pushing to
# <<file>> = file you want to monitor
inotifywait -q -m -e CLOSE_WRITE --format="git commit -m 'auto commit' %w && git push origin <<branch>>" <<file>> | bash

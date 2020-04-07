#!/usr/bin/env bats

load /c/Users/giftm/workspase/shell_test/function.sh

@test "APconfの読み込みができるかcheck　正常" {
export setting_filepath="/c/Users/giftm/workspase/shell_test/AP_conf.conf";
run setpath 
echo "================" >> ./bats.log 
#echo "$setting_filepath" >> ./bats.log
echo "$output" >> ./bats.log 
echo "$status" >> ./bats.log  
echo "================" >> ./bats.log 
[ "${status}" -eq 0 ]
}


@test "load test" {
echo "================" >> ./bats.log 
env1=xxx
echo "$setting_filepath" >> ./bats.log
echo "$output" >> ./bats.log 
echo "${line[1]}" >> ./bats.log
echo "$env1" >> ./bats.log 
echo "$env2" >> ./bats.log 
echo "================" >> ./bats.log 
[ "$env1" = "xxx" ]
}

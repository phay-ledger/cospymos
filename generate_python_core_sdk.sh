for src in $(find /Users/phay/Crypto/cosmos/cosmos-sdk/proto -iname "*.proto")
do protoc --python_out=/Users/phay/Crypto/cosmos/cospymos/proto-generated --proto_path=/Users/phay/Crypto/cosmos/cosmos-sdk/third_party/proto/ --proto_path=/Users/phay/Crypto/cosmos/cosmos-sdk/proto $src
done

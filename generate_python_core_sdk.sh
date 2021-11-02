xecho() {
    echo $1
    exit 1
}


[[ -z "${COSMOS_SDK}" ]] && xecho "Pease clone the official cosmos-sdk repository (https://github.com/cosmos/cosmos-sdk) and set the location to the COSMOS_SDK env variable."

if ! command -v protoc &> /dev/null
then xecho "Please install protoc, the protobuf compiler, to generate the python client"
fi

for src in $(find "${COSMOS_SDK}"/proto -iname "*.proto")
do protoc --python_out=./proto-generated --proto_path="${COSMOS_SDK}"/third_party/proto/ --proto_path="${COSMOS_SDK}"/proto $src
done

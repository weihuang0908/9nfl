// Copyright 2020 The 9nFL Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef TENSORFLOW_CONTRIB_JDFL_KERNELS_DATASET_FL_GRPC_FETCH_DATASET_OP_H_
#define TENSORFLOW_CONTRIB_JDFL_KERNELS_DATASET_FL_GRPC_FETCH_DATASET_OP_H_

#include "tensorflow/core/framework/dataset.h"

#include "tensorflow/contrib/jdfl/rpc/proto/dc_agent.pb.h"
#include "tensorflow/contrib/jdfl/rpc/rpc_bridge/fl_utils.h"
#include "tensorflow/contrib/jdfl/rpc/rpc_bridge/rpc_dc_agent.h"

using namespace ::tensorflow;

namespace jdfl {

class FlGrpcFetchDatasetOp : public DatasetOpKernel {
 public:
  static constexpr const char* const kDatasetType = "FlGrpcFetch";
  static constexpr const char* const kRoleDef = "role_def";
  static constexpr const char* const kMaxRetries = "max_retries";
  static constexpr const char* const kTimeoutInMs = "timeout_in_ms";

  explicit FlGrpcFetchDatasetOp(OpKernelConstruction* ctx);

 protected:
  void MakeDataset(OpKernelContext* ctx, DatasetBase** output) override;

 private:
  class Dataset;
  int max_retries_;
  int timeout_in_ms_;
};

}  // namespace jdfl

#endif  // TENSORFLOW_CONTRIB_JDFL_KERNELS_DATASET_FL_GRPC_FETCH_DATASET_OP_H_

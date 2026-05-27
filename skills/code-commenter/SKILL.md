---
name: "code-commenter"
description: "为代码添加规范中文注释，解释方法使用方法。Invoke when user asks to add comments, explain code, or make code beginner-friendly."
---

# 代码注释专家

这个技能专门为代码添加规范的中文注释，帮助初学者理解代码逻辑和方法的使用方法。

## 何时使用

当用户提出以下需求时，立即调用此技能：
- "帮我添加注释"
- "解释这段代码"
- "让代码更易读"
- "为初学者添加说明"
- "添加方法使用说明"
- "代码需要注释"

## 注释规范

### 1. 注释语言
- **统一使用中文**进行注释和说明
- 保持语言简洁、清晰、易懂

### 2. 注释类型

#### 方法/函数注释（使用多行注释）
```python
"""
功能说明：计算两个数的和

参数：
    a (int/float): 第一个加数
    b (int/float): 第二个加数

返回值：
    int/float: 两个数的和

使用示例：
    result = add(3, 5)  # 返回 8
    result = add(1.5, 2.5)  # 返回 4.0
"""
```

#### 类注释（使用多行注释）
```python
"""
功能说明：用户管理类，用于处理用户相关的操作

主要方法：
    - create_user(): 创建新用户
    - delete_user(): 删除用户
    - update_user(): 更新用户信息

使用场景：
    当需要管理用户信息时使用此类
"""
```

#### 一般语句注释（使用单行注释）
```python
# 初始化变量
count = 0

# 遍历列表中的每个元素
for item in items:
    # 累加计数
    count += 1
```

### 3. 注释内容要求

#### 方法/函数注释必须包含：
1. **功能说明**：简要描述方法的作用（1-2句话）
2. **参数说明**：列出所有参数及其类型和含义
3. **返回值说明**：说明返回值的类型和含义
4. **使用示例**：提供1-2个常见使用场景的代码示例
5. **注意事项**（可选）：说明使用时需要注意的特殊情况

#### 类注释必须包含：
1. **功能说明**：简要描述类的用途
2. **主要方法**：列出类中的重要方法
3. **使用场景**：说明在什么情况下使用这个类

#### 语句注释原则：
- 解释"为什么"而不是"是什么"
- 注释复杂的逻辑判断
- 说明重要的业务规则
- 解释算法的关键步骤

### 4. 注释风格

#### 好的注释示例：
```python
# 检查用户是否已登录
if user.is_authenticated:
    # 允许访问受保护资源
    return protected_data
```

#### 不好的注释示例：
```python
# 如果用户已登录
if user.is_authenticated:
    # 返回数据
    return protected_data
```

## 实施步骤

1. **分析代码结构**
   - 识别所有需要注释的方法、函数、类
   - 理解代码的业务逻辑和算法

2. **添加方法/函数注释**
   - 为每个方法添加多行注释
   - 包含功能、参数、返回值、使用示例

3. **添加类注释**
   - 为每个类添加多行注释
   - 包含功能、主要方法、使用场景

4. **添加语句注释**
   - 为复杂逻辑添加单行注释
   - 解释关键步骤和业务规则

5. **验证注释质量**
   - 确保注释准确反映代码功能
   - 确保注释对初学者友好
   - 确保使用示例可以运行

## 注释模板

### Python方法模板
```python
def function_name(param1, param2):
    """
    功能说明：[一句话描述方法功能]

    参数：
        param1 (type): 参数1的说明
        param2 (type): 参数2的说明

    返回值：
        type: 返回值的说明

    使用示例：
        result = function_name(value1, value2)

    注意事项：
        - 注意点1
        - 注意点2
    """
    # 方法实现
    pass
```

### JavaScript方法模板
```javascript
/**
 * 功能说明：[一句话描述方法功能]
 * 
 * @param {type} param1 - 参数1的说明
 * @param {type} param2 - 参数2的说明
 * @returns {type} 返回值的说明
 * 
 * 使用示例：
 * const result = functionName(value1, value2);
 * 
 * 注意事项：
 * - 注意点1
 * - 注意点2
 */
function functionName(param1, param2) {
    // 方法实现
}
```

### Java方法模板
```java
/**
 * 功能说明：[一句话描述方法功能]
 * 
 * @param param1 参数1的说明
 * @param param2 参数2的说明
 * @return 返回值的说明
 * 
 * 使用示例：
 * ResultType result = methodName(value1, value2);
 * 
 * 注意事项：
 * - 注意点1
 * - 注意点2
 */
public ResultType methodName(Type param1, Type param2) {
    // 方法实现
}
```

## 常见框架注释示例

### PyTorch张量操作
```python
"""
功能说明：对输入张量进行卷积操作

参数：
    x (torch.Tensor): 输入张量，形状为(batch_size, channels, height, width)
    weight (torch.Tensor): 卷积核权重
    bias (torch.Tensor, optional): 偏置项，默认为None

返回值：
    torch.Tensor: 卷积后的输出张量

使用示例：
    import torch
    x = torch.randn(1, 3, 32, 32)  # 批次大小1，3通道，32x32图像
    weight = torch.randn(16, 3, 3, 3)  # 16个3x3卷积核
    output = conv2d(x, weight)  # 输出形状: (1, 16, 30, 30)

注意事项：
- 输入张量必须是4维的
- 卷积核的通道数必须与输入张量的通道数匹配
"""
```

### React组件
```javascript
/**
 * 功能说明：用户列表组件，展示用户信息列表
 * 
 * Props:
 *   users (Array): 用户数据数组，每个元素包含id、name、email等字段
 *   onUserClick (Function): 用户点击时的回调函数
 *   loading (Boolean): 是否正在加载数据
 * 
 * 使用示例：
 *   <UserList 
 *     users={userList}
 *     onUserClick={(user) => console.log(user)}
 *     loading={false}
 *   />
 * 
 * 注意事项：
 * - users数组不能为空，否则会显示空状态
 * - onUserClick是可选的，如果不传则点击无反应
 */
```

## 质量检查清单

完成注释后，检查以下项目：

- [ ] 所有方法/函数都有多行注释
- [ ] 所有类都有多行注释
- [ ] 复杂逻辑都有单行注释
- [ ] 注释使用中文
- [ ] 包含使用示例
- [ ] 参数类型和返回值类型已说明
- [ ] 注释准确反映代码功能
- [ ] 注释对初学者友好
- [ ] 没有过时的注释
- [ ] 注释风格一致

## 注意事项

1. **不要过度注释**：简单的代码不需要注释
2. **保持注释更新**：代码修改时同步更新注释
3. **避免废话**：不要注释显而易见的内容
4. **关注"为什么"**：解释代码的目的和原因，而不是代码本身
5. **使用示例**：提供实际可运行的代码示例帮助初学者理解